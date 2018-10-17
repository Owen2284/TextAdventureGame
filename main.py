def main():
    # === INITIALISATION =======================================================================
    playerName = input("Please enter thy name: ")
    print("Hello " + playerName + "!")

    playing = True
    endingNumber = -1
    
    #playerAge = input("Please enter thy age: ")
    #while not playerAge.isdigit():
    #    print("Fuck off mate")
    #    playerAge = input("Please enter thy age: ")
    #playerAge = int(playerAge)
    # ==========================================================================================

    # === GAMELOOP =============================================================================
    while (playing):
        action = input("Please enter your action: ").lower()
        print(action)

        if action == "quit":
            playing = False
            endingNumber = 0
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