from utility.desktoputility import Desktoputility
from engine.engine import Engine
from data import data
import sys
import getpass

sysuser = getpass.getuser()

if __name__ == "__main__":
    en = Engine()
    du = Desktoputility()

    # Greet user before starting
    du.greeting()
    en.speak("Nova here")
    en.speak("What would you like me to do for you ?")

    while True:
        query = en.command()
        query = query.lower()

        # Voice greeting
        if query in data.voice_greeting:
            du.greetback(query+" "+sysuser)

        # Exit criteria
        if query in data.voice_data_exit:
            en.speak("Alright " + sysuser + "!! Have a nice day")
            sys.exit()

        # Exit if user is wishing good night
        if "good night" in query or "night" in query:
            en.speak("Good night " + sysuser + ". Have a tight sleep")
            sys.exit()

        # Search on Google
        if query in data.voice_search:
            outputList = []
            en.speak('What should I search for ?')
            query = en.command()
            du.searchOnGoogle(query, outputList)
            en.speak('Should I open up the first link for you ?')
            query = en.command()
            if query in data.boolean_affirmitive:
                du.openLink(outputList)
            if query in data.boolean_negate:
                en.speak('Alright.')

