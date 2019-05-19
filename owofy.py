import os
import pyperclip

normaltext = input("Text to make the spawn of Satan: ")

def single(normaltext): #Note: Please only use this.
    satantext = normaltext.replace('O', 'OwO')
    satantext = satantext.replace('o', 'owo')
    satantext = satantext.replace('U', 'UwU')
    satantext = satantext.replace('u', 'uwu')
    print("Here, take your satan spawn.\n", satantext)
    pyperclip.copy(satantext)

def owonest(normaltext):
    for l in normaltext:
        if l == 'O':
            normaltext = normaltext.replace('O', 'OwO')
        elif l == 'o':
            normaltext = normaltext.replace('o', 'owo')
        elif l == 'U':
            normaltext = normaltext.replace('U', 'UwU')
        elif l == 'u':
            normaltext = normaltext.replace('u', 'uwu')
    satantext = normaltext
    pyperclip.copy(satantext)
    print("Here, take your satan spawn.\n", satantext)

choice = input("Single or many owofications?\n>")
if choice == 'single':
    single(normaltext)
else:
    owonest(normaltext)
