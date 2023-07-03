def game():
    score = 600
    return score

score = game()

with open("highscore.txt", "r") as openHighScore:
    readHighScore = openHighScore.read()

if readHighScore == '':
    with open("highscore.txt", "w") as openHighScore:
        openHighScore.write(str(score))

elif int(readHighScore) < score:
    with open("highscore.txt", "w") as openhighScore:
        openHighScore.write(str(score))

