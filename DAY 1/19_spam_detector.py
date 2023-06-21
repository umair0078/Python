text = input("Enter Your Text\n")

if "free" in text:
    spam = True
elif "buy now" in text:
    spam = True
elif "make money" in text:
    spam = True
else:
    spam = False

if spam:
    print("This text is a spam")
else:
    print("This text is not a spam")
