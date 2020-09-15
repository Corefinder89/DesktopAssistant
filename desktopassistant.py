from utility.desktoputility import Desktoputility
from engine.engine import Engine
import data
import sys
import getpass

sysuser = getpass.getuser()

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

        if query in data.voice_data_exit:
            en.speak("Alright " + sysuser + "!! Have a nice day")
            sys.exit()

        if "good night" in query or "night" in query:
            en.speak("Good night " + sysuser + ". Have a tight sleep")
            sys.exit()
