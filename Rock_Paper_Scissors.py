# Rock Paper Scissors
# Hello_Own_World 25.08.19
while True :
    lst = ["rock", "paper", "scissors"]
    player_1 = input("First player : ")
    if player_1 not in lst :
        print("Wrong input try again ")
        continue
    player_2 = input("Second player :")
    if player_2 not in lst:
        print("Wrong input try again ")
        continue
    if player_1 == player_2 :
        print("Draw")
    elif player_1 == "rock" and player_2 == "paper" or player_1 == "paper" and player_2 == "scissors" or player_1 == "scissors" and player_2 == "rock" :
        print("Player 2 won !")
    elif player_1 == "rock" and player_2 == "scissors" or player_1 == "paper" and player_2 == "rock" or player_1 == "scissors" and player_2 == "paper" :
        print("Player 1 won !")










