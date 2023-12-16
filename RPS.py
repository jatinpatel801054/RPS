import random

actions = ['rock', 'paper', 'scissors']

while True:
    x = input('Enter your choice (rock, paper or scissors): ')

    y = random.choice(actions)

    print(f"Your choice {x}, computer choice {y}\n")

    if x == y:
        print(f"Both players selected {x}. It's a tie!")
    elif x == "rock":
        if y == "scissors":
            print("You win! because Rock smashes scissors.")
        else:
            print("You lose :( Paper covers rock!")
    elif x == "paper":
        if y == "rock":
            print("You win! because Paper covers rock.")
        else:
            print("You lose :( Scissors cuts paper!")
    elif x == "scissors":
        if y == "paper":
            print("You win! because Scissors cuts paper.")
        else:
            print("You lose :( Rock smashes scissors!")
            
    play_again = input('Play again? (y/n)')
    if (play_again.lower() == 'n'):
        break