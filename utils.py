# -*- coding: utf-8 -*-
import os

WARNING = '\033[93m'
ENDC = '\033[0m'
WIDTH = 40 - 2


def draw_box(items):
    print("┌" + "─" * WIDTH + "┐")
    for i in items:
        print("│" + "{: ^{}s}".format(i, WIDTH) + "│")
    print("└" + "─" * WIDTH + "┘")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def header(msg, get_id=True):
    draw_box([msg])
    if get_id:
        return input('ID (0 para voltar): ') or 0
    else:
        return


def select(registro):
    print(
        f'{"ID":^5} {"Nome":^25} {"Data de Nascimento":^25} {"Salario":^10}')
    print('-' * 70)
    print(
        f'{registro[0]:<5} {registro[1]:<25} {registro[2]:<25} {registro[3]:<10}')


def pause(should_clear=False):
    input('\nPressione <ENTER> para continuar')
    if should_clear:
        clear()
