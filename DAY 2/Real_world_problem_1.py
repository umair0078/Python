# Suppose, a student wants to pass an exam. He requires minumum 33 marks to pass that exam. He will sit in exam again and again until he gets 33 or above marks.
def exam(marks):
    try:
        if marks < 33:
            exam(marks+1)
        else:
            print(f"Congratulations! You are passed with {marks} marks!")
    except:
        print("Please Enter the Valid Marks!")

exam(22)