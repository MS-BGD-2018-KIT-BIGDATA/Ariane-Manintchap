#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:40:31 2017

@author: ariane
"""

import re
import operator

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.

# creation du cictionnaire de (mots, nombre d'occurances)
def file_dict(filename):
    countwords = {}
    file = open(filename)
    for word in file.read().split():
        word=word.lower()
        word = re.sub(r"([?!--.:\[_`])",'', word)
        if word not in countwords:
            countwords[word] = 1
        else:
            countwords[word] = countwords[word] + 1
    return countwords


# affichage du dictionnaire

def print_words(filename):
    countwords = file_dict(filename)
    dictio = sorted(countwords.keys())
    for word in dictio:
        print(word, countwords[word])

# affichage des 10 premiers mots du dictionnaire
def print_top(filename):
    countwords = file_dict(filename)
    dictio = sorted(countwords.items(), key=operator.itemgetter(1),reverse=True)
    print(dictio[:10])

print_words('/home/ariane/Documents/Session1/INFMDI721_KDS/Ariane-Manintchap/Lesson 1/alice.txt')
print_top('/home/ariane/Documents/Session1/INFMDI721_KDS/Ariane-Manintchap/Lesson 1/alice.txt')




