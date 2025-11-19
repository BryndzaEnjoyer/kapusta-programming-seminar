import random
N=1
C=5
M=400
a=50
V=4
q=70
Z=1
rent=100

moneyz=500
D=1


while moneyz >-100:
    go=False
    Ml=800+Z*500
    if q>100:
        Ml=Ml*1.2
    elif q>80:
        Ml=Ml*1.1
    elif q<60:
        Ml=Ml*0.9
    elif q<50:
        Ml=Ml*0.8
    elif q<40:
        Ml=0
    if M>Ml:
        M=Ml
    I= random.uniform(0.8,1.2)
    P = I*N*(C*(M-a*C)-V*(M-a*C)-q*Z-rent)
    moneyz= moneyz+P
    print("Day: ", D)
    print("Todays profit: ", P)
    print("Saved up: ", moneyz)
   
    while go ==False:
        action=input("Any changes?").lower()
        if action=="ad campaign":
            moneyz-=200
            M+=50
        elif action=="coffee quality+":
            a-=15
            V+=1
        elif action=="coffee quality-":
            a+=15
            V-=1
        elif action=="recruitment":
            moneyz-=50
            Ml+=500
            Z+=1
        elif action=="fire somebody":
            if Z==1:
                print("you can't do that")
            else:
                Ml-=1000
                Z-=1
        elif action=="salary":
            q=int(input("How much should they earn?"))
        elif action=="set price":
            C=float(input("New price: "))
        elif action=="expand":
            moneyz-= 10000
            N+=1
        elif action=="make it fancy":
            moneyz -=1000
            a-=15
            M+=100
            rent+=50
        elif action=="ok":
            go =True
        elif action=="even thou this game is excelent I do not wish to play it for the time being": 
            quit()
        else:
            print("wrong command") 
        

    
    D +=1
print("Days running: ", D)