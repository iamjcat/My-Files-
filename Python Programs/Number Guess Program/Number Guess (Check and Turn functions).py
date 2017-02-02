# This is a guess the number game.  
import random  

guessesTaken = 0  
guess = 0 
ans = 'y'  

print('Hello! What is your name?') #introduces user  
myName = input()  
 
while ans == 'y': 
        number = random.randint(1, 20) #generates random numbers  
        print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')#Asks the user a clue 

        while (guess != number) and (guessesTaken < 6): #the backbone and the check function 
                print('Take a guess.')  #^limits the number of guesses taken 
                guess = input() 
                try: 
                    guess = int(guess) 
                    guessesTaken = guessesTaken + 1  
                    if (guess < number):  
                        print('Your guess is too low.') 
                    if (guess > number):  
                        print('Your guess is too high.')  
                except ValueError: 
                    print ('ERROR! Input is not a number') 
                    guess = 0 
                guess = int(guess) 
                if (guess == number):  
                    break 
   
        if guess == number: #congratulates the user if the number is right   
            guessesTaken = str(guessesTaken)  
            print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  
  
        if guess != number:#if the user has six wrong number guesses, GAME OVER!  
            number = str(number)  
            print('Nope. The number I was thinking of was ' + number) 
 
 
        ans = input('Would you like another turn? y/n \n') #Asks the user if he/she wants another turn 
        if ans != 'y': 
                print('Goodbye\n') 
        elif ans == 'y': 
                guessesTaken = 0
