# -*- coding: utf-8 -*-
import platform


# import os

# cols, rows = os.get_terminal_size()
# os.system('cls' if os.name == 'nt' else 'clear')
# print('{:^{cols}}'.format("aaa", cols=cols))


if platform.system() == 'Windows':
    import curses
    import curses.ascii
else:
    import curses


options = ["Procurar", "Incluir", "Atualizar", "Remover"]


def menu(stdscr):
    attributes = {}
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0
    option = 0
    while c != 10:
        stdscr.erase()
        stdscr.addstr("Selecione uma opção:\n", curses.A_UNDERLINE)
        for i in range(len(options)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("{0}. ".format(i + 1))
            stdscr.addstr(options[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(options) - 1:
            option += 1

    print("fjsabgoeb")
    stdscr.addstr("You chose {0}".format(options[option]))
    stdscr.getch()


if __name__ == '__main__':
    if platform.system() == 'Windows':
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        try:
            menu(stdscr)
        except Exception as e:
            raise e
        finally:
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
    else:
        curses.wrapper(menu)
