##This is a simple guess game by using 100 random numbers
from random import randint 
secret_num=randint(1,100) ##The random answer is stored in "secret_num" variable
count=0 ##used to keep track of number of turns user takes
guess=0 ##initilaizedg guess to compare with secret_num variable
while guess!=secret_num and count <=4: ##while condition for user to enter guess 5 times while the guess is not equal to the answer
    guess=eval(input("Enter your guess:"))
    count=count+1
    if guess<secret_num:
        print("Higher!",5-count,'guesses left') 
    elif guess>secret_num:
        print("Lower!",5-count,'guesses left')
    else:
        print('You got it')
if count==5 and guess !=secret_num:
    print("You lost!,The number was: ",secret_num)
