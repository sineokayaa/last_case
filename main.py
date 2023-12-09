import os
import RU_LOCAL as RU


def accept_command():
    flag = False
    while not flag:
        command = input(RU.QUESTION_1)
        try:
            command = int(command)
            if 1 <= command <= 7:
                flag = True
                return command
            else:
                print(RU.MISTAKE_1)
        except ValueError:
            print(RU.MISTAKE_2)

def run_command(command):
    if command == 1:
        print(os.listdir())
    if command == 2:
        moveUp()
    if command == 3:
        moveDown(current_dir='')
    if command == 4:
        print(countFiles(path=''))

def moveUp():
    os.chdir('../')

def moveDown(current_dir):
    flag = False
    while not flag:
        print(os.listdir())
        current_dir = input(RU.QUESTION_2)
        try:
            os.chdir(current_dir)
            flag= True
        except FileNotFoundError:
            print(RU.MISTAKE_3)
        except OSError:
            print(RU.MISTAKE_3)
def countFiles(path):
    case = os.listdir()
    count = 0
    for i in range(len(case)):
        if os.path.isfile(case[i]):
            count += 1
        elif os.path.isdir(case[i]):
            count += countFiles(os.chdir(case[i]))
    return count




def main():
    while True:
        print(os.getcwd())
        print(RU.MENU)
        command = accept_command()
        run_command(command)
        if command == 7:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()
