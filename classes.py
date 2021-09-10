__author__ = "Robert van der Leeuw"
__date__ = "11/9/2021"

from datetime import datetime, timedelta
import ctypes


class Reminder:
    done = False

    def __init__(self, time: datetime, description: str):
        self.time = time
        self.description = description

    def PopUp(self):
        if self.done:
            return

        mbox = ctypes.windll.user32.MessageBoxW(0, self.description, "Rmindr", 1)

        match mbox:
            case 1:  # IDYES
                self.done = True

            case 2:  # IDCANCEL
                self.time += timedelta(minutes=10)  # Snoozing.

            case _:
                self.time += timedelta(seconds=5)

    def __str__(self):
        return f"{self.time}: {self.description}"


class ReminderSystem:
    reminderList = list()

    def __init__(self, path: str):
        self.path = path

    def Check(self):
        for reminder in [rmd for rmd in self.reminderList if not rmd.done]:
            if (reminder.time - datetime.now()).seconds > 0:
                continue

            reminder.PopUp()
