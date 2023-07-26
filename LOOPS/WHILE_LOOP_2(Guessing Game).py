import random
n = 20
to_be_guessed = int (n*random.random()) + 1
guess = 0
#print(to_be_guessed)
while guess != to_be_guessed: 
    guess = int(input('New number: '))
    if guess > 0:
        if guess > to_be_guessed:
            print('Number too large')
        elif guess < to_be_guessed: 
            print('Number too small')   
    else:
        print('Sorry that youre giving up!')
        break
else:
    print('Congratulation. You made it!')