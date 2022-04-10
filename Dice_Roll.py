import random
x = True
while x==True:
    number = random.randint(1,6)
    print(number)
    say = input("do you want to roll it again (y/n) :")
    ans = say.lower()
    if ans == 'y' :
        x=True
    else:
        x= False

