"""
#its like binary search
Guess a number (18).
give instruction to guess the number.
if guess higher= Its lower than input
if guess lower+ Its higher than Input
total number of guess allowed= 9
print no. of guess left.
if no of guess finised= print game over
if guessed correctly= contratulation you won
print no. of guesses took to win the game.
"""
# correct ansewer is 18
i = 1 # i is number of guesses
print(" Try your luck by guessing a correct number and  win an Iphone 15 pro max. You have 9 attempts to win.")

while (i<10):
    g = int((input(" Guess a number:\n"))) #g is user input/guessed number

    if g>18:
        print("Try again with smaller number")
    elif g<18:
        print("Try again with greater number")
    else:
        print("congratulation! You won an iphone 15 pro max")
        print("No. of attempts taken to win: ", i)
        break

    print("Remaining no. of attempts: ",9-i)
    i = i + 1


if(i>9):
    print("Game over!")
    print("Better luck next time.")
