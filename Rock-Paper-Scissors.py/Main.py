import random
computerWins = 0
humanWins=0
ties = 0 
def rules(Human,Computer):
    global humanWins, computerWins, ties
    if (Human == "Rock" and Computer=="Scissors") or (Human=="Paper"and Computer =="Rock")or (Human == "Scissors" and Computer=="Paper"):
        humanWins +=1
        return print("<== You win! ==>")
    elif (Computer == "Rock" and Human=="Scissors") or (Computer=="Paper"and Human =="Rock")or (Computer == "Scissors" and Human=="Paper"):
        computerWins +=1
        return print("<== Computer wins! ==>")
    elif (Computer == Human):
        ties+=1
        return print("<== It's a tie! ==>")                                                   
def computerrand():
    computer = int (random.randrange(1,3))
    if computer == 1:
        computertext = "Rock"
    elif computer == 2:
        computertext = "Paper"
    elif computer == 3:
        computertext = "Scissors"
    return computertext
print ("\n\nWinning rules of the game ROCK PAPER SCISSORS are:\nRock vs Paper -> Paper wins\nRock vs Scissors -> Rock wins\nPaper vs Scissors -> Scissors wins")
Keeplayingbool= True
while Keeplayingbool== True:
    print("\nEnter your choice\n1 - Rock\n2 - Paper\n3 - Scissors")
    userinput= int(input("\nEnter your choice: "))
    if userinput == 1:
        text = "Rock"
    elif userinput == 2:
        text = "Paper"
    elif userinput == 3:
        text = "Scissors"
    computerchoice= computerrand()
    print ("User Choice is: {}".format(text))
    print("Now it's Computer's Turn...\nComputer choice is: {}".format(computerchoice))

    print ("{} vs {}".format(text,computerchoice))
    rules(text,computerchoice)
    playAagin = input ("\nDo you want to play again? (Y/N): ").lower()
    while playAagin.isalpha() == False:
        playAagin = input ("Input must be Y / N only: ").lower()

    if playAagin =="n":
        Keeplayingbool= False
    elif playAagin == "y":
        Keeplayingbool= True

print("\nThanks for playing!")
print("\nTotal Game played: {}\nYou won: {} times\nComputer won: {} times\nThe was {} tie Games".format(computerWins+ties+humanWins,humanWins,computerWins,ties))




    




