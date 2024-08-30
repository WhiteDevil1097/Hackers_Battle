import random
import time
import requests
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '''
 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████ ▓█████▄ 
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▒██▀ ██▌
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ░██   █▌
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ░▓█▄   ▌
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░▒████▓ 
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒▒▓  ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░ ░ ▒  ▒ 
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░    ░ ░  ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░                   ░                       ░     
 '''
animated(logo)
print('      »»»Devoloper By White_Devil«««')
print('      _________________________________')

# Game settings
player_health = 1000
hacker_health = 1000
game_over = False

def display_intro():
    print("Welcome to the Hacking Battle Game!")
    print("You (the player) will engage in a hacking battle against a stronger hacker.")
    print("Take turns attacking each other until one is defeated.")
    print("If your health drops to 0, you lose. If the hacker's health drops to 0, you win.")
    print("Let's begin the battle!")
    time.sleep(3)

def player_turn():
    global hacker_health
    print("\nYour turn to attack!")
    time.sleep(1)
    
    attack_type = input("Choose your attack (metasploit, pegasus, brute_force): ").strip().lower()
    if attack_type == "metaspoloit":
        damage = random.randint(200, 250)
        hacker_health -= damage
        print(f"Metaspoloit attack successful! Hacker's health reduced by {damage}.")
    elif attack_type == "pegasus":
        damage = random.randint(250, 350)
        hacker_health -= damage
        print(f"Pegasus successful! Hacker's health reduced by {damage}.")
    elif attack_type == "brute_force":
        damage = random.randint(350, 400)
        hacker_health -= damage
        print(f"Brute force attack successful! Hacker's health reduced by {damage}.")
    else:
        print("Invalid attack! You missed your chance to attack.")
    
    time.sleep(1)
    if hacker_health <= 0:
        print("You have defeated the hacker! Victory is yours!")
        return True
    else:
        print(f"Hacker's remaining health: {hacker_health}")
    return False

def hacker_turn():
    global player_health
    print("\nHacker's turn to attack!")
    time.sleep(1)
    
    attack = random.choice(["SQL_injection", "DDoS", "exploit"])
    damage = random.randint(350, 400)
    player_health -= damage
    print(f"Hacker used {attack}! Your health reduced by {damage}.")
    
    time.sleep(1)
    if player_health <= 0:
        print("The hacker has defeated you! Game over.")
        return True
    else:
        print(f"Your remaining health: {player_health}")
    return False

def main():
    display_intro()

    while not game_over:
        if player_turn():
            break
        if hacker_turn():
            break

    print("\nThanks for playing the Hacking Battle Game!")

if __name__ == "__main__":
    main()

