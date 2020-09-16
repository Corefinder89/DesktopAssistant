import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')


class Engine:
    for voice in voices:
        if voice.languages[0] == u'en_US':
            engine.setProperty("voice", voice.id)
            break

    def speak(self, audio):
        print("Nova: " + audio)
        engine.say(audio)
        engine.runAndWait()
        engine.stop()

    def command(self):
        cmd = sr.Recognizer()
        with sr.Microphone() as source:
            cmd.adjust_for_ambient_noise(source)
            print("\n"+"Listening....")
            audio = cmd.listen(source)
            try:
                query = cmd.recognize_google(audio, language="en-us")
                print("User: " + query + "\n")
            except sr.UnknownValueError:
                self.speak("Sorry ! I did not get that. Could you please type it out ?")
                query = str(input("Command: "))

        return query
