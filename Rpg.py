import random
print("\n")
print("🌍 Your World Is in Danger! 💀 Aliens Are Attacking! ⚠️".center(100))
print("You Are the Saviour 🦸‍♂️... Prepare to Fight the Enemies!\n".center(100))

enemyHealth = 100
playerHealth = 100
def userAttack():
    Health = random.randint(10,20)
    global enemyHealth
    enemyHealth = enemyHealth - Health
    print(f"You dealt {Health} damage to the enemy.")
def enemyAttack():
    Health = random.randint(10,20)
    global playerHealth
    playerHealth = playerHealth - Health
    print(f"Enemy dealt {Health} damage to the You.")
def show(en,pl):
    print(f"\n🦸 Your Health {pl} | 👽 Enemy Health {en}\n")
def op():
    global enemyHealth
    global playerHealth
    while not(enemyHealth<=0 or playerHealth<=0):
        options = int(input("Choose Your Move and beat the monster\n1.Attack\n2.Heal\n-->"))
        match options:
            case 1:
                print("\n➡️ You chose Attack!")
                userAttack()
                print("\n👽 Enemy Attack You!")
                enemyAttack()
                if enemyHealth>=0 or playerHealth>=0:
                    show(enemyHealth,playerHealth)
            case 2:
                print("➡️ You Are Healing!")
                health = random.randint(1,6)
                if playerHealth+health<=100:
                    playerHealth = playerHealth + health
                    print(f"\nYour Health Increases by {health}\n")
                    show(enemyHealth,playerHealth)
                else:
                    print("\nYour Health is Full\n")
                    show(enemyHealth,playerHealth)
            case _:
                print("Invalid You Have To Die...")
        
op()
if enemyHealth<=0:
    print("Congratulations...You Beat The Monster🎉🫡\n")
else:
    print("ohh noooo.....Saviour Died☹️\n")
    print("Game Over...\n")
