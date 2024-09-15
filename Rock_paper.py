import random


choices = ["sten", "sax", "påse"]


def get_player_choice():

    player_choice = input("CHoose sten, sax, påse: ").lower()

    #check valid input

    while player_choice not in choices:
        print("Invlaid choice. Please choose agian")
        player_choice = input("CHoose sten, sax, påse: ").lower()

    return player_choice

def  get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(player_choice, computer_choice):
    if(player_choice == computer_choice):
        return "draw"
    
    #Rules for player win
    if (player_choice == "sten" and computer_choice == "sax") or (player_choice == "sax" and computer_choice == "påse") or (player_choice == "påse" and computer_choice == "sten"):
        return "Player"

    return "computer"


def display_result(player_choice, computer_choice, result):
    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if result == "draw":
        print("It's a draw!")
    elif result == "player":
        print("You win!")
    else:
        print("Computer wins!")


def play_game():
    while True:
        # Get the player's and computer's choices
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        # Determine the winner
        result = determine_winner(player_choice, computer_choice)
        
        # Display the result
        display_result(player_choice, computer_choice, result)
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break


play_game()