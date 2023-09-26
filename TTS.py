import pyttsx3 as pytts

def tts(input):
    engine = pytts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # This voice package has to be changed
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 0.6)   
    pytts.speak(input) 
    return True