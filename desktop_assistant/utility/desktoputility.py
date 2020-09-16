# -*- coding: utf-8 -*-
import datetime
import webbrowser

import requests
from googlesearch import search

from desktop_assistant.engine.engine import Engine
from desktop_assistant.utility.utility import Utility


class Desktoputility:
    def __init__(self):
        self.en = Engine()
        self.ut = Utility()

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

    def search_on_google(self, query, output_list):
        self.en.speak('The top five search results from Google  are listed below.')
        for output in search(query, num_results=5, lang="en"):
            print(output)
            output_list.append(output)
        return output_list

    def open_link(self, output_list):
        self.en.speak("Here's the first link for you.")
        webbrowser.open(output_list[0])

    def tell_a_joke(self):
        parser = self.ut.parse_config()
        api_endpoint = parser.get("source", "api_joke")
        response = requests.get(
            api_endpoint, headers={
                "accept": "application/json",
                "content-type": "application/json"
            }
        )
        if response.status_code == 200:
            self.en.speak("Okay. Here's one")
            self.en.speak(str(response.json().get("joke")))
