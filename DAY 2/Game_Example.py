score = 0

def game(key):
    try:
        if key == 's':
            game_start()
        elif key == 'q':
            quit()
        else:
            key = input("Please Press the valid key(press s to start or q to quit):")
            game(key)
    except ValueError:
        key = input("Please press the valid key(press s to start or q to quit):")
        game(key)

def game_start():
    print("Starting your game...")

    while True:
        try:
            key = int(input("Press 1 to Jump or 0 to quit this game:"))
            if key == 1:
                print("You Jumped")
                global score
                score = score + 1
                print(f"Your Score:{score}")
            elif key == 0:
                print("Thanks for playing this game!")
                quit()
                break

        except ValueError:
            print("Please Press the valid key!")
            game_start()

def quit():
    print(f"You quit the game! and your final score is:{score}")



key = input("Press s to start and q to quit this game:")
game(key)