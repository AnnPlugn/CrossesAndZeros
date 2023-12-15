from OOP.Board import Board
import universal
import DB


def play_game():

    side_length = int(input("Введите сторону доски: "))
    board = Board(side_length)
    players = ['X', 'O']
    turn = 0

    while True:
        player_symbol = players[turn]
        if board.make_move(player_symbol):
            break

        turn = (turn + 1) % 2

def main():
    run = True
    commands = """==========================================================================
1. Создать БД, результат сохранить в MySQL.
2. Создать таблицу, результат сохранить в MySQL.
3. Начать игру, победитель получает 10 очков.
4. Сохранить все данные из MySQL в Excel.
5. Завершить"""
    while run:
        run = universal.uni(commands,
                            DB.db.check_db, DB.db.check_table, play_game,
                            DB.db.save_to_excel)
    return


if __name__ == '__main__':
    main()
