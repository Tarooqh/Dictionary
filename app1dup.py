import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn=input("Did you mean %s instead? Enter Y is Yes,or N if No:" %get_close_matches(word, data.keys())[0])

        if yn =="Y" or "y" :
            return data[get_close_matches(word, data.keys())[0]]
        elif yn =="N" or "n":
            return "Word doesn't exit. Please recheck "
        else:
            return "please enter a valid choice"
    else:
        return "The word does not exist. Get your spellings right Dumbass!"

while True:
    word = input(" To quit enter 'quit!'.\nEnter the word: ")
    if word == "q!":
        break
    output = (translate(word))
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
