# TODO Create an empty list to maintain the player names

players = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
choose = "y"

while choose.lower() == "y":
    choose = input("Would you like to add a new player to the team (Y/N)")
    if choose.lower() == "y":
        new_player = input("Who is your new player?")
        players.append(new_player)


# TODO print the number of players on the team

print ("Your team has a {} player".format(len(players)))

# TODO Print the player number and the player name

for x in range(len(players)):
    print (x+1,". ",players[x])
    
goalkeeper = input("Who will be the goalkeeper? ")
print ("The golakeeper will be {}".format(goalkeeper))

       



# The player number should start at the number one


# TODO Select a goalkeeper from the above roster


# TODO Print the goal keeper's name
# Remember that lists use a zero based index

