import Start
from Quit import quit
def game(key):
    if key == 's':
        Start.game_start()
    elif key == 'q':
        quit()
    else:
        key = input("Please press a valid key(Press s to start and q to quit:)")
        game(key)
        

