#Samson Haile
#This program is a game in which the player is pitted against the computer. The computer randomly generates a number (binary or decimal) and the player must
#convert the number to the opposite base.
#First to 10 wins.
import random

#Global constant for how many points needed to win
winningscore = 10

# variable used to turn the game on and off
GameOn = True

#Prints the intro to the game, and contains the function call to all the necessary functions.
def main():
    #Intro to the game, explaining the rules and such.
    print("Welcome to the Conversion Game! Think you have what it takes to beat the Computer? all you have is convert the number the computer displays into binary or decimal, depending on the number it displays.")
    print("Both players start at 0 points. First to 10 points wins! Good Luck.")

    Maingamecode()
    
    
    

    

 
# Holds a majority of the games code. Holds the random number generator, score calculator and score counter.  
def Maingamecode():
    compscore = 0
    userscore = 0
    
    #Allowes me to edit the global variable "GameOn"
    global GameOn
    
    while GameOn == True:

        #Variable that is used to pick which  in which base the number is generated.
        DiceRoll = random.randint(1,6)                               

        #Generates a random number in base 10.
        CompNumDec = random.randint(0,100)                           

        #Generates a random number in base 2, using the built in bin() function. the "[2:]" at the end is so the string does not print the "Ob" prefix
        #Associated with binary numbers
        CompNumBi = bin(random.randint(0,100))[2:]                      

        #Checks to see if the nnumber generated is a binary number
        if DiceRoll < 4:                                           
           print("Here is a binary number. Can you convert it to decimal?")
           print(CompNumBi)
        #Checks to see if the number generated is a decimal number
        if DiceRoll > 3:
            print("Here is a decimal number. Can you convert it to binary?")
            print(CompNumDec)
        UserNum =(input("Please input:"))

        #Checks to see if the user got the conversion right using the built in bin() and int() functions, which converts decimal to binary
        #and vice versa, respectively. 
        # It then adds a point to their score if true.                  
        if UserNum == bin(CompNumDec)[2:] or int(UserNum) == int(CompNumBi,2):
            print("You Got It!")

            #Updates User's score due to a winning situation
            userscore = userscore + 1 

            #Prints current scores for both the player and computer.
            print("Current Score:")
            print("Your Score:",userscore)
            print("Computer's Score:",compscore)
            
        #Checks to see if the player got the conversion to decimal wrong, using the built in int() function, which converts binary to decimal.
        #It then adds a point to the computer's score if true.
        elif int(UserNum) != int(CompNumBi,2) and DiceRoll < 4:

            #prints correct asnwer
            print("Sorry, but that was incorrect. The correct answer is",int(CompNumBi,2))
            
            #Updates Computer's score due to a losing situation
            compscore = compscore + 1
            

            #Prints current scores for both the player and computer.
            print("Current Score:")
            print("Your Score:",userscore)
            print("Computer's Score:",compscore)
            
        #Checks to see if the player got the conversion to binary wrong, using the built in bin() function, which converts decimal to binary.
        #It then adds a point to the computers score if true.
        elif UserNum != bin(CompNumDec)[2:] and DiceRoll > 3:

            #prints correct answer
            print("Sorry, but that was incorrect. The correct answer is", bin(CompNumDec)[2:])

            #Updates Computer's score due to a losing situation
            compscore = compscore + 1                                                                

            #Prints current scores for both the player and computer.
            print("Current Score:")
            print("Your Score:",userscore)
            print("Computer's Score:",compscore)
            
    
#This section checks to end the game, and to see who has won.

        #Checks to see if the Computer has won.
        if compscore == winningscore:                                                                
                print("Sorry, but the Computer has won.")
                print("Re-run to try your luck against the Computer once more.")
                
                #Ends the game
                GameOn = False                                                                       

        #Checks to see if the Player has won.          
        elif userscore == winningscore:                                                              
                print("Yeah, You Win!")
                print("Re-run to play again!")
                
                #Ends the game
                GameOn = False                                                                       

      
       
main()

