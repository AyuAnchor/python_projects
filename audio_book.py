import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
engine.say('arey motherfucker bhosdeekey')
engine.runAndWait()

