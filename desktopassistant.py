from utility.desktoputility import Desktoputility
from engine.engine import Engine
import data
import sys

if __name__ == "__main__":
    en = Engine()
    du = Desktoputility()

    # Greet user before starting
    du.greeting()
    en.speak('Nova here')
    en.speak('What would you like me to do for you ?')

    while True:
        query = en.command()
        query = query.lower()

        if query in data.voice_greeting:
            du.greetback(query)
            if "good night" in query or "night" in query:
                en.speak("Have a tight sleep")
                sys.exit()

        if query in data.voice_data_exit:
            en.speak('Alright. Have a nice day')
            sys.exit()