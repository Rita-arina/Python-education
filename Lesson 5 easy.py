# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import sys
import os
from shutil import copyfile

def folder_on ():
    for i in range(1,10):
        try:
            os.mkdir('dir_'+str(i))
        except:
            pass
    return 0
def folder_off():
    for i in range(1,10):
        try:
            os.rmdir('dir_'+str(i))
        except:
            pass

print('Директории созданы и удалены')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

def print_dir ():
    dirs = []
    i = 0
    print("List of current dir:")
    for x in os.listdir():
        if os.path.isdir(x):
            i += 1
            print(i,x)
    return 0

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys

def copy_this_file():
    src = str(sys.argv[0])
    dst = src.replace('.py','_copy.py')
    copyfile(src, dst)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys

def copy_file():
    src = str(sys.argv[0])
    dst = src.replace('.py','_copy.py')
    copyfile(src, dst)