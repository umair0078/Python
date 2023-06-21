# Program to calculate the total runs scored by a batsman in an innings

total_score = 0

while True:
    print("Enter 'out' to stop")
    score = input("Enter the score:")
    

    if score.lower() == "out":
        break

    try:
        score = int(score)
        total_score += score
    except ValueError:
        print("Invalid Input! Please Enter a valid score")



print(f"Total Score: {total_score}")
