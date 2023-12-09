from tabulate import tabulate
from colorama import init, Fore, Back, Style


stor = int(input("Введите сторону доски: "))
numb = int(input("Количество элементов: "))

from tabulate import tabulate

def print_board(board):
    table_data = []
    field = ['XO'] + [str(i) for i in range(1, stor+1)]
    for i, row in enumerate(board, start=1):
        table_data.append([Fore.GREEN + str(i) + Style.RESET_ALL] + row)
    headers = [Fore.GREEN + cell + Style.RESET_ALL for cell in field]
    table_with_headers = [headers] + table_data
    formatted_table = tabulate(table_with_headers, tablefmt="fancy_grid")
    print(formatted_table)
    return

def check_win(board, symbol):
    for i in range(numb):
        if all([board[i][j] == symbol for j in range(numb)]) or all([board[j][i] == symbol for j in range(numb)]):
            return True
        if all([board[i][i] == symbol for i in range(numb)]) or all([board[i][numb - 1 - i] == symbol for i in range(numb)]):
            return True
        return False


def check_valid(board, row, col):
    return 0 <= row < stor and 0 <= col < stor and board[row][col] == '.'


def main():
    board = [['.'] * stor for _ in range(stor)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player_symbol = players[turn]
        print(f"Ход игрока {player_symbol}")

        row = int(input("Выберите номер строки (от 0 до %s): " % str(stor)))
        col = int(input("Выберите номер столбца (от 0 до %s): " % str(stor)))

        if check_valid(board, row, col):
            board[row][col] = player_symbol
            if check_win(board, player_symbol):
                print_board(board)
                print(f"Игрок {player_symbol} победил!")
                break
            elif all([cell != '.' for row in board for cell in row]):
                print_board(board)
                print("Ничья!")
                break
            turn = 1 - turn
        else:
            print("Недопустимый ход. Попробуйте снова.")


if __name__ == '__main__':
    main()
