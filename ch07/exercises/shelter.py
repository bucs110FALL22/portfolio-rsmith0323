import time

class Animal:
    def __init__(self, name, type):
        self.id = time.strftime("%d%m%M%S")
        self.name = name
        