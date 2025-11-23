
import random

def myfun(n):
    lst=['rock','paper','scissor']
    s=0
    a=0
    i=0
    for i in range(1,n+1):
        print(f"----round {i}----")
        ch=input("enter rock,paper,scissor: ")
        c=random.choice(lst)
        print(c)
         
    
    
        if ch=='paper' and c=='rock' or ch=='scissor' and c=='paper' or ch=='rock' and c=='scissor':
            s+=1
            print("win")
            if s>(n/2):
                break
        elif c=='paper' and ch=='rock' or c=='scissor' and ch=='paper' or c=='rock' and ch=='scissor':
            a+=1
            print("lose")
            if a>(n/2):
                break
        else:
            i+=1
            print("tie")
        
    if s>a or i==s and a<s or i==a and a<s:
        print("------------------you win the game-------------")
    elif a>s or i==s and a>=s or i==a and a>s:
        print("-----------------you lost the game--------------")
        
    else:
        print("-------------------try again--------------------")
        
n=int(input("enter no of rounds to play"))       
myfun(n)
print("------------------game over------------------------------")


 

    
