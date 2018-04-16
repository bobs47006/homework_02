# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:15:10 2018

@author: bob
"""

items = ["PS4", "Switch", "Xbox"]
prices = [100,90,80]
buy=[]

print('We have', end="")
print(*items, sep=", ", end=".\n")
for i in range(3):
    print(items[i], ':', prices[i])
apple = int(input("How much money do you have?"))
while True:
    pie = input("What do you want to buy?(or bye)")
    
    if pie == "bye":
        break
    elif pie in items:
        index=items.index(pie)
        price=prices[index]
        pizza = int(input("How many "+ pie +" do you want to buy?"))
        print("-"*30)
        print("You spend", pizza*price,"dollars to buy",pizza, '"',pie,'."')
        d = pizza*price
        
        
        apple=apple-d
        buy.append((pie,pizza,d))
        if apple<0:
            print("Sorry, you don't have enough money")
            apple+=d
        else:
            
            print("You still have",apple,"left.")
    else:
        print("I don't know what are you talking about. Please try it again.")
        continue
print("-"*30)
print("you bought:", end="\n")
for i,j,k in buy:
    print(i,"X",j,"=",k)
    
        
        
           