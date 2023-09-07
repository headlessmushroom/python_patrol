import random

m,n = input("type (m,n) m columns and n rows (>_0)  :").split()

m = int(m)
n = int(n)

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


if m >3 or m< 1:
    print("nope")
    quit()
else :
    a = m




if n >3 or n<1 :
    print("nah dah")
    quit()

elif n == 1 :
    b = 5

elif n == 2 :
    b = 7

else :
    b = 11


c= a*b
print("value of c:",c)
print("a:",a , "b:", b, "; m:", m, "n:", n)

if c == 5:
    t11 = "x"
elif c == 7:
    t12 = "x"
elif c == 11:
    t13 = "x"
elif c == 10:
    t21 = "x"
elif c == 14:
    t22 = "x"
elif c == 22:
    t23 = "x"
elif c == 15 :
    t31 = "x"
elif c == 21 :
    t32 ="x"
elif c == 33 :
    t33 = "x"


print("\n",t11,"|",t12,"|",t13,"\n",t21,"|",t22,"|",t23,"\n",t31,"|",t32,"|",t33)


complete = [1,1,1,1,1,1,1,1,1]

intake = [0,0,0,0,0,0,0,0,0]

    
q = n*3 + m - 4
    
if intake[q] == 1 :
    print("ergh filled")
else :
    intake[q] = 1





while intake != complete :

    sanitycheck = False

    while sanitycheck == False :

        m,n = input("type (m,n) m columns and n rows (>_0)  :").split()

        m = int(m)
        n = int(n)

        if m >3 or m< 1:
            print("nope")

            quit()
            
        else :
            a = m
            sanitycheck = True

        if n >3 or n<1 :
            print("nah dah")
            quit()
        
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
    print("value of c:",c)
    print("a:",a , "b:", b, "; m:", m, "n:", n)
    
    
    if c == 5:
        t11 = "x"
    elif c == 7:
        t12 = "x"
    elif c == 11:
        t13 = "x"
    elif c == 10:
        t21 = "x"
    elif c == 14:
        t22 = "x"
    elif c == 22:
        t23 = "x"
    elif c == 15 :
        t31 = "x"
    elif c == 21 :
        t32 ="x"
    elif c == 33 :
        t33 = "x"


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
    
    if intake[q] == 1 :
        print("ergh filled")
    else :
        intake[q] = 1


# who won 
# if that then they won
