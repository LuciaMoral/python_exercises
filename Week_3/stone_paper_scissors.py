import random

options = (["stone", "paper", "scissors"])
while True:
    player = input("Type option: \n stone, paper, scissors \n")
    computer_input = random.choice(options)
    print(f"\n computer chose {computer_input}")

    if player == "paper" and computer_input == "stone":
        print("Congrats! you win: paper wins over stone!")
    elif player == "stone" and computer_input == "scissors":
        print("Congrats! you win: stone destroys scissors")
    elif player == "scissors" and computer_input == "paper":
        print("Congrats! you win: scissors cut paper!")
    elif  computer_input == "paper" and player == "stone":
        print("Sorry, you lost! paper wins over stone!")
    elif computer_input == "stone" and player == "scissors":
        print("Sorry, you lost! stone destroys scissors")
    elif computer_input == "scissors" and player == "paper":
        print("Sorry, you lost! scissors cut paper")
    elif player == computer_input:
        print("no one wins!")
