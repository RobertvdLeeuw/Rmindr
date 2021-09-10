from enum import Enum

class Reminder:
    def __init__(self, time, description):
        self.time = time
        self.description = description

    @property
    def time(self):
        return self.time

    @time.setter
    def time(self, newtime):
        self.time = newtime

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, newdescription):
        self.description = newdescription


class ReminderSystem:
    reminderList = list()

    def __init__(self, path):
        self.path = path
