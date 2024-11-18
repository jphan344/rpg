import random

# Welcome message
print ("After many trials and tribulations, you have found the treasure of the dread captain Templeton 'Scarface' Darby.")
print ("But before you can open the chest, the specter of the long dead pirate appears before you!")
print ("'Arrrgh! On guard ye foul landlubber! Or prove to me that ye got yer sealegs!'")
print ("Captain Scarface challenges you to a battle!\n")
print("Instructions: You and the enemy will take turns attacking each other.")
print("Each attack reduces health, and the game ends when one character’s health reaches zero.")
print("Let's begin!\n")

# Initialize health points
player_health = 100
enemy_health = 100

# Define the display_status function
def display_status():
    print(f"Player Health: {player_health}")
    print(f"Enemy Health: {enemy_health}\n")

# Define the player_attack function
def player_attack():
    global enemy_health
    damage = random.randint(10, 20)
    enemy_health -= damage
    print(f"You attack the enemy for {damage} damage!")

# Define the enemy_attack function
def enemy_attack():
    global player_health
    damage = random.randint(10, 20)
    player_health -= damage
    print(f"The enemy attacks you for {damage} damage!")

# Define the check_victory function
def check_victory():
    if player_health <= 0:
        print("You have been defeated! Game over.")
        return True
    elif enemy_health <= 0:
        print("Congratulations! You have defeated the enemy.")
        return True
    return False

# Main game loop
game_run = True
while game_run:
    display_status()
    action = input("Enter 'a' to attack or 'q' to quit: ").lower()
    
    if action == 'a':
        player_attack()
        if check_victory():
            game_run = False
            break
        
        enemy_attack()
        if check_victory():
            game_run = False
            break
    elif action == 'q':
        print("You have chosen to quit the game. Goodbye!")
        game_run = False
    else:
        print("Invalid input, please enter 'a' to attack or 'q' to quit.")

print("Thank you for playing!")
