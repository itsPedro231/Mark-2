# import wolframalpha
import speech_recognition as sp
from gpt import gpt
from mic import *
from TTS import tts

# in development  
mic_timeout = 2
while True:
  
  if wake_up():
      tts('yes sir?')
      res = capture(mic_timeout)
      
      answer = gpt(res)
      tts(answer)
      
      continue
          
  else: pass