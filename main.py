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

        command = command.split()

        match command[0].lower():
            case 'a':
                rmdtime, rmddescription = input("Time: "), input("Description: ")

                if rmdtime := CheckTime(rmdtime):
                    print(type(rmdtime))
                    reminder = Reminder(rmdtime, rmddescription)
                    remindersystem.reminders.append(reminder)
                else:
                    print("Invalid timestamp format.")

            case 'r':
                if len(command) != 2:
                    print('Need 2 arguments (r <id>).')
                    continue

                if remindersystem.Delete(int(command[1])):
                    print(f'Removed reminder with id {command[1]}.')

            case 'c':
                if len(command) != 2:
                    print('Need 2 arguments (c <id>).')
                    continue

                if reminder := remindersystem.Get(int(command[1])):
                    rmdtime, rmddescription = input("Change time? (Y/N)"), input("Change description? (Y/N)")

                    if rmdtime == "Y":
                        if checkedtime := CheckTime(input("Time: ")):
                            print(type(checkedtime))
                            reminder.time = checkedtime
                        else:
                            print("Invalid timestamp format.")
                    if rmddescription == "Y":
                        reminder.description = input("Description: ")

            case 'l':
                if not len(remindersystem.reminders):
                    print('No reminders left.')
                    continue

                for reminder in remindersystem.reminders:
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
