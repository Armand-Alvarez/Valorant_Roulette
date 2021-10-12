#!/usr/bin/env python3

# Valorant Roulette
# Author:  Armand Alvarez
# Github: github.com/Armand-Alvarez

# This program generates a random agent to play and selects random guns to use. 

import random
from os import system, name
from sys import exit

AGENTS = {
1: "Brimstone",
2: "Viper",
3: "Omen",
4: "Killjoy",
5: "Cypher",
6: "Sova",
7: "Sage",
8: "Pheonix",
9: "Jett",
10: "Reyna",
11: "Raze",
12: "Breach",
13: "Skye",
14: "Yoru",
15: "Astra",
16: "KAY/O"
}

MAX_AGENTS = len(AGENTS)

GUNS = {
1: "Classic",
2: "Shorty",
3: "Frenzy",
4: "Ghost",
5: "Sheriff",
6: "Stinger",
7: "Spectre",
8: "Bucky",
9: "Judge",
10: "Bulldog",
11: "Guardian",
12: "Phantom",
13: "Vandal",
14: "Marshall",
15: "Operator",
16: "Ares",
17: "Odin",
18: "Knife"
}


COVER_ART = """
╦  ╦┌─┐┬  ┌─┐┬─┐┌─┐┌┐┌┌┬┐  
╚╗╔╝├─┤│  │ │├┬┘├─┤│││ │   
 ╚╝ ┴ ┴┴─┘└─┘┴└─┴ ┴┘└┘ ┴   
╦═╗┌─┐┌┐┌┌┬┐┌─┐┌┬┐         
╠╦╝├─┤│││ │││ ││││         
╩╚═┴ ┴┘└┘─┴┘└─┘┴ ┴         
╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
"""

# Print the splash screen
def printSplashScreen():
	clear()
	print("----------------")
	print(COVER_ART)
	print("\n\n\n")


# Clear the screen
def clear():

	# For windows
	if name == "nt": _ = system("cls")
	
	# For Unix environments
	else: _ = system("clear")


# Print the agents and guns generated so far
def printQueue(agent, guns):

	print("Agent:  " + agent)
	print()
	for x in guns[:-1]: print(GUNS[guns[x]])
	print(GUNS[guns[-1]] + "  <----")


# Get random gun
def generateRandomGun(): return GUNS[random.randint(1, len(GUNS))]


#### MAIN LOGIC
###############

printSplashScreen()

input("Press any key to continue...") 

con = True
while(con):
	clear()
	print("How many agents do you want to generate? (Pick a number betwen 1 - " + str(MAX_AGENTS) + ")")
	numAgents = 0

	# Only allow between 1 and the number of agents that exist, to avoid duplications
	try: numAgents = int(input())
	except ValueError: 
		print("Please input a number.")
		input("Press [ENTER] to continue.")

	else: 
		if numAgents > 0 and numAgents <= MAX_AGENTS: con = False

# Generate the agents
agents = []
for x in (random.sample(range(1, MAX_AGENTS+1), numAgents)): agents.append(AGENTS[x])

guns = [generateRandomGun()]

while(True):
	clear()
	
	print("Agents:\n")
	print('\n'.join(map(str, agents)))

	print('\n-------------------\n')

	print("Guns:\n")

	print('\n'.join(map(str, guns)))
	print('\n')

	if (input("Press [ENTER] to continue, or type 'quit' to exit the program.\n").lower() == "quit"): exit()
	guns.append(generateRandomGun())
		
