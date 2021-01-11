# This is a random agent picker for the popular game, 
# Valorant. I created this script after my friends and I 
# were so indecisive about who to play which match. 
# Created by David Dominguez, worked on 1/11/2021

# We import random module so we can use the random choice function with lists.
import random
# Our beginning list of agents
valorantAgents = ["Brimstone", "Viper", "Omen", "Killjoy", "Sova", "Cypher",
    "Sage", "Phoenix", "Jett", "Reyna", "Raze", "Breach", "Skye", "Yoru"]

print("These are the potential agents you could play:")

# I want to enumerate the agents through the list and just loop it so we can callback later 
for index, agent in enumerate(valorantAgents, start=1):
    print(index, agent)
print("The agent you should play today is:", random.choice(valorantAgents))