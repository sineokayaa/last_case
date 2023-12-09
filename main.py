import os
import RU_LOCAL as RU


def acceptCommand():
    command = input(RU.QUESTION_1)
    flag = False
    while not flag:
        try:
            command = int(command)
            if 1 <= command <= 7:
                flag = True
                return command
            return RU.MISTAKE_1
        except ValueError:
            return RU.MISTAKE_2


def main():
    while True:
        print(os.getcwd())
        print(RU.MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()
