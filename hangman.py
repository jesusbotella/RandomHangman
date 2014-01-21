#!/usr/bin/python
# -*- coding: utf-8 -*-
from game import Game

print "-- Welcome to Random Hangman --\n"
try:
    playersnum=int(raw_input("How many players are going to play? (At least one): "))
except ValueError:
    print "That wasn't a number!"

playerList=[]

for player in range(1,playersnum+1):
    name=raw_input("What's player "+str(player)+" name? ")
    while(name==""):
        print "Please insert one name!"
        name=raw_input("What's player "+str(player)+" name? ")
    playerList.append({"id":player,"name":name})

game=Game(playerList)
game.run()
