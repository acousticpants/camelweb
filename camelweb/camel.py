#camel
print()
print("Welcome to Camel!")
print()
print("You have stolen a camel to make your way across the great Mobi desert. The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")


done = False
miles = 0
thirst = 0
camel_tired = 0
natives = -20
canteen = 10

import random
    
while not done:
    
    oasis = random.randrange(20)

    if oasis == 7:
        print("You've found an oasis. Thank f***!")
        canteen = 10
        thirst = 0
        camel_tired = 0
        print()
        print("You refill your canteen, slake your thirst, and rest your camel")
    
   
        
    
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.") 
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print()
    #print(oasis)
    #print(natives)
    u = raw_input("Your choice? ")
    print()
    
    if u.upper() == "Q":
        done = True    
    
    
        
    elif u.upper() == "E":
        print("Miles traveled: ", miles)
        print("Drinks in canteen: ", canteen)
        print("The natives are ", miles - natives , "miles behind you.")
        
    elif u.upper() == "D":
        camel_tired = 0
        print("your camel is happy!")
        natives = natives + random.randrange(7,14)
        
    elif u.upper() == "C":
        miles = miles + random.randrange(10,21)
        print("You have travelled for", miles, "miles.")
        thirst = thirst + 2
        camel_tired = camel_tired + random.randrange(2,5)
        natives = natives + random.randrange(7,14) 
        
    elif u.upper() == "B":
        miles = miles + random.randrange(5,13)
        print("You have travelled for", miles, "miles.")
        thirst = thirst + 1
        camel_tired = camel_tired + random.randrange(1)
        natives = natives + random.randrange(7,14)    
        
    elif u.upper() == "A":
        if canteen > 0:
            canteen = canteen - 1
            thirst = 0
            print("Your thirst is quenched. For now...")
        else:
            print("There is no water left in your canteen.")
            print()
            print("You shake and sqeeze the canteen vigourously for another drop of water. To no avail.")
    
    elif thirst >= 4:
        print("You are getting thirsty.")        

    if miles >= 200:
        print("You have crossed the desert!")
        print()
        print("Congratulations on your survival.")
               
        done = True
               
    if (miles - natives) < 15:
        print("The natives are gaining on you.")
               
    if natives >= miles:
        print("The natives see you in the distance. Shouting and running commences.")
        print("")
        print("They catch up to you, and with much hollering and cursing you are dragged from your saddle.")
        print("")
        print("You begin to sob and wail at your helplessness.")
        print("")
        print("They spear your head to the sand as punishment.")
        print("")
        print("The natives celebrate your death by dancing around your carcass all through the night.")
        print("")
        print("Even your camel joins in the fun.")
                       
        done = True        
           
    if thirst > 4:
        print("You are getting thirsty.")    
           
    if thirst > 6:
        print("You died of thirst.")
        done = True
           
    if camel_tired > 5:
        print("Your camel is feeling tired.")
           
    if camel_tired > 8:
        print("Your camel is dead.")
        print("")
        print("You slide out of the saddle, falling to the sand.")
        print("")
        print("You begin to sob and wail at your helplessness.")
        print("")
        print("The natives see you in the distance. Shouting and running commences.")
        print("")
        print("They catch up to you, and spear your head to the sand as punishment.")
        print("")
        print("The natives celebrate your death by dancing around your carcass all through the night...feasting on strips of your exhausted dead camel.")
               
        done = True

if done == True:
    print("Thank you for playing. Stay hydrated!")  
    
