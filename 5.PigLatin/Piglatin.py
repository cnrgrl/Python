"""
Pig Latin (www.wikihow.com/Speak-Pig-Latin) is a common children’s "secret" language in English-speaking 
countries. （It’s normally secret among children who forget that their parents were once children 
themselves.) The rules for translating words from English into Pig Latin are quite simple:

If the word begins with a vowel (a, e, i, o, or u), then add way to the end of the word. 
So air becomes airway and eat becomes eatway.
If the word begins with any other letter, then we take the first letter, put it on the end of the word, 
and then add ay. Thus, python becomes ythonpay and computer becomes omputercay.
(And yes, I recognize that the rules can be made more sophisticated. Let’s keep it simple for 
the purposes of this exercise.)

For this exercise, write a Python program that asks the user to enter an English word. 
Your program should then print the word, translated into Pig Latin. You may assume that the word contains
 no capital letters or punctuation.
"""

vowel=['a', 'e', 'i', 'o','u']

text=input('Bitte schreiben sie einen Satz: ')

textlist=text.split()
print(text)
for word in textlist:
    if (word[0][0] in vowel):
        print(word[0:]+'way', end=' ')
    else:
        print(word[1:] + word[0][0] + 'ay', end=' ')