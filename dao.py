# -*- coding: utf-8 -*-
import sqlite3
import os
import utils as cli


def is_table_empty(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM Funcionarios')
    resultado = cursor.fetchone()
    cursor.close()
    return resultado[0] == 0


def table_contains(conn, id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Funcionarios WHERE id=?', (id, ))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado or None


def insert_multiple(conn):
    comando = 'INSERT INTO Funcionarios (nome, data_de_nascimento, salario) VALUES (?, ?, ?)'
    pessoas = [('Fulano', '1980-04-23', '6000'),
               ('Ciclano', '1992-10-15', '4500'),
               ('Beltrano', '1985-07-08', '8000'),
               ('Sicrano', '1998-02-28', '3500'),]
    cursor = conn.cursor()
    cursor.executemany(comando, pessoas)
    conn.commit()
    if cursor:
        cursor.close()


def getConn():
    conn, db = None, 'unoesc.db'

    print(f"{cli.WARNING}SQLite versão: {sqlite3.version}{cli.ENDC}\n")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db)

    if not os.path.isfile(path):
        if input(f'Banco de dados não encontrado, deseja criá-lo? \n'
                 f'Banco será criado em [{os.getcwd()}]! [S/N]: ').upper() != 'S':
            raise sqlite3.DatabaseError('Banco de dados não selecionado!')

    conn = sqlite3.connect(path)
    print(f'BD aberto em [{path}]!\n')
    return conn


def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        data_de_nascimento TEXT,
        salario REAL
    );
    """)
    conn.commit()
    cursor.close()


def select_all(conn, clear=True):
    if is_table_empty(conn):
        cli.draw_box(["TABELA VAZIA"])
        cli.pause(True)
        return

    cli.draw_box(['dbo.Funcionarios'])

    cursor = conn.execute('SELECT * from Funcionarios')
    registros = cursor.fetchall()

    print(
        f'{"ID":^5} {"Nome":^25} {"Data de Nascimento":^25} {"Salario":^10}')
    print('-' * 70)

    for registro in registros:
        print(
            f'{registro[0]:<5} {registro[1]:<25} {registro[2]:<25} {registro[3]:<10}')

    if clear:
        cli.pause(True)
    cursor.close()


def insert(conn):
    cli.header('Inclusão', False)

    nome = input('\nNome: ')
    data_de_nascimento = input('\nData de Nascimento: ')
    salario = input('\nSalario: ')

    sql = 'INSERT INTO Funcionarios (nome, data_de_nascimento, salario) VALUES (?, ?, ?)'
    sql_params = (nome, data_de_nascimento, salario)

    exec_db(conn, sql, sql_params)


def update(conn):
    if is_table_empty(conn):
        cli.draw_box(["TABELA VAZIA"])
        cli.pause()
        return
    select_all(conn, False)
    id = cli.header('Alteração')
    if int(id) == 0:
        return
    resultado = table_contains(conn, id)
    if not resultado:
        print('\nID não existe!')
    else:
        cli.select(resultado)
        nome = input('\nNome: ')
        data_de_nascimento = input('\nData de Nascimento: ')
        salario = input('\nSalario: ')

        sql = 'UPDATE Funcionarios SET nome=?, data_de_nascimento=?, salario=? WHERE id=?'
        sql_params = (nome, data_de_nascimento, salario, id)

        exec_db(conn, sql, sql_params)


def delete(conn):
    if is_table_empty(conn):
        cli.draw_box(["TABELA VAZIA"])
        cli.pause()
        return
    select_all(conn, False)
    id = cli.header('Exclusão')
    if int(id) == 0:
        return
    resultado = table_contains(conn, id)
    if not resultado:
        print('\nID não existe!')
    else:
        cli.select(resultado)
        exec_db(conn, 'DELETE FROM Funcionarios WHERE id=?', id)


def exec_db(conn, sql, sql_params):
    if input('\nConfirma a ação [S/N]? ').upper() == 'S':
        cursor = conn.cursor()

        cursor.execute(sql, sql_params)
        conn.commit()
        if cursor:
            cursor.close()


def search_codigo(conn):
    cli.header('Busca por Código', False)

    if is_table_empty(conn):
        cli.draw_box(["TABELA VAZIA"])
        cli.pause()
        return
    id = int(input("Digite o ID: "))
    if int(id) == 0:
        return
    resultado = table_contains(conn, id)
    if not resultado:
        print('\nNenhum registro encontrado!')
    else:
        cli.draw_box(['Resultado da Busca'])
        cli.select(resultado)


def search_nome(conn):
    cli.header('Busca por Nome', False)

    if is_table_empty(conn):
        cli.draw_box(["TABELA VAZIA"])
        cli.pause()
        return

    nome = input("Digite o Nome: ")
    if nome == '':
        return

    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM Funcionarios WHERE nome like ?', ('%' + nome + '%',))
    resultado = cursor.fetchone()
    cursor.close()

    if not resultado:
        print('\nNenhum registro encontrado!')
    else:
        cli.draw_box(['Resultado da Busca'])
        cli.select(resultado)


def search_data(conn):
    cli.header('Busca por Data de nascimento', False)

    if is_table_empty(conn):
        cli.draw_box(["TABELA VAZIA"])
        cli.pause()
        return

    data_inicio = input("Digite a data de início (YYYY-MM-DD): ")
    data_fim = input("Digite a data de fim (YYYY-MM-DD): ")

    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM Funcionarios WHERE data_de_nascimento BETWEEN ? AND ?', (data_inicio, data_fim))
    resultados = cursor.fetchall()
    cursor.close()

    if not resultados:
        print('\nNenhum registro encontrado!')
    else:
        cli.draw_box(['Resultado da Busca'])
        print(
            f'{"ID":^5} {"Nome":^25} {"Data de Nascimento":^25} {"Salario":^10}')
        print('-' * 70)
        for resultado in resultados:
            print(
                f'{resultado[0]:<5} {resultado[1]:<25} {resultado[2]:<25} {resultado[3]:<10}')
        cli.pause()


def search_salario(conn):
    cli.header('Busca por Salario', False)

    if is_table_empty(conn):
        cli.draw_box(["TABELA VAZIA"])
        cli.pause()
        return

    salario_min = float(input("Digite o salário mínimo: "))
    salario_max = float(input("Digite o salário máximo: "))

    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM Funcionarios WHERE salario BETWEEN ? AND ?', (salario_min, salario_max))
    resultados = cursor.fetchall()
    cursor.close()

    if not resultados:
        print('\nNenhum registro encontrado!')
    else:
        cli.draw_box(['Resultado da Busca'])
        print(
            f'{"ID":^5} {"Nome":^25} {"Data de Nascimento":^25} {"Salario":^10}')
        print('-' * 70)
        for resultado in resultados:
            print(
                f'{resultado[0]:<5} {resultado[1]:<25} {resultado[2]:<25} {resultado[3]:<10}')
        cli.pause()
