import random


def getChoices():
    playerChoice = input("enter a choice (rock,paper or scissor)")
    options = ["rock","paper","scissor"]
    computerChoice = random.choice(options)
    choices = {"player":playerChoice,"computer":computerChoice}

    return choices

def checkWin(player,computer):
    # print("you chose " + player + ", the computer chose + " + computer)
    print(f"you chose {player}, the computer chose {computer}")
    if player == computer:
        return "It's a Tie!"
    elif player == "rock" and computer == "scissor":
        return "Rock smashes scissor. You win!"
    elif player == "scissor" and computer == "rock":
        return "Rock smashes scissor. You win!"
    elif player == "rock" and computer == "paper":
        return "paper covers rock. You lose!"
    elif player == "paper" and computer == "rock":
        return "paper covers rock. You win!"
    elif player == "paper" and computer == "scissor":
        return "scissor cuts paper. You lose!"
    elif player == "scissor" and computer == "paper":
        return "scissor cuts paper. You win!"
    

choices = getChoices()
result = checkWin(choices["player"],choices["computer"])
print(result)


# age = 20
# print(f"i am {age} years old.")  #---------another method to concat string