import datetime
import webbrowser
from engine.engine import Engine
from googlesearch import search


class Desktoputility:
    def __init__(self):
        self.en = Engine()

    def greeting(self):
        current_h = int(datetime.datetime.now().hour)
        if 0 <= current_h < 12:
            self.en.speak("Good Morning")
        if 12 <= current_h < 17:
            self.en.speak("Good Afternoon")
        if current_h >= 17 and current_h != 0:
            self.en.speak("Good Evening")

    def greetback(self, query):
        self.en.speak(query)

    def searchOnGoogle(self, query, outputList):
        self.en.speak('The top five search results from Google  are listed below.')
        for output in search(query, num_results=5, lang="en"):
            print(output)
            outputList.append(output)
        return outputList

    def openLink(self, outputList):
        self.en.speak("Here's the first link for you.")
        webbrowser.open(outputList[0])
