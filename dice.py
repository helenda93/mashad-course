import random
x = random.randint(0,6)
count = 0
for i in range(7):
    count=count+1
    user= int(input())
    if user==x:
        print("cool!")
        print("you tried " + str(count) + " times")
        break

    elif user<x:
        print("try bigger")
    elif user>x:
        print("try smaller")