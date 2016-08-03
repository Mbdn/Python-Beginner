#coding: utf-8

import random
from urllib import urlopen
import sys

#字符串
WORD_URL = "http://learncodethehardway.org/wirds.txt"
WORDS = []

#字典
phrases = {
        "class ###(###):":
        "Make a class named ### that is-a ###.",
        "Class ###(object):\n\tdef __init__(self, ***)":
          "Class ### has-a __init__ thar rales self and *** parametres.",
          "*** = ###()":
            "Set *** to an instance of class ###.",
            "***.***(@@@)":
                "From *** get the *** function, and call it with parameters selfn, @@@.",
            "***.*** ='***'":
                "From *** get the *** atterbute and set it to '***'"
        }
#do they want to drill pharase first

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(senippet, phrase):
    class_names = [w.capitalize() for w in
            random.sample(WoRDS, snippet.count("###"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("###", word, 1)

        #fake other names
        for word in other_names:
            result = resule.replace("***", word, 1)

        #fale parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
