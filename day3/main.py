print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\" \n")

if direction == "right":
    print("You come across a bridge guarded by a troll.")
    action = input("Do you want to 'fight' or 'run away'? \n")
    
    if action == "fight":
        print("You defeat the troll and cross the bridge.")
        next_step = input("You see a castle in the distance. Do you want to 'approach' it or 'continue' on your path? \n")
    
    if next_step == "approach":
        print("As you approach the castle, you encounter a drawbridge.")
        drawbridge = input("Do you want to 'lower' the drawbridge or 'find another way' into the castle? \n")
        
        if drawbridge == "lower":
            print("The drawbridge lowers and you enter the castle.")
            print("You explore the castle and find a hidden passage leading to the treasure room!")
            print("Congratulations! You found the treasure. You win!")
        elif drawbridge == "find another way":
            print("You search for another way into the castle and find a secret entrance.")
            print("You sneak into the castle and discover a hidden treasure chamber!")
            print("Congratulations! You found the treasure. You win!")
        else:
            print("Invalid input! Game over.")
    elif next_step == "continue":
        print("You continue on your path and find a magical portal.")
        portal = input("Do you want to 'enter' the portal or 'avoid' it? \n")
        
        if portal == "enter":
            print("You enter the portal and find yourself in a treasure room!")
            print("Congratulations! You found the treasure. You win!")
        elif portal == "avoid":
            print("You decide to avoid the portal and keep exploring.")
            print("After a long journey, you finally find the treasure hidden in a cave!")
            print("Congratulations! You found the treasure. You win!")
        else:
            print("Invalid input! Game over.")
    else:
        print("Invalid input! Game over.")
elif action == "run away":
    print("You run away from the troll and get lost in the forest. After wandering for hours, you stumble upon a hidden cave.")
    cave = input("Do you want to 'enter' the cave or 'continue' on your path? \n")
    
    if cave == "enter":
        print("You enter the cave and find a treasure chest!")
        print("Congratulations! You found the treasure. You win!")
    elif cave == "continue":
        print("You decide to continue on your path and eventually reach a deserted island.")
        island = input("Do you want to 'explore' the island or 'sail away'? \n")
        
        if island == "explore":
            print("You explore the island and discover a buried treasure!")
            print("Congratulations! You found the treasure. You win!")
        elif island == "sail away":
            print("You sail away from the island and embark on a new adventure.")
            print("Unfortunately, you never find the treasure. Game over.")
        else:
            print("Invalid input! Game over.")
    else:
        print("Invalid input! Game over.")
else:
    print("Invalid input! Game over.")

