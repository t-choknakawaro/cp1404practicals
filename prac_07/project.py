import datetime
COMPLETION = '100'


class Project:

    def __init__(self, name, start_date, priority, cost, percentage):
        self.name = name
        self.startdate = start_date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f'{self.name}, start: {self.startdate}, priority {self.priority}, estimate: ${self.cost}, completion: {self.percentage}%'

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        return

    def is_completion(self):
        return self.percentage == COMPLETION