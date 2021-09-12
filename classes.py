__author__ = "Robert van der Leeuw"
__date__ = "11/9/2021"

from datetime import datetime, timedelta
from enum import Enum
import ctypes, random


class Status(Enum):
    DONE = 0
    PENDING = 1
    DELETED = 2
    ERROR = 3


class Reminder:
    status = Status.PENDING

    def __init__(self, time: datetime, description: str):
        self.time = time
        self.description = description
        self.id = random.randint(100000, 999999)  # Eventually get vacant ones from database.

    def PopUp(self):
        if self.status != Status.PENDING:
            return

        mbox = ctypes.windll.user32.MessageBoxW(0, self.description, "Rmindr", 1)

        match mbox:
            case 1:  # IDYES
                self.status = Status.DONE

            case 2:  # IDCANCEL
                self.time += timedelta(minutes=10)  # Snoozing.

            case _:
                self.time += timedelta(seconds=5)

    def __str__(self):
        return f"{self.id}: ({self.time.strftime('%d %B %Y %H:%M')}: {self.description})"


class ReminderSystem:
    reminders = list()

    def __init__(self, path: str):
        self.path = path

    def Check(self):
        for reminder in [rmd for rmd in self.reminders if rmd.status == Status.PENDING]:
            if (reminder.time - datetime.now()).seconds > 0:
                continue

            reminder.PopUp()

    def Get(self, id: int):
        result = [rmd for rmd in self.reminders if rmd.id == id]

        if not len(result):  # No result => len = 0 => not 0 => not False
            print(f"Reminder with id {id} not found.")
            return

        return result[0]

    def Delete(self, id: int):
        if reminder := self.Get(id):
            self.reminders.remove(reminder)

            # reminder.status = Status.DELETED
            del reminder

            return True
