"""
docstring test - main() will serve as the body of the game.
"""
def main():

    # === INITIALISATION =======================================================================
    # Initialising game variables
    playing = True
    isImmobilised = True
    endingNumber = -1
    actionListPhaseOne = ["look around", "quit"]

    # Game intro
    print("Once upon a time, there was a humble ")
    
    # Gets the player's name
    playerName = input("Please enter thy name: ")
    print("Hello " + playerName + "!")

    # Gets the player's age
    playerAge = input("Please enter thy age: ")
    while not playerAge.isdigit():
        print("That's not an age")
        playerAge = input("Please enter thy age: ")
    playerAge = int(playerAge)
    # ==========================================================================================

    # === GAMELOOP =============================================================================
    while (playing):
        # actionLists will be printed at the start of each 'turn' once populated with the immediate  
        # options available to a player. PhaseOne denotes the start of a game session.
        print("What do you do?")
        print(actionListPhaseOne)
        action = input("Please enter your action: ").lower()
        print(">" + action)
   
         if action == "look around" and isImmobilised is True:
            #Not sure if this will even work - I want to add options as the game runs, certain actions 
            #unlock other actions, and disable no longer valid ones.
            
            actionListPhaseOne.append("free yourself")
            print("You try to LOOK AROUND. Sadly, your head is stuck!")  

        if action == "quit":
            playing = False
            endingNumber = 0
    # ==========================================================================================

    # === ENDINGS ==============================================================================
    if endingNumber == 0:
        print("You were eaten by a grue.")
        print("Thanks for playing!")
    else:
        print("Wait what the fuck")
    # ==========================================================================================

# Main bootstrap method that will kick off the game.
if __name__ == "__main__":
    main()