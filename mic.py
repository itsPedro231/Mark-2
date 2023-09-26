import speech_recognition as sp

recognizer = sp.Recognizer()
mic = sp.Microphone()

def wake_up():
    timeout = 1
    output = capture(timeout)
    if output:
        if "mark" in output.lower(): return True
        else: return False
    else: return False

def capture(timeout_timer):
    print('listening')
    try:
        with mic as source:
            audio = recognizer.listen(source, timeout=timeout_timer, phrase_time_limit=2)
            output = recognizer.recognize_google(audio)
            print(output)
    except:
        output = False
    return output