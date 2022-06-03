import random

dice = ["R", "P", "S"]


def move_name(move):
    if move == "R":
        return "Rock"
    elif move == "S":
        return "Scissors"
    elif move == "P":
        return "Paper"
    else:
        return False


def move_validity(user_input, computer_input):
    if user_input == "R" or user_input == "S" or user_input == "P":
        move = f"Player ({move_name(user_input)}) : CPU ({move_name(computer_input)})"
        return move
    else:
        return "Invalid Move"


def move_logic(user_input, computer_input):
    if user_input == "R" and computer_input == "S":
        return "Player wins"
    elif user_input == "P" and computer_input == "R":
        return "Player wins"
    elif user_input == "S" and computer_input == "P":
        return "Player wins"
    elif computer_input == "R" and user_input == "S":
        return "Computer wins"
    elif computer_input == "P" and user_input == "R":
        return "Computer wins"
    elif computer_input == "S" and user_input == "P":
        return "Computer wins"
    elif computer_input == user_input:
        return "TIE"
    else:
        return None


def init():
    while True:
        user_input = input('pick an option between "R", "P" or "S" \n').upper()
        computer_input = random.choice(dice)

        move = move_validity(user_input, computer_input)
        print(move)

        logic = move_logic(user_input, computer_input)

        if logic == "TIE":
            print(logic)
        elif (logic != "TIE") and (logic != None):
            print(logic)
            break


init()
