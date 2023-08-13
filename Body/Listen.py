# hindi or english command

# three fucntions 
# 1) Listen function 2) translate in english 3) connect
# pip install pyAudio     
import speech_recognition as sr  #pip install speechrecognition
from googletrans import Translator   #pip install googletrans==3.1.0a0

 # 1 - listen : hindi or english 

def Listen():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,7) #listening mode in 8 seconds
    
    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='hi')
    
    except:
        return ""
    
    query = str(query).lower()
    return query

# 2- translation

def TranslationHinToEng(Text):
    line = str(Text)
    translator = Translator()
    result = translator.translate(line,dest='en')  # translate the string to english by default 
    data = result.text
    print(f"you : {data}.")
    return data

# 3 - connect 

def MicConnect():
    query=Listen()
    data=TranslationHinToEng(query)
    return data



