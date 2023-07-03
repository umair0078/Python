for numbers in range(2,21):
    with open(f"Tables/The_Multiplication_Table_of_{numbers}.txt", "w") as file:
        for number in range(1,11):
            file.write(f"{numbers}*{number} = {numbers*number}")
        