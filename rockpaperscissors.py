import random
import sys


def main():
    choices = ["rock", "paper", "scissors"]
    print("Let's play a game of rock paper scissors!")

    while True:
        user_choice = input("What do you choose? Type out your choice and your choice only without abbreviating. Type q to quit. \n").strip().lower()

        if user_choice == "q" or user_choice == "quit":
            break

        elif user_choice not in choices:
            print("Please enter a valid choice.")
            continue

        else:
            computer_choice = random.choice(choices)

            if computer_choice == user_choice:
                message = f"We tied! I chose {computer_choice}. Do you want to play again? Type q to quit."
            elif result(user_choice, computer_choice):
                message = f"You win! I chose {computer_choice}. Do you want to play again? Type q to quit."
            else:
                message = f"You lose! I chose {computer_choice}. Do you want to play again? Type q to quit."

            want = input(message).strip().lower()
            if want == "q" or want == "quit":
                break
            continue


    print("Exiting...")
    sys.exit()

def result(s, t):
    win_results = {"rock":"scissors", "scissors":"paper", "paper":"rock"}
    return win_results[s] == t


if __name__ == "__main__":
    main()
