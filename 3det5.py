import os
import random

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self, name: str, st: int, dx: int, re: int, am: int, fp: int, hp: int):
        self.name = name
        self.st = st
        self.dx = dx
        self.re = re
        self.am = am
        self.fp = fp
        self.hp = hp
        
    def check_valid_input(self):
        total_points = self.st + self.dx + self.re + self.am + self.fp
        if all(0 <= i <= 5 for i in (self.st, self.dx, self.re, self.am, self.fp)) and total_points <= remaining_points:
            return True
        return False
    
    def display_properties(self):
        print("Player name: ", self.name)
        print("Strength: ", self.st)
        print("Dexterity: ", self.dx)
        print("Resistance: ", self.re)
        print("Armor: ", self.am)
        print("Firepower: ", self.fp)
        print("Hit Points: ", self.hp)


remaining_points = 14
print("Points to distribute: ", remaining_points)
player_name = input("Enter player name: ")

fill_type = input("Enter 'm' for manual fill or 'r' for random fill: ")

if fill_type == "m":
    player_st = int(input("Enter player strength (0-5): "))
    remaining_points -= player_st
    print("You still have " , remaining_points , "to spend in DX, RE, AM, FP")
    player_dx = int(input("Enter player dexterity (0-5): "))
    remaining_points -= player_dx
    print("You still have " , remaining_points , "to spend in RE, AM, FP")
    player_re = int(input("Enter player resistance (0-5): "))
    remaining_points -= player_re
    print("You still have " , remaining_points , "to spend in AM, FP")
    player_am = int(input("Enter player armor (0-5): "))
    remaining_points -= player_am
    print("You still have " , remaining_points , "to spend in FP")
    player_fp = int(input("Enter player firepower (0-5): "))
    remaining_points -= player_fp
    print("You still have " , remaining_points )
    player_hp = player_re * 5
    total = player_st+player_dx+player_re+player_am+player_fp
elif fill_type == "r":
    player_st = random.randint(0,5)
    remaining_points -= player_st
    player_dx = random.randint(2,5)
    remaining_points -= player_dx
    player_re = random.randint(1,5)
    remaining_points -= player_re
    player_am = random.randint(0,5)
    remaining_points -= player_am
    player_fp = remaining_points
    remaining_points -= player_fp
    player_hp = player_re * 5
    total = player_st+player_dx+player_re+player_am+player_fp
else:
    print("Invalid input. Please enter 'm' for manual fill or 'r' for random fill.")
    exit()
    
print(player_name)
print("ST:",player_st, "#" * player_st)
print("DX:",player_dx, "#" * player_dx)
print("RE:",player_re, "#" * player_re)
print("AM:", player_am, "#" * player_am)
print("FP:",player_fp, "#" * player_fp)
print("HP:",player_hp, "#" * player_hp)

player = Player(player_name, player_st, player_dx, player_re, player_am, player_fp, player_hp)

#player.display_properties()

print("Total points spent: ", total)

#if player.check_valid_input():
#    print("Player object created with name:", player.name)
#    player.display_properties()
#    print(total)
#else:
#    player.display_properties()
#    print("THERE IS SOME PROBLEM")
#    print(total)
# Choose opponent
   
while True:
    opponent = input("Choose your opponent (1 for Opponent 1, 2 for Opponent 2): ")
    if opponent == '1':
        
        print("11111111")
        opponent_pointsvalue = random.randint(10,15)
        o1name = "Vlad Loco"
        print("opponent_pointsvalue", opponent_pointsvalue)
        
        o1st = random.randint(0,3)
        print("st = " , o1st)
        opponent_pointsvalue -=  o1st
        print("RemainingPoints: " , opponent_pointsvalue)
        
        o1dx = random.randint(1,5)
        print("dx = " , o1dx)
        opponent_pointsvalue -=  o1dx
        print("RemainingPoints: " , opponent_pointsvalue)
        
        o1re = random.randint(1,5)
        print("re = " , o1re)
        opponent_pointsvalue -=  o1dx
        print("RemainingPoints: " , opponent_pointsvalue)
        
        o1am = random.randint(1,5)
        print("am = " , o1am)
        opponent_pointsvalue -=  o1dx
        print("RemainingPoints: " , opponent_pointsvalue)
        
        o1fp = opponent_pointsvalue
        print("fp = " , o1fp)
        opponent_pointsvalue -=  o1dx
        print("RemainingPoints: " , opponent_pointsvalue)
        
        o1hp = o1re * 5
        oDmg = 0
        otDmg = 0
        
        break
    if opponent == '2':
        print('22222222')
        break
    
print("Your Opponent is ", o1name)
print("His attributes are as follows: ")
print("st:" , o1st , "#" * o1st)
print("dx:" , o1dx , "#" * o1dx)
print("re:" , o1re , "#" * o1re)
print("am:" , o1am , "#" * o1am)
print("fp:" , o1fp , "#" * o1fp)
print("HP:" , o1hp , "#" * o1hp)


while ( player_hp > 0 and o1hp >0):
    action = input("Chose your action in combat: 1=Punch 2=Shoot 3=Run: ")
    if action == '1':
        diceAt = random.randint(1,6)
        print("Dice: ",diceAt)
        if diceAt == 6:
            print("Critical Attack")
            atR = player_dx + player_st*2 + diceAt
            
        else:
            print("You attacked the enemy")
            atR = player_dx + player_st + diceAt
        
    if action == '2':
        diceAt = random.randint(1,6)
        print("Dice: ",diceAt)
        if diceAt == 6:
            print("Critical Attack")
            atR = player_dx + player_fp*2 + diceAt
            
        else:
            print("You attacked the enemy")
            atR = player_dx + player_fp + diceAt
        
            
    print("Player's attack is DX:", player_dx, "ST: ", player_st)
    print("player attack is: ",atR)
    print("Defender'S TURN ------")
    diceDf = random.randint(1,6)
    print("Dice Roll is: ", diceDf)
    print("Enemy's Defense is DX:", o1dx, "+ AM:", o1am)
    dfR = o1dx + o1am + diceDf
    print("Defense Roll is: ", dfR)
    if atR>dfR:
        oDmg = atR-dfR
        otDmg += oDmg
        print("Opponent loses ", oDmg , "Hit Points")
        o1hp -= oDmg
    else:
        print("Opponent didnt take damage")
    
    print("Enemy")
    print("HP:" , o1hp , "#" * o1hp, "[]" * oDmg)
    
if player_hp > 0: 
    print("Text to continue the game \n You continue to go to the place where saniofnaos \n try to escape")
    scene2=input("Chose between the path 1, 2, or 3")
        