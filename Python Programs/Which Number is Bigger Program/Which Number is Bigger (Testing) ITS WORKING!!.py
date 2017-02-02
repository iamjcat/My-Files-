import time 
import random
import sys

firstname = raw_input("What's your name?\n") #Asks the user's name
print ("Well hello " + firstname) #Greets the user 
time.sleep(0.5) 
print ("Loading...") #pretending to load the game 
time.sleep(2) 
print ("Starting Game")
time.sleep(1)
correctanswer = 0
incorrectanswer = 0
Useranswer = 0

print ("Level One") #Level 1 Section 

for repeat in range(4):

    Lvl1No1 = random.randint(0,10) #Variables that generate 
    Lvl1No2 = random.randint(0,10) #random numbers
    
    
    while (Useranswer != Lvl1No1 and Useranswer != Lvl1No2):
        Useranswer = raw_input("Which is bigger? " + str(Lvl1No1) + " or " + str(Lvl1No2)+"\n")  #Checks if input is a number 
        try:                                                                                     #And also asks the user which number is bigger
            int(Useranswer)     
        except ValueError:
            print ("ERROR! Input is not a number")
            Useranswer = 0
        Useranswer = int(Useranswer)
             
    if (Lvl1No1 > Lvl1No2): #Checks if number input is correct 
        correctanswer = Lvl1No1
    else:
        correctanswer = Lvl1No2
    if (Useranswer == correctanswer):
        print("Correct")
    else:
        print ("Nice try its a wrong number")
        incorrectanswer = incorrectanswer + 1
        if (incorrectanswer == 3):
            print("Three Incorrect Answers You Lose!")
            time.sleep(1.5)
            sys.exit()

#same features from below but at different values 

print ("Level Two")

for repeat in range(6):

    Lvl2No1 = random.randint(10,100) 
    Lvl2No2 = random.randint(10,100)


    while (Useranswer != Lvl2No1 and Useranswer != Lvl2No2):
        Useranswer = raw_input("Which is bigger? " + str(Lvl2No1) + " or " + str(Lvl2No2)+"\n")
        try:
            int(Useranswer)
        except ValueError:
            print ("ERROR! Input is not a number")
            Useranswer = 0
        Useranswer = int(Useranswer)

    if (Lvl2No1 > Lvl2No2):
        correctanswer = Lvl2No1
    else:
        correctanswer = Lvl2No2

    if (Useranswer == correctanswer):
        print("Correct")
    else:
        print ("Nice try its a wrong number")
        incorrectanswer = incorrectanswer + 1
        if (incorrectanswer == 3):
            print("Three Incorrect Answers You Lose!")
            time.sleep(1.5)
            sys.exit()

print ("Level Three")

for repeat in range(8):

    Lvl3No1 = random.randint(100,1000) 
    Lvl3No2 = random.randint(100,1000)


    while (Useranswer != Lvl3No1 and Useranswer != Lvl3No2):
        Useranswer = raw_input("Which is bigger? " + str(Lvl3No1) + " or " + str(Lvl3No2)+"\n")
        try:
            int(Useranswer)
        except ValueError:
            print ("ERROR! Input is not a number")
            Useranswer = 0
        Useranswer = int(Useranswer)

    if (Lvl3No1 > Lvl3No2):
        correctanswer = Lvl3No1
    else:
        correctanswer = Lvl3No2

    if (Useranswer == correctanswer):
        print("Correct")
    else:
        print ("Nice try its a wrong number")
        incorrectanswer = incorrectanswer + 1
        if (incorrectanswer == 3):
            print("Three Incorrect Answers You Lose!")
            time.sleep(1.5)
            sys.exit()

#Bonusanswer = raw_input("Good job :), So what would you like a potato or skooma?")  

         

print("Well done :)")

time.sleep(5)
sys.exit()

    
