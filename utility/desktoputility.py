import datetime
from engine.engine import Engine


class Desktoputility:
    def __init__(self):
        self.en = Engine()

    def greeting(self):
        current_h = int(datetime.datetime.now().hour)
        if 0 <= current_h < 12:
            self.en.speak('Good Morning')
        if 12 <= current_h < 17:
            self.en.speak('Good Afternoon')
        if current_h >= 17 and current_h != 0:
            self.en.speak('Good Evening')

    def greetback(self, query):
        self.en.speak(query)