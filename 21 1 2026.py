import pandas as pd
import random as rd
import numpy as np
#
#dice1list = []
#dice2list = []
#dice3list = []
#dicesumlist = []
#def dice():
#    return rd.randint(1, 6), rd.randint(1, 6) , rd.randint(1, 6)
#for n in range(20):
#    dice1, dice2, dice3 = dice()
#    sum_dice = dice1 + dice2+ dice3
#    dice1list.append(dice1)
#    dice2list.append(dice2)
#    dice3list.append(dice3)
#    dicesumlist.append(sum_dice)
#
#d = {"dice1": dice1list, "dice2": dice2list, "dice3": dice3list, "sum_dice": dicesumlist}
#df= pd.DataFrame(data=d,index=range(1,21))

def roll_dice(size=20):
    return np.random.randint(1, 7, size=size)
d={"dice1": roll_dice(), "dice2": roll_dice(), "dice3": roll_dice(), }
df = pd.DataFrame(data=d,index=range(1,21))


def read_collumn(collumn):
    return df[collumn]
A=read_collumn("dice1")
B=read_collumn("dice2")
C=read_collumn("dice3")
step1 = A.mul(B,fill_value=0)
product = step1.mul(C,fill_value=0)
sum1= A.add(B,fill_value=0)
sum= sum1.add(C,fill_value=0)


df.insert(3,"sum",sum)
df.insert(4,"product",product)
print (df)