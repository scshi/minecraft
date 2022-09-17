import random

def adventure():
    direction = str(random.randint(1,4))
    
    #turns the random integer into a direction
    if direction == "1":
        direction = "North"
    elif direction == "2":
        direction = "East"
    elif direction == "3":
        direction = "South"
    elif direction == "4":
        direction = "West"
    
#gives a repeatable start
def start(name):
    choice = int(input("""******CHOICE******
    1) Build house (Free)
    2) Go out trekking"""))
    if choice == 1:
        print()
        

def easy(name):
    choice = int(input("""******CHOICE******
    1) You could go out trekking into the wilderness
    2) You could improve your base 
    choose: """))
    if choice == 1:
        adventure()
    
    rannum = random.randint(1,10)
    