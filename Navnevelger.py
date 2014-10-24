
""" Du må ha en whitespace-linje på slutten
    av tekstdokumentet. Hvis ikke så kommer
    Den til å lese av det første og det
    siste navnet samtidig """
# Må bruke Python 2.7

	
"""
Jeg fikset lesingen av tekstfilen.
Applikasjonen virker ikke helt som den er tenkt akkurat nu.
Mulig jeg har en eldre versjon av koden :)
Tips:
1. Legg filnavnet i en variabel så kan du gjenbruke den rundt omkring.
2. Er det hensiktsmessig å lagre resultatet i filen?
3. Det man egentlig vil ha output på er ett utvalgt navn per klikk.
4. Arnstein hjelper deg videre i morgen om det trengs :)

"""
import sys
from tkinter import *
import random
from random import shuffle

import random
lineWithTickets = []

with open('Test.txt', 'r') as infile:
    lines = infile.readlines()
for line in lines:
    numTickets = int(line.split()[2])
    for ticket in range(0, numTickets):
	    lineWithTickets.append(line)




random.shuffle(lineWithTickets)

print("." *30)
with open('Test3.txt', 'w') as outfile:
    outfile.writelines(lineWithTickets)


def nameLabel():
    nameLabel.configure(text= f.readline())

def deleteFile():
	f.close()
	tf = open("Test3.txt", 'w+')
	tf.truncate()
	mGui.destroy()
	
	
f = open("Test3.txt", 'r+')

mGui = Tk()

mGui.title("Navnevelger")

mGui.geometry("600x200")

pickButton = Button(text="Trykk på!", command=nameLabel)
pickButton.pack()

nameLabel= Label(text="", font=('Arial Black', 32))
nameLabel.pack()

quitButton = Button(text="Avslutt", command=deleteFile)
quitButton.pack()


mGui.mainloop()
