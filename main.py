import time, json, sys, os
from classes import Reminder, ReminderSystem
from threading import Thread


def InputLoop(reminderSystem):
    while True:
        command = input('Enter command:\n> ')

        match command.lower():
            case 'a':
                pass

            case 'r':
                pass

            case 'c':
                pass

            case 'l':
                pass

            # Add network stufff. (add/remove connection, invite.)

            case 'h':
                print("a: add reminder\nr: remove reminder\nc: change reminder l: list reminders\nq: quit")

            case 'q':
                sys.exit()

            case _:
                print('Invalid argument. Type h for help.')


def TimeCheck(reminderSystem):
    pass


def Main():
    reminderSystem = ReminderSystem(path='reminders')

    inputThread = Thread(target=InputLoop, args=(reminderSystem, ))
    inputThread.start()

    timeThread = Thread(target=TimeCheck, args=(reminderSystem, ))
    timeThread.daemon = True
    timeThread.start()


if __name__ == "__main__":
    Main()
