import sqlite3
import os
from time import sleep


def get_conn():
    conn = None
    db = 'unoesc.db'

    print('{:>12}'.format(f'SQLite ver.: {sqlite3.version}'))

    path = os.path.abspath(os.getcwd())
    file_path = os.path.join(path, db)
    print(f'Banco de dados')


get_conn()
