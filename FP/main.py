from tabulate import tabulate
from colorama import Fore, Style
import db1
import universal1

stor = int(input("Введите сторону доски: "))
numb = min(int(input("Количество элементов: ")), stor)
arr_x = []
arr_o = []

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
        if all([board[i][j] == symbol for j in range(numb)]) or all(
                [board[j][i] == symbol for j in range(numb)]):
            return True
        if all([board[i][i] == symbol for i in range(numb)]) or all(
                [board[i][numb - 1 - i] == symbol for i in range(numb)]):
            return True
    return False


def check_valid(board, row, col):
    return 0 <= row < stor and 0 <= col < stor and board[row][col] == '.'


def play_game():
    board = [['.'] * stor for _ in range(stor)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player_symbol = players[turn]
        print(f"Ход игрока {player_symbol}")

        row = int(input("Выберите номер строки (от 0 до %s): " % str(stor-1)))
        col = int(input("Выберите номер столбца (от 0 до %s): " % str(stor-1)))

        if player_symbol == 'X':
            arr_x.append([row, col])
        else:
            arr_o.append([row, col])
        if check_valid(row, col):
            board[row][col] = player_symbol
            if check_win(player_symbol):
                print_board()
                print(f"Игрок {player_symbol} победил!")
                if player_symbol == 'X':
                    db1.save_result(str(10), str(0), arr_x, arr_o)
                else:
                    db1.save_result(str(0), str(10), arr_x, arr_o)
                return True
            elif all(all(cell != '.' for cell in row) for row in board):
                print_board()
                print("Ничья!")
                db1.save_result(str(5), str(5), arr_x, arr_o)
                return True
        return False

def main():
    run = True
    commands = """==========================================================================
1. Создать БД, результат сохранить в MySQL.
2. Создать таблицу, результат сохранить в MySQL.
3. Начать игру, победитель получает 10 очков.
4. Сохранить все данные из MySQL в Excel.
5. Завершить"""
    while run:
        run = universal1.uni(commands,
                            db1.check_db, db1.check_table, play_game,
                            db1.save_to_excel)
    return

if __name__ == '__main__':
    main()
