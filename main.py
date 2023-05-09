"""Main"""
# -*- coding: utf-8 -*-
from menu import arrow_key_menu
# from utils import

def main():
    """Main function"""
    options = ["Consultar", "Incluir", "Alterar", "Excluir"]
    selected_option = arrow_key_menu(options)

    match selected_option:
        case 0:
            print("\nConsulta")
        case 1:
            print("\nInclusão")
        case 2:
            print("\nAlteração")
        case 3:
            print("\nExclusão")

    options = ["Código", "Nome do funcionário", "Data de nascimento", "Salário"]

if __name__ == '__main__':
    main()
