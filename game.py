import random

# Initialize scores and valid moves
choices = ['stone', 'paper', 'scissors']
scores = {"player": 0, "computer": 0, "tie": 0}

def winner(user_choice, comp_choice):
    """
    Logic to decide the winner and update the scores dictionary.
    """
    if user_choice == comp_choice:
        scores["tie"] += 1
        return f"Both chose {user_choice}. It is a tie!"
    
    # Winning conditions for the player
    if (user_choice == 'stone' and comp_choice == 'scissors') or \
       (user_choice == 'paper' and comp_choice == 'stone') or \
       (user_choice == 'scissors' and comp_choice == 'paper'):
        scores["player"] += 1
        return f"Your {user_choice} beats {comp_choice}. You won!"
    else:
    # If it's not a tie and the player didn't win, the computer wins
        scores["computer"] += 1
        return f"The computer's {comp_choice} beats your {user_choice}. You lost!"

def main():
    while True:
        print('\n--- Stone Paper Scissors Game ---')
        print('1. Play Game')
        print('2. Show Score')
        print('3. Reset Score')
        print('4. Exit')

        user_selection = input("Choose Option (1-4): ").strip()

        if user_selection == '1':
            user_move = input("Enter stone, paper, or scissors: ").lower().strip()
            
            if user_move not in choices:
                print("Invalid input. Please type stone, paper, or scissors.")
                continue
            
            comp_move = random.choice(choices)
            print("\n--- Result ---")
            print(winner(user_move, comp_move))

        elif user_selection == '2':
            print("\n--- Current Scoreboard ---")
            print(f"Player Wins:   {scores['player']}")
            print(f"Computer Wins: {scores['computer']}")
            print(f"Total Ties:    {scores['tie']}")

        elif user_selection == '3':
            scores["player"] = 0
            scores["computer"] = 0
            scores["tie"] = 0
            print("\nScores have been reset.")

        elif user_selection == '4':
            print("\nFinal Score:")
            print(f"You: {scores['player']} | Computer: {scores['computer']}")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
