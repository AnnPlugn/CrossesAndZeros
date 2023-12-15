from tabulate import tabulate
from colorama import init, Fore, Back, Style
import os
import DB
arr_x = []
arr_o = []
class Board:
    def __init__(self, side_length):
        self.size = side_length
        self.numb = int(input("Количество элементов: "))
        self.board = [['.'] * self.size for _ in range(self.size)]

    def print_board(self):
        table_data = []
        field = ['XO'] + [str(i) for i in range(1, self.size + 1)]
        for i, row in enumerate(self.board, start=1):
            table_data.append([Fore.GREEN + str(i) + Style.RESET_ALL] + row)
        headers = [Fore.GREEN + cell + Style.RESET_ALL for cell in field]
        table_with_headers = [headers] + table_data
        formatted_table = tabulate(table_with_headers, tablefmt="fancy_grid")
        print(formatted_table)
        return

    def check_win(self, symbol):
        for i in range(self.numb):
            if all([self.board[i][j] == symbol for j in range(self.numb)]) or all(
                    [self.board[j][i] == symbol for j in range(self.numb)]):
                return True
            if all([self.board[i][i] == symbol for i in range(self.numb)]) or all(
                    [self.board[i][self.numb - 1 - i] == symbol for i in range(self.numb)]):
                return True
        return False

    def check_valid(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == '.'

    def make_move(self, player_symbol):
        self.print_board()
        print(f"Ход игрока {player_symbol}")

        row = int(input("Выберите номер строки (от 0 до %s): " % str(self.size-1)))
        col = int(input("Выберите номер столбца (от 0 до %s): " % str(self.size-1)))
        if player_symbol == 'X':
            arr_x.append([row, col])
        else:
            arr_o.append([row, col])
        if self.check_valid(row, col):
            self.board[row][col] = player_symbol
            if self.check_win(player_symbol):
                self.print_board()
                print(f"Игрок {player_symbol} победил!")
                if player_symbol == 'X':
                    DB.db.save_result(str(10), str(0), arr_x, arr_o)
                else:
                    DB.db.save_result(str(0), str(10), arr_x, arr_o)
                return True
            elif all(all(cell != '.' for cell in row) for row in self.board):
                self.print_board()
                print("Ничья!")
                DB.db.save_result(str(5), str(5), arr_x, arr_o)
                return True
        return False


os.system('cls' if os.name == 'nt' else 'clear')
