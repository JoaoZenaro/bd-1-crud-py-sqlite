# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error, OperationalError
from utils import draw_box, clear, pause
import dao


def menu(conn):
    opcao = 1
    while opcao != 6:
        draw_box([
            "MENU DE OPÇÕES", "───────────────", "1. Consultar", "2. Incluir",
            "3. Alterar", "4. Excluir", "5. Listar", "6. Sair"
        ])

        opcao = int(input('\nOpção [1-6]: ')) if opcao in range(1, 8) else 0

        if opcao == 1:
            clear()
            draw_box(["Efetuar busca por:", "─────────", "1. Código",
                     "2. Nome", "3. Data de Nascimento", "4. Salário", "5. Voltar"])
            opcao_busca = int(
                input('\nOpção [1-5]: ')) if opcao in range(1, 6) else 0
            if opcao_busca == 1:
                dao.search_codigo(conn)
            elif opcao_busca == 2:
                dao.search_nome(conn)
            elif opcao_busca == 3:
                dao.search_data(conn)
            elif opcao_busca == 4:
                dao.search_salario(conn)
            elif opcao_busca != 5:
                clear()

        elif opcao == 2:
            dao.insert(conn)
        elif opcao == 3:
            dao.update(conn)
        elif opcao == 4:
            dao.delete(conn)
        elif opcao == 5:
            dao.select_all(conn)
        elif opcao == 7:  # opção p/ testes
            dao.insert_multiple(conn)
        elif opcao != 6:
            clear()
            print('Opção inválida, tente novamente')
            opcao = 1

    return opcao


if __name__ == '__main__':
    conn = None
    while True:
        try:
            clear()
            conn = dao.getConn()
            dao.criar_tabela(conn)
            if menu(conn) == 6:
                break
        except OperationalError as e:
            print('Erro operacional:', e)
        except sqlite3.DatabaseError as e:
            print('Erro database:', e)
            # Não mostra o traceback
            raise SystemExit()
        except Error as e:
            print('Erro SQLite3:', e)
            # Não mostra o traceback
            raise SystemExit()
        except Exception as e:
            print('Erro durante a execução do sistema!')
            print(e)
        finally:
            if conn:
                print('Liberando a conexão...')
                conn.commit()
                conn.close()
    print('Encerrando...')
