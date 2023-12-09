import os


def uni(entercom: str, *func):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(entercom)
    command = input("Команда: ")
    if command.isdigit() and len(func) > int(command) - 1 >= 0:
        func[int(command) - 1]()
    elif command.isdigit() and int(command) == len(func) + 1:
        return False
    else:
        print('Такой команды нет...')
    input('\nEnter для продолжения\n')
    return True
