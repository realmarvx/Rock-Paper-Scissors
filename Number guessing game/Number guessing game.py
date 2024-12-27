import random

print ("               Number Guessing Game                ")
lowerBound = 0
upperBound= 0
minimum = 0
randomNumber = 0
userguess = 0
lowerBound= int(input("Input Lower Bound:"))
upperBound = int(input("Input Upper Bound:"))
minimum= int(input("Input How Many Tries:"))

randomNumber = int (random.randrange(lowerBound,upperBound))

print ("                Start Guessing              ")
userguess =int(input("Guess a Number:"))

trycount=1
while userguess != randomNumber:
    userguess = int(userguess)
    if trycount == minimum:
        print ("Out of tries! The number was {}.\nBetter Luck Next Time!".format(randomNumber))
        break
       

    elif userguess > randomNumber:
        userguess = int(input("Try Again! You guessed too high\nGuess a Number:"))
        trycount +=1
        
    elif userguess< randomNumber:
        userguess= int (input("Try Again! You guessed too small\nGuess a Number:"))
        trycount +=1

    
if userguess == randomNumber and trycount <= minimum:
      print("Congratulations! \nIt took you {} tries!".format(trycount))
    