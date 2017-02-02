#Vending Machine Program
import time
mars = 3
snickers = 3   #Amount of chocolate bars 
kitkat = 3
verify = "y" 
Useranswer = ["mars","snickers","kitkat"]
ans = 'y'

print("Hello") #greets user 

while (ans == 'y' or 'n'):#A while loop
    print("What chocolate bar do you want?")#Asks user what chocolate bar
    Useranswer = raw_input("I have the following: mars, snickers and kitkat""\n")#lists the following  
                                                                                 #chocolate bars available
    if (Useranswer == "mars"):#if user typed "mars" do this 
        if (mars == 0): #if "mars" bar ran out, it'll the apologise user  
            print("Sorry ran out of mars")
            time.sleep(1.5)#wait just to give the impression that computer is thinking
        if (mars > 0): #if the chocolate bars are not empty, then it'll ask and give the user one
            verify = raw_input("Is this what you want? y/n""\n")
            if (verify != "y"):
                print("Ok what was it again?")
                time.sleep(1)
            elif (verify == "y"):
                print("Here you go :)")
                mars = mars - 1 #decrease mars bar value by 1 everytime the user wants the "mars" bar 
                time.sleep(1.5)
                print("*Gives Chocolate Bar*")
                ans = raw_input("Would you like something else? y/n""\n")
                if (ans == 'n'): #if the user says "no" the code is started again, but the amount of bars  
                    print("Alright then") #is not affected
                    time.sleep(0.75)
                    print("Enjoy :)")
                    time.sleep(3)
                    print("Hello")
                    time.sleep(1)

    if (Useranswer == "snickers"):#if user typed "snickers" do this 
        if (snickers == 0): #if "snickers" bar ran out, it'll apologise the user 
            print("Sorry ran out of snickers")
            time.sleep(1.5)
        if (snickers > 0): #if the chocolate bars are not empty, then it'll ask and give the user one
            verify = raw_input("Is this what you want? y/n \n")
            if (verify != "y"):
                print("Ok what was it again?")
                time.sleep(1) 
            elif (verify == "y"):
                print("Here you go :)")
                snickers = snickers - 1 #decrease snickers bar value by 1 everytime the user wants the "snickers" bar 
                time.sleep(1.5)
                print("*Gives Chocolate Bar*")
                ans = raw_input("Would you like something else? y/n""\n")
                if (ans == 'n'): #if the user says "no" the code is started again, but the amount of bars 
                    print("Alright then") #is not affected
                    time.sleep(0.75)
                    print("Enjoy :)")
                    time.sleep(3)
                    print("Hello")
                    time.sleep(1)

    if (Useranswer == "kitkat"):#if user typed "kitkat" do this 
        if (kitkat == 0): #if "kitkat" bars ran out, it'll apologise the user 
            print("Sorry ran out of kitkat")
            time.sleep(1.5) 
        if (kitkat > 0): #if the chocolate bars are not empty, then it'll ask and give the user one 
            verify = raw_input("Is this what you want? y/n""\n")
            if (verify != "y"):
                print("Ok what was it again?")
            elif (verify == "y"):
                print("Here you go :)")
                kitkat = kitkat - 1 #decrease snickers bar value by 1 everytime the user wants the "kitkat" bar
                time.sleep(1.5)
                print("*Gives Chocolate Bar*")
                ans = raw_input("Would you like something else? y/n""\n")
                if (ans == 'n'): #if the user says "no" the code is started again, but the amount of bars 
                    print("Alright then") #is not affected
                    time.sleep(0.75)
                    print("Enjoy :)") 
                    time.sleep(3)
                    print("Hello")
                    time.sleep(1)

    

        
        
        
    



