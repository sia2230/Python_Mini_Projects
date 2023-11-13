import random as rd
list=['Rock', 'Paper', 'Scissor']
print("============= Welcome to the game ===============")
print("============= Rock, Paper, Scissors =============")
while(True):
    print("you have three choices :Rock, Paper, Scissor ")
    player_a=input(" Enter your choice ")
    computer=rd.choice(list)
    print("computer choose : ",computer)
    if computer=="Rock":
        if player_a=="Scissor":
            print("Computer is winner")
            break
        elif player_a=="Paper":
            print("player_a is winner")
            break
        else:
            print("tie")
    elif computer=="Paper":
        if player_a=="Scissor":
            print("player_a  is winner")
            break
        elif player_a=="Rock":
            print("computer is winner")
            break
        else:
            print("tie")
    elif computer=="Scissor":
        if player_a=="Paper":
            print("computer  is winner")
            break
        elif player_a=="Rock":
            print("player_a is winner")
            break
        else:
            print("tie")
