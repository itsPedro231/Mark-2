# import wolframalpha
import speech_recognition as sp
import pyttsx3 as tts
import os
import openai
import chronological
from gpt import gpt

recognizer = sp.Recognizer()
mic = sp.Microphone()
# engine = tts.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id) # This voice package has to be changed
# engine.setProperty('rate', 145)
# engine.setProperty('volume', 0.6)
# psq = wolframalpha.Client('TOKEN') # a token has to be placed here
y = 0

def micInput():
  print('listening')
  try:
    with mic as source:
      audio = recognizer.listen(source, timeout=2)
      output1 = (recognizer.recognize_google(audio))
      print(output1)
  except:
    output1 = ' . '
  return output1        
  
# in development  
'''def newNotes():
  tts.speak('what is the name of the note?')
  noteName = micInput()
  tts.speak('please tell me the note')
  noteContent = micInput()
  path = 'C:\jarvis_notes\\' + noteName + '.txt'
  newNote = open(path, 'w+')
  newNote.write(noteContent)
  newNote.close()

def deleteNotes():
  files = os.scandir('C:\mark_notes')
  tts.speak('which notes would you like to delete: ', files)

def readNotes():
  files = os.scandir('C:\mark_notes')
  content = 'available notes: ' + str(files)
  tts.speak(content)  

def notes():
  tts.speak('do you want to create, delete or display a note')
  
  output3 = micInput()
  output3 = output3.split()
  for x in output3:
      if x.lower() == 'create' or x.lower() == 'new' or x.lower == 'add':
        newNotes()
      elif x.lower() == 'delete':
        deleteNotes()
      elif x.lower() == 'display' or x.lower() == 'show':
        readNotes()
'''

while True:
  # mic_result1 = micInput().split()
  mic_result1 = "mark"
  for x in mic_result1:
    x = "mark"
    if x.lower() == 'mark':
      # tts.speak('yes sir?')
      print("now")
      # while True:
      #   micResult2 = micInput()
      #   if micResult2.isalpha() or len(micResult2.split()) > 1: break
      # tempResult = micResult2
      # tempResult = tempResult.split()
      # print(tempResult)
      micResult2 = input(">> ")
      # if isinstance(tempResult, list):
      if micResult2:
        # for x in tempResult:
        #   print(x)
        #   if x.lower() == 'notes' or x.lower() == 'note':
        #     notes()
        #     y = 1
        #     break
        if y == 0:
          
          # search = psq.query(micResult2)
          # answer = (next(search.results).text)
          answer = gpt(micResult2)
          # tts.speak(answer)

          continue
          # except Exception as e:
          #   # tts.speak("im sorry sir I couldnt find anything about that on my database")
          #   print(e)
          #   continue

    else: continue  
