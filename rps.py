import random

b = input("pick your pick 1-rock 2-scissors 3-paper : \n")

b = int(b)

print("you chose :")

if b==1:
    print("rock") 

elif b==2 :
    print("paper")

elif b==3 :
    print("scissors") 

elif b>3 :
    print("to not read the rules, properly.")
    quit()
elif b<1 :
    print("violence")
    quit()

a = random.randint(1,3)

print("computer chose :")

if a==1:
    print("rock") 
    if  b== 1:
            print(" its a tie")

    elif b==2:
            print("you won")

    elif b==3:
            print("you lost")

elif a==2 :
    print("paper")  
    if  b== 1:
            print(" you lost")

    elif b==2:
            print("its a tie")
            
    elif b==3:
            print("you won")

elif a==3 :
    print("scissors") 
    if  b== 1:
            print(" you won")

    elif b==2:
            print("you lost")
            
    elif b==3:
            print("its a tie")



