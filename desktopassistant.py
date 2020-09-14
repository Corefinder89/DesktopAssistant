import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if voice.languages[0] == u'en_US':
        engine.setProperty('voice', voice.id)
        break


def speak(audio):
    print("Nova: " + audio)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()


speak("Dothraki tribe of Anges way up in the mountains")
