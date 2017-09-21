import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data=json.load(open("data.json"))

def dictionary(word):
    word=word.lower()
    if word  in data:
            return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        confirm=input("Did you Mean? %s instead? Enter Y for Yes and N for No."%get_close_matches(word,data.keys())[0])
        if confirm=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "The word is not in dictionary."

    else:
            return "The word doesn't exist"

w=input("Enter a word: ")
output=dictionary(w)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
