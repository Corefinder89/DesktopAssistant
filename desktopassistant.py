# -*- coding: utf-8 -*-
import sys

from desktop_assistant.data import data
from desktop_assistant.engine.engine import Engine
from desktop_assistant.utility.desktoputility import Desktoputility
from desktop_assistant.utility.utility import Utility


class Desktopassistant:
    def __init__(self):
        self.en = Engine()
        self.du = Desktoputility()
        self.ut = Utility()

    def desktop_main(self):
        # Greet user before starting
        self.du.greeting()
        self.en.speak("Nova here ")
        self.en.speak("What would you like me to do for you ?")

        while True:
            query = self.en.command()
            query = query.lower()

            # Voice greeting
            if query in data.voice_greeting:
                self.du.greetback(query + " " + self.ut.get_current_user())

            # Exit criteria
            if query in data.voice_data_exit:
                self.en.speak("Alright " + self.ut.get_current_user() + "!! Have a nice day")
                sys.exit()

            # Exit if user is wishing good night
            if "night" in query:
                self.en.speak("Good night " + self.ut.get_current_user() + ". Have a tight sleep")
                sys.exit()

            # Search on Google
            if "search" in query:
                output_list = []
                self.en.speak("What should I search for ?")
                query = self.en.command()
                self.du.search_on_google(query, output_list)
                self.en.speak("\nShould I open up the first link for you ?")
                query = self.en.command()
                if query in data.boolean_affirmitive:
                    self.du.open_link(output_list)
                if query in data.boolean_negate:
                    self.en.speak("Alright !!")

            # Telling a joke
            if "joke" in query:
                self.du.tell_a_joke()

            # Open safari
            if "safari" in query:
                self.du.open_application("safari")

            # Open google chrome
            if "chrome" in query:
                self.du.open_application("chrome")

            # Open slack
            if "slack" in query:
                self.du.open_application("slack")

            # Open insomnia
            if "insomnia" in query:
                self.du.open_application("insomnia")


if __name__ == "__main__":
    Desktopassistant().desktop_main()
