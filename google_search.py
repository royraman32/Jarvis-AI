
import pywhatkit
from Body.speak import Speak
import wikipedia
from pywikihow import WikiHow , search_wikihow
from selenium.webdriver.chrome.options import Options

import os


def googlesearch(term):

    query=term.replace("jarvis","")
    query=term.replace("what is","")
    query=term.replace("how to","")
    query=term.replace("who is","")
    query=term.replace("what do you mean by","")
    writeable = str(query)
    oo=open('Database\google.txt',"r+")
    oo.write(writeable)
    oo.close()
    


    Query = str(term)
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result=1
        how_to_func = search_wikihow(query=Query,max_results=max_result)
        assert len(how_to_func) ==1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)
 

    
    else:
        chrome_options=Options()
        chrome_options.headless = True
        search = wikipedia.summary(Query,2)
        Speak("According to your search :" + search)

googlesearch('distance between the india and the uk')


