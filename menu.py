"""Menu"""
import sys
import os
try:
    import tty
    import termios
    WINDOWS = False
except ImportError:
    import msvcrt
    WINDOWS = True


def clear_term():
    os.system("clear || cls")


def getch():
    """Cross platform getch"""
    if not WINDOWS:
        file_descriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(file_descriptor)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
        return char
    else:
        char = msvcrt.getch()  # ignorar erro (se houver)
        if char in [b'\x00', b'\xe0']:
            char = msvcrt.getch()
        return char.decode()


def arrow_key_menu(options):
    """Arrow key menu"""
    selected = 0

    while True:
        clear_term()
        for index, option in enumerate(options):
            if index == selected:
                print(">> " + option + " <<")
            else:
                print("   " + option)

        char = getch()
        if char == '\x1b':
            next1, next2 = getch(), getch()
            if next1 == '[':
                if next2 == 'A':
                    selected = max(0, selected - 1)
                elif next2 == 'B':
                    selected = min(len(options) - 1, selected + 1)

        elif char == '\r':
            return selected
