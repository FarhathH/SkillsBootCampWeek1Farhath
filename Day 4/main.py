import random
#19th Oct 2023
#Recap
#Integer
# day_num = 4
# #String
# tutor = "Matt"
#
# #Incrementation
# day_num = day_num + 1
# #short hand is day_num+=1
# print(day_num)
#
# #using abs() function
# day_num*=6.5
# day_num = abs(day_num)
# print(day_num)
#print(len("Farhath"))
#Make a variable presenting the user password
#If the attempt is correct, print "Logged in"
#othetrwise, print "Password incorrect"

#Being cheeky and attemping a loop with a password checking exercise
# truePassword = "Pizza"
# #Eliminating white spaces
# truePassword = truePassword.strip()
# #Asking input
# userInput = input("What's the password \n")


#checking the conditions are met, otherwise the loop continues
#len() is used to check the length of a value
# while userInput != truePassword:
#     if userInput == truePassword:
#         print("Password correct.")
#     elif len(userInput) > len(truePassword):
#         print("Too long.")
#         userInput = input("What's the password \n")
#     elif len(userInput) < len(truePassword):
#         print ("Too short.")
#         userInput = input("What's the password \n")
#     else:
#         print("Incorrect")
#         userInput = input("What's the password \n")

# my_var = ["Matt", "Ploy", "Fatme", "Mason", "Jess", "Tom", "Jose"]
#
# #print Jose
# print(my_var[6])
#
# #print Fatme
# print(my_var[2])
#
# #print Tom
# print(my_var[5])

# #replaced a value with a new value in the list before printing.
# my_var[6] = "Monke"
# print(my_var[6])
# #used len() function to print out value in list
# print(my_var[len(my_var)-4])
# #
# my_var[6] += "y boy"
# print(my_var[6])
# my_var[0] = "Player " + my_var[0]
# print(my_var[0])

#my_num_list = [80, 43, 65, 73, 12, 9, 8, 5]
#write code to multiply all the elements by 2

# #used shorthand operators to reference an index and multipling them
# my_num_list[0]*=2
# my_num_list[1]*=2
# my_num_list[2]*=2
# print(my_num_list)
#
# #attempted a 'for' loop
# for i in my_num_list:
#     i+=2 #incremented each value
#     print(i)

#using the list from earlier, made a for loop to iterate the values in the array and increment them
# for i in range(0, len(my_num_list)):
#     my_num_list[i] *= 2
# print(my_num_list)

#practicing the use of for loops to imcrement values in an array.
# num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# for i in range(0, len(num)):
#     num[i] *= 5
#     print(num[i])

#using for loop to check that multiples of 3 and 5 print 'fizz' and 'buzz' or 'fizzbuzz'
# for i in range(1, 151):
#     if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#         print("fizzbuzzpop")
#     elif i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0 and i % 7 == 0:
#         print("fizzpop")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     elif i % 7 == 0:
#         print("pop")
#     else:
#         print(i)

#For loop practice
# run = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# for i in range(0, len(run)):
#     if i % 3 == 0 and i % 2 == 0:
#         print("coconut")
#     elif i % 3 == 0:
#         print("coco")
#     elif i % 2 == 0:
#         print("nut")
#     else:
#         print(run[i])

# for i in range(3, 30):
#     if i % 3 == 0 and i % 5 == 0:
#         print("coconut")
#     elif i % 3 == 0:
#         print("coco")
#     elif i % 5 == 0:
#         print("nut")
#     else:
#         print(i)

#It was a mess, but I managed to do something.
right_num = random.randint(1,10)

for i in range(0,3):
    guess = int(input("Guess a number between 1 and 10 \n"))
    if guess > right_num:
        print("Too high\n")
    elif guess < right_num:
        print("Too low")
    elif guess == right_num:
        print("Correct")
        break

if guess != right_num:
    print(":P Too bad")





