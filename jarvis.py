from Brain.JarvisBrain import ReplyBrain
from Brain.QNA import QuestionReplier
from Body.Listen import MicConnect
print(">> Starting the Jarvis Wait for some seconds")
from Body.speak import Speak
from Features.clap import Tester
print(">> Starting the Jarvis Wait for some more seconds!!!")
from main import MainTaskExecution
def MainExe():
    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm ready to assist you Sir.")

    while True:

        Data = MicConnect()
        Data=str(Data)
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
           pass

        elif "whatsapp message" in Data:
            pass

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
          Reply=  QuestionReplier(Data)
        
        else:
         Reply=ReplyBrain(Data)
         Speak(Reply)

def clapdetected():
    query= Tester()

    if "True-Mic" in query:
        print("")
        print("clap detected !!")
        print("")
        MainExe()
    else: 
        pass

clapdetected()
