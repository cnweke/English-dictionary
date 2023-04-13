'''
import json

data = json.load(open('data.json'))
dat = data

while True:
    inp = input('Search for word: ').lower()
    for items in dat.keys():
        if inp == items:
            out = dat[inp]
            for p in out:
                print(f'{inp} means:  {p}')

import json

def word(inp):

    data = json.load(open('data.json'))
    dat = data
    for items in dat.keys():
        if items == inp:
            da = dat[inp]
            for it in da:
                return it
    else:
        return 'Not sure you got the spelling of that word right boss '


count = 0

while True:
    inp = input('Enter word here boss: ').lower()
    print(word(inp))
    count += 1
        elif SequenceMatcher(None,W,get_close_matches(W,data, cutoff=0.5)[0]).ratio() :
        mismatch = input(f'Did you mean "{get_close_matches(W,data, cutoff=0.5)[0]}" instead? Enter Y if yes, or N if no:')
        if mismatch == 'Y':
            for item in data[get_close_matches(W,data)[0]]:
                return f'Definition: {item}'
        elif mismatch == 'N':
                return 'Try again abeg'
'''

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(W):

    if W in data:
        return data[W]
    elif W.title() in data:
        return data[W.title()]
    elif W.upper() in data:
        return data[W.upper()]
    elif len(get_close_matches(W,data.keys())) > 0:
        mismatch = input('Did you mean %s instead? Type "Y" for Yes and "N" for No: ' % get_close_matches(W,data.keys())[0]).upper()
        if mismatch == 'Y':
            return data[get_close_matches(W,data.keys())[0]]
        elif mismatch== 'N':
            return 'Try again boss or double check :)'
        else:
            return "Sorry i no too sabi your message boss :("



    else:
        return 'I no too sabi that one boss, please double check pronunciation :('




while True:
    word = input('Enter word here boss: ').lower()
    output = translate(word)
    if isinstance(output,list): #This is to check the data type of the list to confirm if it is true so it won't print out line by line.
        for items in output:
            print(items)
        break
    else:
        print(output)
        break











