'''
Group:
Varfolomeeva Victoria: 95
Sineokaya Anastasia:
'''
import os
import RU_LOCAL as RU


def accept_command():
    '''
    Function to check the correctness of the command
    :return: if command is correct then return command, else return error message
    '''
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
    '''
    Function determines by the command number which function to call
    :param command: number of command
    :return: None
    '''
    if command == 1:
        print(os.listdir())
    if command == 2:
        moveUp()
    if command == 3:
        moveDown('')
    if command == 4:
        print(countFiles(''))
    if command == 5:
        print(countBites(''))
    if command == 6:
        target = input(RU.FILENAME)
        findFiles(target, '')


def moveUp():
    '''
    Function for moving up a catalog level
    :return: None
    '''
    os.chdir('../')


def moveDown(current_dir):
    '''
    The function requests the name of the subdirectory, and if it is correct, it goes to this subdirectory
    :param current_dir: current file directory
    :return: None
    '''
    flag = False
    while not flag:
        print(os.listdir())
        current_dir = input(RU.QUESTION_2)
        try:
            os.chdir(current_dir)
            flag = True
        except FileNotFoundError:
            print(RU.MISTAKE_3)
        except OSError:
            print(RU.MISTAKE_3)


def countFiles(path):
    '''
    The function counts the number of files in the directory
    :param path: directory in which to count the number of files
    :return: count of files
    '''
    case = os.listdir()
    count = 0
    for i in range(len(case)):
        if os.path.isdir(case[i]):
            count += countFiles(os.chdir(case[i]))
        else:
            count += 1
    return count


def countBites(path):
    '''
    The function calculates the total volume in bytes of all files in the directory
    :param path: directory in which to count the total volume in bytes of all files
    :return: total volume in bytes of all files
    '''
    case = os.listdir()
    count = 0
    try:
        for i in range(len(case)):
            if os.path.isdir(case[i]):
                count += countBites(os.chdir(case[i]))
            else:
                count += os.path.getsize(case[i])
    except OSError:
        count = count
    return count


def findFiles(target, path):
    '''
    The function generates a list of paths to files whose names contain target
    :param target: part of the file name
    :param path: directory in which to generate a list of paths to files
    :return: None
    '''
    case = os.listdir()
    flag = 0
    for i in range(len(case)):
        if os.path.isdir(case[i]):
            findFiles(target, os.chdir(case[i]))
        else:
            if target in case[i]:
                print(os.path.abspath(case[i]))
                flag = 1
    if flag == 0:
        print(RU.NOFILE)


def main():
    '''
    A function that displays the path to the current directory and menu
    :return: None
    '''
    while True:
        print(os.getcwd())
        print(RU.MENU)
        command = accept_command()
        run_command(command)
        if command == 7:
            print(RU.FINAL)
            break


if __name__ == '__main__':
    main()
