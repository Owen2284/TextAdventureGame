def main():
    """
    docstring test - main() will serve as the body of the game.
    """
    # === INITIALISATION =======================================================================
    print("lalalal backstory ur a skellington who wants out of this hell ayy lmao")
    
    playerName = input("Please enter thy name: ")
    print("Hello " + playerName + "!")

    playing = True
    isImmobilised = True
    endingNumber = -1

    
    playerAge = input("Please enter thy age: ")
    while not playerAge.isdigit():
        print("That's not an age")
        playerAge = input("Please enter thy age: ")
    playerAge = int(playerAge)
    

    
    # ==========================================================================================

    
    # === GAMELOOP =============================================================================
    while (playing):
        print("What do you do?")
        actionListPhaseOne = ["look around", "quit"]
        print(actionListPhaseOne)
        action = input("Please enter your action: ").lower()
        print(">" + action)
   
    # actionLists will be printed at the start of each 'turn' once populated with the immediate  
    # options available to a player. PhaseOne denotes the start of a game session.
   
        if action == "quit":
            playing = False
            endingNumber = 0

        if action == "look around" and isImmobilised is True:
            playing = True
            actionListPhaseOne.insert(1, "free yourself")
            print("You try to LOOK AROUND. Sadly, your head is stuck!")

    # ==========================================================================================

    
    # === ENDINGS ==============================================================================
    if endingNumber == 0:
        print("You were eaten by a grue.")
    else:
        print("Wait what the fuck")

    if endingNumber >= 0:
        print("Thanks for playing!")
    # ==========================================================================================

# Main bootstrap method that will kick off the game.
if __name__ == "__main__":
    main()