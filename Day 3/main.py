import random

# 18th October 2023
# assigning a value and printing an increased amount and default
#my_num = 5
#print(my_num + 3)
#print(my_num)
#print
# Another attempt but with abbreviated incrementation
#num = 5
#num = num + 3
#num+=3
#print(num)


#variable for health with a value of 100
#decrease is by 10 and print out the new value
#health_bar = 100
#health_bar = health_bar - 10
#health_bar-=10
#print(f"You've been stabbed and now have {health_bar} hit points remaining")

#create a variable called my_num_2, set it value between 1 and 100
#write code to make the variable equal to itself multiplied by two
#my_num_2 = 56
#my_num_2 = my_num_2 * 2
#my_num_2*=2
#print(my_num_2)

#mini exercise to apply increment/decrement
#fuel = 0
#fuel -=4
#print(fuel)

#mini exercise to apply increment/decrement again
#used int function to convert input function into accepting integer data type
#kansaiDrifto = int(input("Pick a number between between 1 and 100"))
#kansaiDrifto*=5
#print(f"You now have {kansaiDrifto} yen.")

#Trying out conditional operators
#checking if 5 is less than 6
#print(5<6)

#checking if 9 is less than or equal than 4
#print(9<=4)

#checking if 10 is greater than 1
#print(10>1)

#checking if 5 is equal to 6
#print(5==6)

#checking if 6 is not equal to 8
#print(6!=8)

#Intialising variables and checking the condition
#num1 = 5
#num2 = 5
#if num1 == num2:
 #   print("They're the same")
#else:
 #   print("Something's wrong. I can feel it")

#Creating a variable called lockpick_level
#If the level is 60 or above, print "You picked the lock"
#lockpick_level = 45
#if lockpick_level >= 60:
 #   print("You picked the lock")
#else:
 #   print("You couldn't pick the lock.")

#checking conditions with if statements
#num_1 = 5
#num_2 = 10
#if num_1>num_2:
 #   print("Num 1 is bigger")
#elif num_1<num_2:
 #   print("Num 1 is smaller")
#else:
 #   print("They're the same")

#create variables team1score and team2score
#if team1score is higher, print "team1 won"
#if team2score is higher, print "team2 won"
#if they're the same, print "draw"

#declaring variables
#team1score = 3
#team2score = 5
#goalString = ""

#for calculating score difference
#dif = abs(team1score-team2score)

#for output based on the condition
#if dif > 1:
 #   goalString = "goals"
#elif dif < 1:
 #   goalString = "goal"

#conditioned statement with variables applied
#if team1score > team2score:
 #   print(f"team1 won by {dif} {goalString}")
#elif team1score < team2score:
 #   print(f"team2 won by {dif} {goalString}")
#else:
 #   print("Draw")

#Test program
#ploy_score = int(input("Enter a score between 1 and 100"))
#if statements for a grading system
#if ploy_score >= 80:
 #   print("You got an A")
#elif ploy_score >= 70:
 #   print("You got a B")
#elif ploy_score >= 60:
 #   print("You got a C")
#elif ploy_score >= 50:
 #   print ("You got a D")
#elif ploy_score >= 40:
 #   print("You got an E")
#elif ploy_score < 40:
#    print("You got an F")

#prompted user for numeral input
#firstNumber = int(input("Type in a number"))
#secondNumber = int(input("Type in another number"))
#printed the calculation of both variables multipled
#print(f"{firstNumber} multiplied by {secondNumber} equals {firstNumber * secondNumber}")

#Another try with prompting for input and printing the output
#one = int(input("Give us a number"))
#two = int(input("Give us another number"))
#print(f"{one} + {two} = {one + two}")

#Generating random number
#print(random.randint(1, 10))

#randomly generating a coin toss that runs once
#coin_toss = random.randint(1,2)
#if coin_toss == 1:
 #  print("heads")
#elif coin_toss == 2:
 #  print("tails")

#Used a while loop to run the if statements by rolling for a random number
#depending on the outcome, heads or tails get printed and the corresponding variables get increamented
#continues until the loop ends and the final score is printed.
head = 0
tails = 0
for i in range(1, 1000):
     roll = random.randint(1, 100)
     if(roll < 49):
         head+=1
         print("HEADS")
     elif roll >= 50:
         tails+=1
         print("TAILS")
print(f"Heads: {head} Tails: {tails}")



