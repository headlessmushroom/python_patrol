import random


print(" rules: \n 1. the first dude starts with x (i'm still working on so that first dude can pick o or but for now it is what it is) \n 2. u can pick your square by entering coordinates of the matrix.\n >1 1 (top left) \n >1 3 (top right) \n >3 1 (bottom left) \n >3 3 (bottom right) \n >2 2 (middle)\n 3. the rest of the game is similar standard tictactoe")
print(">_0")
a = 0
b = 0

t11 = " "
t12 = " "
t13 = " "
t21 = " "
t22 = " "
t23 = " "
t31 = " "
t32 = " "
t33 = " "


complete = [1,1,1,1,1,1,1,1,1]

intake = [0,0,0,0,0,0,0,0,0]

turn = 0

turn = int(turn)

x = ""
o = ""
amithab = " "
bachan = ""

while amithab != bachan :
    x = input("what do you want x or o:")

    if x == "x":
        amithab = bachan
        o = "o"

    elif x == "o":
        amithab = bachan
        o = "x"

    else :
        print("try again")






while intake != complete :

    sanitycheck = False

    while sanitycheck == False : #input and input processing

       
        m,n = input("type (m n) m columns and n rows :").split()

        m = int(m)
        n = int(n)

        if m >3 or m< 1:
            print("check the row")
            
            a = 0
            
            
        else :
            a = m
            sanitycheck = True

        if n >3 or n<1 :
            print("check the column")
            
            b = 0
        
        elif n == 1 :
            b = 5
            sanitycheck = True

        elif n == 2 :
            b = 7
            sanitycheck = True
        else :
            b = 11
            sanitycheck = True


    c= a*b
    #print("value of c:",c)
    #print("a:",a , "b:", b, "; m:", m, "n:", n)
    
    if turn%2 == 0:
        
        if c == 5 and t11 == " " :
            t11 = x
        elif c == 7 and t12 == " ":
            t12 = x
        elif c == 11 and t13 == " ":
            t13 = x
        elif c == 10 and t21 == " ":
            t21 = x
        elif c == 14 and t22 == " ":
            t22 = x
        elif c == 22 and t23 == " ":
            t23 = x
        elif c == 15 and t31 == " ":
            t31 = x
        elif c == 21 and t32 == " ":
            t32 =x
        elif c == 33 and t33 == " ":
            t33 = x
        elif c ==0 :
            print("out of range: try again")
        else :
            print("common the other dude picked it")


    elif turn%2 != 0:
             
        if c == 5 and t11 == " " :
            t11 = o
        elif c == 7 and t12 == " ":
            t12 = o
        elif c == 11 and t13 == " ":
            t13 = o
        elif c == 10 and t21 == " ":
            t21 = o
        elif c == 14 and t22 == " ":
            t22 = o
        elif c == 22 and t23 == " ":
            t23 = o
        elif c == 15 and t31 == " ":
            t31 = o
        elif c == 21 and t32 == " ":
            t32 =o
        elif c == 33 and t33 == " ":
            t33 = o
        elif c ==0 :
            print("out of range: try again")
        else :
            print("common the other dude picked it")



    print("\n",t11,"|",t12,"|",t13,"\n",t21,"|",t22,"|",t23,"\n",t31,"|",t32,"|",t33)

   


    # quotient 0 to 8 interms of m and n 
    
    # 1,1 - 1 - 0
    # 1,2 - 2 - 1
    # 1,3 - 3 - 2
    # 2,1 - 4 - 3
    # 2,2 - 5 - 4
    # 2,3 - 6 - 5
    # 3,1 - 7 - 6
    # 3,2 - 8 - 7
    # 3,3 - 9 - 8

    # n*3-(3-m)
    
    q = n*3 + m - 4
    if 0<= q <= 8 :

        if intake[q] == 1 :
            print("the block is full, please mind")
        else :
            intake[q] = 1
            turn = turn+1
            #print (turn)
            
    else :
        print("out of range try, try again")

    

    if t11 == t12 == t13 != " " or t21 == t22 == t23 != " " or t31 == t32 == t33 != " " or t11 == t21 == t31 != " " or t12 == t22 == t32 != " " or t13 == t23 == t33 != " " or t11 == t22 == t33 != " " or t13 == t22 == t31 != " " :
        if t11 or t22 or t33 == "x":
            print(x," won")
            quit()

        elif t11 or t22 or t33 == "o":
            print(o," won")
            quit()
        else :
            print(" u shouldnt get this message, if u get this message txt me, i fucked up.")

        

    elif turn%2 == 0:
                print(x,"'s turn ")
    elif turn%2 != 0:
                print(o,"'s turn")

       
    else :
        print("TIE")

    





# fun ideas
# take a list input, then split the list to get inputs, -> u can if loop to get the input again if he puts only one number in list 
#
# let the user pick if they start or the computer starts. 
#       they say yes they are odd and you are even vice versa
#
#  random function - to place the x or o's anywhere remaining
# 