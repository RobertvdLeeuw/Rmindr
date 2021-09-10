__author__ = "Robert van der Leeuw"
__date__ = "11/9/2021"

import time, json, sys, os
from datetime import datetime
from threading import Thread

from classes import Reminder, ReminderSystem
from argcheck import CheckTime


def InputLoop(remindersystem):
    while True:
        command = input('Enter command:\n> ')

        if not command:
            continue

        match command.lower():
            case 'a':
                rtime, rdescription = input("Time: "), input("Description: ")

                if not (rtime := CheckTime(rtime)):
                    continue

                reminder = Reminder(rtime, rdescription)
                remindersystem.reminderList.append(reminder)

            case 'r':
                pass

            case 'c':
                pass

            case 'l':
                for reminder in remindersystem:
                    print(reminder)

            # Add network stuff. (add/remove connection, invite.)

            case 'h':
                for line in open('sourcefiles/help.txt').readlines():
                    print(line.replace('\n', ''))

            case 'q':
                sys.exit()

            case _:
                print('Invalid argument. Type h for help.')


def TimeCheck(remindersystem):
    while True:
        time.sleep(1)
        remindersystem.Check()


def Main():
    reminderSystem = ReminderSystem(path='reminders')

    timeThread = Thread(target=TimeCheck, args=(reminderSystem, ))
    timeThread.daemon = True
    timeThread.start()

    InputLoop(reminderSystem)


if __name__ == "__main__":
    Main()
