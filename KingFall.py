import time
import sys
import threading
from DialogueOptions import options

class user():
    people = 0
    tech = 0
    karma = 0

    def change(self, p, t, k):
        self.people += p
        self.tech += t
        self.karma += k
    
    def getInfo(self):
        return self.people, self.tech, self.karma


def isTerminal(people, tech, karma, year):
    if people <= -5:
        print("The people hate you now, sorry you lose")
        print(f"year: {year}\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")
        exit(0)

    elif people >= 5:
        print("The people are in love with you and you can do no wrong. You win!!")
        print(f"year: {year}\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")
        exit(0)

    if karma <= -5:
        print("You hate yourself for the things you've done, I'm sorry but you lose")
        print(f"year: {year}\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")
        exit(0)

    elif karma >= 5:
        print("You feel great about yourself and feel like retiring. You win!!")
        print(f"year: {year}\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")
        exit(0)

    if tech <= -5:
        print("The technological world has not progressed and you will lose your job. I'm sorry bout that loss")
        print(f"year: {year}\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")
        exit(0)
        
    elif tech >= 5:
        print("Technology is flourishing and you're the godfather of it. You win!!")
        print(f"year: {year}\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")
        exit(0)

def play():
    year = 2010
    ops = options()
    usr = user()

    initial_in = input("Challenge mode or coninuous?: ")

    if initial_in.lower() == 'challenge':

        while (usr.people, usr.tech, usr.karma > -5):

            people, tech, karma = usr.getInfo()
            print(f"year: {year}\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")

            dialogue, p, t, k = ops.find_dialogue_option()
            print(dialogue)

            userin = input("Yes or No: ")
            if userin.lower()=='yes':
                usr.change(p, t, k)
            if userin.lower()=='no':
                usr.change(-p, -t, -k)

            year+=1
            isTerminal(usr.people, usr.tech, usr.karma, year)

    elif initial_in.lower() == 'continuous':

        while True:
            
            people, tech, karma = usr.getInfo()
            print(f"year: {year}\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")

            dialogue, p, t, k = ops.find_dialogue_option()
            print(dialogue)

            userin = input("Yes, No or q to quit: ")
            if userin.lower()=='yes':
                usr.change(p, t, k)
            if userin.lower()=='no':
                usr.change(-p, -t, -k)

            year+=1

            if userin.lower()=='q':
                print(f"FINAL {year}:\tpeople: {people}\ttechnology progress: {tech}\t\tyour karma: {karma}")
                print("I hope you had fun, and have a good day")
                exit(0)

play()

if __name__ == 'main':
    play()