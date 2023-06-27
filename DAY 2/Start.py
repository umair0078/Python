from Quit import quit
score = 0
def game_start():
    print("Loading Your Game!")
    while True:
        key = int(input("Press 1 to Jump and 0 to Quit this game:"))
        if key == 1:
            print("Jumped")
            global score
            score += 1
            print(f"Your Current Score:{score}")
        elif key == 0:
            quit()
            break
        

        
