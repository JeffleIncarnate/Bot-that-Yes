# Imports
import time
import random

# Welcome
print("Welcome to my amazing bot that decides yes or no: ")
time.sleep(1)
input("Press any button to continue: ")

# Lists
b = "Why"
c = "No"
d = "Yes"
e = "IDK"
f = "I don't know"
g = "JK LOL"
h = "Haha"

i = [b, c, d, e, f, h]


# Function
def j():
    n = 1
    while n < 10000000000000000000000000000000000000:
        a = input("Ask a question: ")
        if n < 10000000000000000000000000000000000000:
            if a == "":
                print("Go away short idiot")
                while True:
                    if n == 1:
                        break
                    elif n == 2:
                        break
                    else:
                        break
            else:
                print("The answer to your question: " + '"' + a + '"')
                print(random.choice(i))
                n = n + 1
                print("")
        else:
            print("Go away short idiot")


# Call the function
j()
