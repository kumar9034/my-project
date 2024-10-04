import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


recongnizer =sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def processCommand(c):
    if"open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.py.music[song]
        webbrowser.open(link)

if __name__=="__main__":
    speak("Initializing jarvis.....")
    while True:
        # obtain audio from the microphone
      r = sr.Recognizer()
      

      
# recognize speech using Sphinx
      print("recongnizer...")
      try:
          with sr.Microphone() as source:
              print("listening...")
              audio = r.listen(source)  
          word = r.recognize_google(audio)
          if (word.lower() == " jarvis"):
              speak("Ya")
            #   listen for command
              with sr.Microphone() as source:
                     print("jarvis active...")
                     audio = r.listen(source) 
                     command = r.recognize_google(audio)
                    #  print(command)
                     processCommand(command)

   
      except sr.RequestError as e:
              print(" error; {0}".format(e))
      
       



