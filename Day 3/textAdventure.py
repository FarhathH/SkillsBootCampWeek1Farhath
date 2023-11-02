#code scroll function from: https://replit.com/talk/learn/How-to-make-a-basic-TextStory-Game-in-Python/77845

#headers for allowing scrolling text and speed
import sys
import time

#defined function that responsible for allowing the printed text to scroll
def scrollTxt(text):
   for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.05)

max_attempts = 3
current_attempt = 0

for current_attempt in range(0, max_attempts):
    current_attempt+=1
    #series of statements to guide through decision making for user
    scrollTxt("You're walking in a forest. \n You're hungry and lost and see a figure in the distance. \n Is that?\n ")
    choice_one = input("Pick A for wendigo or B for skin walker")
    if choice_one == "A" or choice_one == "a":
        scrollTxt("The wendigo looks up and before it notices you and dashes towards you. Do you?\n")
        choice_two = input("Pick A to run or B to stay still")
        if choice_two == "A" or choice_two == "a":
            scrollTxt("You make a mad dash but the wendigo was too fast for you. Too bad")
        elif choice_two == "B" or choice_two == "b":
            scrollTxt("You panick and freeze, but by some miracle the wendigo \n get burned by Pyro. They look at the "
                      "wendigo burning up to a crisp \n They turn to you and point their flamethrower. Burn, baby burn.")
    elif choice_one == "B" or choice_one == "b":
        scrollTxt("The skin walker morphs into a cross-eyed deer and before it notices you and slowly \n walks towards you. Do you? \n")
        choice_two = input("Pick A throw a rock at them to or B to power walk and pretend that you didn't see them")
        if choice_two == "A" or choice_two == "a":
            scrollTxt("You grab a rock and throw it towards the deer. They morph into their true form before \n devouring you. Not the sharpest tool in the shed, are ya?")
        elif choice_two == "B" or choice_two == "b":
            scrollTxt("You hope that this works. You power walk, looking over your shoulder from time to time. \n Before you know it, you lost the skin walker or they lost interest in you. \n You hear a crack on your ribs after something falls on you")


print("Thanks for playing")
