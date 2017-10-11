'''
Created on 6 окт. 2017 г.

@author: Сергей
'''
import platform


def system_data():
    print(platform.architecture())
    # todo
    # need to correct


def system_version():
    if platform.system() == 'Windows':
        print("Your characteristics: " + str(platform.win32_ver()))
    # todo


if __name__ == '__main__':
    system_data()
    system_version()
