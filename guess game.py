from random import randint
secret_num=randint(1,10)
count=0
guess=0
while guess!=secret_num and count <=4:
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