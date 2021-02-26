import json
import sys
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word,data.keys()))>0:
        print("DiD you mean %s instead" %get_close_matches(word,data.keys())[0])
        
        decide=input("press y for yes and n for no")
        if decide=="y":
                return data[get_close_matches(word,data.keys())[0]]
                

        else:
            print("you dont get meaning of this words")
            


    else:
        print("doesn,t find")
        
        sys.exit()


    

word=input("enter the word you want to search")
z=translate(word)
if type(z)==list:
    for item in z:
        print(item)
