import random

def gamewine(comp, you):
    if comp == you:
         return None
    
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
        
    elif comp == 'g':
        if you == 'w':
            return False
        elif you == 's':
            return True
        

comp = input("computer turn : snack(s) water(w) gun(g) ")
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input("users turn : snack(s) water(w) gun(g) : ")


a = gamewine(comp, you)
print(f"computer chose : {comp}")
print(f"user chose : {you}")


if a == None:
    print("game is tie")

elif a == True:
    print("you won")
elif a == False:
    print("you lose")


        