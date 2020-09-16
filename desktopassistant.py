# -*- coding: utf-8 -*-
import getpass
import sys

from data import data
from engine.engine import Engine
from utility.desktoputility import Desktoputility

sysuser = getpass.getuser()


class Desktopassistant:
    def __init__(self):
        self.en = Engine()
        self.du = Desktoputility()

    def desktop_main(self):
        # Greet user before starting
        self.du.greeting()
        self.en.speak("Nova here")
        self.en.speak("What would you like me to do for you ?")

        while True:
            query = self.en.command()
            query = query.lower()

            # Voice greeting
            if query in data.voice_greeting:
                self.du.greetback(query + " " + sysuser)

            # Exit criteria
            if query in data.voice_data_exit:
                self.en.speak("Alright " + sysuser + "!! Have a nice day")
                sys.exit()

            # Exit if user is wishing good night
            if "good night" in query or "night" in query:
                self.en.speak("Good night " + sysuser + ". Have a tight sleep")
                sys.exit()

            # Search on Google
            if query in data.voice_search:
                output_list = []
                self.en.speak("What should I search for ?")
                query = self.en.command()
                self.du.searchOnGoogle(query, output_list)
                self.en.speak("Should I open up the first link for you ?")
                query = self.en.command()
                if query in data.boolean_affirmitive:
                    self.du.openLink(output_list)
                if query in data.boolean_negate:
                    self.en.speak("Alright !!")


if __name__ == "__main__":
    Desktopassistant().desktop_main()
