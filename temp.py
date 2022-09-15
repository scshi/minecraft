import rngworld as r

def version189(name): 
    #you will start with a basic base
    
    day = 0

    again = True
    while again:
        #prints what day you are on
        print("******DAY " + str(day) + "******")

        #after 40 days the difficulty goes up
        if day < 40:
            r.easy(name) 
        elif day < 80:
            r.intermediate()
        else:
            r.hard()
        day = day + 1 #goes to next day
        


def versionlatest():
    print("here 2")


#choose 1.8.9
def setup():
    
    print("Text Adventures (Minecraft)")
    
    print("******SETUP******")
    name = input("What do you want your IGN (in game name) to be: ")
   
    version = int(input("""******PICK VERSION******
    
    (Due to new blocks being added constantly 
    throughout minecraft's lifespan,
    you have to choose which version you want)
    
    1. 1.8.9 
    2. Latest
    3. Exit
    
    Choose: """))
    again = 1
    while again == 1:
        if version == 1:
            version189(name)
        elif version == 2:
            versionlatest()
        else:
            pass

