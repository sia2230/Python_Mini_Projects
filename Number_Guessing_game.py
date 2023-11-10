import random
print("============= NUMBER GUESSING GAME =========== ")
print("Enter minimum and maximum :")
a,b=map(int,input().split())
number=random.randint(a,b)
print("you have only 3 Chances ")
for i in range(3):
    number_2=int(input("Enter number :"))
    if(number_2>number):
        print(" Your guess is larger than the number ")
    elif(number_2<number):
        print(" Your guess is smaller than the number ")
    else:
        print("=========== YOU WON =============")
        break
else:
    print(" Better luck next time !!!")    