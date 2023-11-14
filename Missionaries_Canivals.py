print("========= Welcome to the game =============")
print("3 CANNIVALS 3 MISSIONARIES ")
print("3M 3C || ===========BOAT==========|| 0M 0C")
missionaries=3
cannibals=3
l_mi=3
l_can=3
r_mi=0
r_can=0
boat_side="left"
while(True):
    if((r_can==3 and r_mi==3)):
        print("game over")
        print("You Win")
        break

    print("enter number of cannivals and missionaries on boat :",end=" ")
    b_mi,b_can=map(int,input().split())
    if((b_mi+b_can)!=1 and (b_mi+b_can)!=2):
        print("Invalid  Move1 ")
        continue

    if(boat_side=="left"):
        # decrease number of m and c on left
        l_can=l_can-b_can
        l_mi=l_mi-b_mi
        if(l_can<0 or l_mi<0):
            print("invalid move")
            continue

        # increase number of m and c on right
        r_mi=r_mi+b_mi
        r_can=r_can+b_can
        if(r_can>3 or l_mi>3):
            print("invalid move")
            continue
        boat_side="right"
        print(f"{l_mi }  {l_can} ||======{b_mi} {b_can}=>=>=>=>=>=>=>||{r_mi}  {r_can}")

    else:
        # decrease number of m and c on left
        r_can=r_can-b_can
        r_mi=r_mi-b_mi
        
        # increase number of m and c on right
        l_mi=l_mi+b_mi
        l_can=l_can+b_can
        boat_side="left"
        print(f"{l_mi }  {l_can} ||<=<=<=<=<=<={b_mi}  {b_can}=======||{r_mi}   {r_can}")
    if((l_mi<l_can and l_mi>0) or (l_mi<l_can and l_mi>0)):
        print("you loose")
        break



