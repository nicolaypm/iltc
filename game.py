import cmd
import textwrap
import sys
import os
import random
import time
import socket

#strings
screen_width = 100

#player damage strings

player_damage = 30
player_damage_money = 50
#mp damage strings

mp_damage = 45
mp_damage_money = 100
#hp upgrade strings

hp_upgrade = 50
hp_upgrade_money = 100
#magical stick strings

magical_stick_money = 100
magical_stick = 1
#healing potion strings

healing_potion_money = 25
healing_potion = 1
healing_potion_hp = 20

#random
value = random.randint(1, 6)
value2 = random.randint(1, 2)
value3 = random.randint(1, 5)

#magic
explosion_magic_points = 5
healing_magic_points = 2
fire_magic_points = 2
water_magic_points = 1

#rewards
kill_quest_money_reward = 200

# player setup
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.magic_learnt = ''
        self.hp = 0
        self.mp = 0
        self.sword_d = 0
        self.money = 0
        self.healing_potion = 0
        self.magical_stick = 0
        self.monster_health = 550
        self.monster_damage = 20
        self.status_effects = []
        self.location = 'home'
        self.location_com = '4e'
        self.game_over = False
        self.healing_com = 0
        self.mp_com = 0
        self.magical_staff = 0
        self.magical_book = 0

class magical_book:
    def __init__(magic):
        magic.magical_points = 0
        magic.explosion_damage = 300
        magic.healing = 40
        magic.fire_damage = 60
        magic.water_damage = 10

class items:
    def __init__(item):
        item.stick = 0
        item.stone = 0
        item.wood = 0
        item.iron = 0

class crafting:
    def __init__(crafted):
        crafted.club = 'not club'

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        system.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            system.exit()

myPlayer = player()
mymagic = magical_book()
item = items()
itemCrafted = crafting()

def title_screen():

    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('          -play-            ')
    print('          -help             ')
    print('          -quit             ')
    title_screen_selections()

def help_menu():
    print("\n")
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('Use attack to attack a enemy')
    print('Use Healing to heal yourself')
    print('Use shop to buy items for your inventory')
    print('Ues inventory to access inventory')
    title_screen_selections()

#---------- what would you like to do? ------------#
def prompt():
    if myPlayer.location_com == '5c':
        print("\n#######################################")
        print("#    what would you like to choose?   #")
        print("#######################################")
        print("---------------------------------------")
        print("                  quit                 ")
        print("---------------------------------------")
        print("                   map                 ")
        print("---------------------------------------")
        print("                inventory              ")
        print("---------------------------------------")
        print("               magical book            ")
        print("---------------------------------------")
        print("                   shop                ")
        print("---------------------------------------")
        print("                read news              ")
        print("---------------------------------------")
        print("\n" + "==========================")
        print("what would you like to do?")
        action2 = input("> ")

        if action2.lower() == 'quit':
            sys.exit()

        elif action2.lower() == 'inventory':
            inventory()

        elif action2.lower() == 'magical book':
            magicaBook()

        elif action2.lower() == 'read news':
            readNews()

        elif action2.lower() == 'shop':
            shop()

        elif action2.lower() == 'map':
            map()

    elif myPlayer.location_com == '4i':
        print("\n#######################################")
        print("#    what would you like to choose?   #")
        print("#######################################")
        print("---------------------------------------")
        print("                  quit                 ")
        print("---------------------------------------")
        print("                   map                 ")
        print("---------------------------------------")
        print("                inventory              ")
        print("---------------------------------------")
        print("               magical book            ")
        print("---------------------------------------")
        print("                   shop                ")
        print("---------------------------------------")
        print("                read news              ")
        print("---------------------------------------")
        print("\n" + "==========================")
        print("what would you like to do?")
        action2 = input("> ")

        if action2.lower() == 'quit':
            sys.exit()

        elif action2.lower() == 'inventory':
            inventory()

        elif action2.lower() == 'magical book':
            magicaBook()

        elif action2.lower() == 'read news':
            readNews()

        elif action2.lower() == 'shop':
            shop()

        elif action2.lower() == 'map':
            map()

    elif myPlayer.location_com == '6g':
        print("\n#######################################")
        print("#    what would you like to choose?   #")
        print("#######################################")
        print("---------------------------------------")
        print("                  quit                 ")
        print("---------------------------------------")
        print("                   map                 ")
        print("---------------------------------------")
        print("                inventory              ")
        print("---------------------------------------")
        print("               magical book            ")
        print("---------------------------------------")
        print("                   shop                ")
        print("---------------------------------------")
        print("                read news              ")
        print("---------------------------------------")
        print("\n" + "==========================")
        print("what would you like to do?")
        action2 = input("> ")

        if action2.lower() == 'quit':
            sys.exit()

        elif action2.lower() == 'inventory':
            inventory()

        elif action2.lower() == 'magical book':
            magicaBook()

        elif action2.lower() == 'read news':
            readNews()

        elif action2.lower() == 'shop':
            shop()

        elif action2.lower() == 'map':
            map()

    elif myPlayer.location_com == '7i':
        print("\n#######################################")
        print("#    what would you like to choose?   #")
        print("#######################################")
        print("---------------------------------------")
        print("                  quit                 ")
        print("---------------------------------------")
        print("                   map                 ")
        print("---------------------------------------")
        print("                inventory              ")
        print("---------------------------------------")
        print("               magical book            ")
        print("---------------------------------------")
        print("                   shop                ")
        print("---------------------------------------")
        print("                read news              ")
        print("---------------------------------------")
        print("\n" + "==========================")
        print("what would you like to do?")
        action2 = input("> ")

        if action2.lower() == 'quit':
            sys.exit()

        elif action2.lower() == 'inventory':
            inventory()

        elif action2.lower() == 'magical book':
            magicaBook()

        elif action2.lower() == 'read news':
            readNews()

        elif action2.lower() == 'shop':
            shop()

        elif action2.lower() == 'map':
            map()

    elif myPlayer.location_com == '8b':
        print("\n#######################################")
        print("#    what would you like to choose?   #")
        print("#######################################")
        print("---------------------------------------")
        print("                  quit                 ")
        print("---------------------------------------")
        print("                   map                 ")
        print("---------------------------------------")
        print("                inventory              ")
        print("---------------------------------------")
        print("               magical book            ")
        print("---------------------------------------")
        print("                   shop                ")
        print("---------------------------------------")
        print("                read news              ")
        print("---------------------------------------")
        print("\n" + "==========================")
        print("what would you like to do?")
        action2 = input("> ")

        if action2.lower() == 'quit':
            sys.exit()

        elif action2.lower() == 'inventory':
            inventory()

        elif action2.lower() == 'magical book':
            magicaBook()

        elif action2.lower() == 'read news':
            readNews()

        elif action2.lower() == 'shop':
            shop()

        elif action2.lower() == 'map':
            map()

    elif myPlayer.location_com == '1b':
        print("\n#######################################")
        print("#    what would you like to choose?   #")
        print("#######################################")
        print("---------------------------------------")
        print("                  quit                 ")
        print("---------------------------------------")
        print("                   map                 ")
        print("---------------------------------------")
        print("                inventory              ")
        print("---------------------------------------")
        print("               magical book            ")
        print("---------------------------------------")
        print("                   shop                ")
        print("---------------------------------------")
        print("                read news              ")
        print("---------------------------------------")
        print("\n" + "==========================")
        print("what would you like to do?")
        action2 = input("> ")

        if action2.lower() == 'quit':
            sys.exit()

        elif action2.lower() == 'inventory':
            inventory()

        elif action2.lower() == 'magical book':
            magicaBook()

        elif action2.lower() == 'read news':
            readNews()

        elif action2.lower() == 'shop':
            shop()

        elif action2.lower() == 'map':
            map()

    else:
        print("\n#######################################")
        print("#    what would you like to choose?   #")
        print("#######################################")
        print("---------------------------------------")
        print("                  quit                 ")
        print("---------------------------------------")
        print("                   map                 ")
        print("---------------------------------------")
        print("                inventory              ")
        print("---------------------------------------")
        print("               magical book            ")
        print("---------------------------------------")
        print("                 missions              ")
        print("---------------------------------------")
        print("                  sleep                ")
        print("---------------------------------------")
        print("\n" + "==========================")
        print("what would you like to do?")
        action = input("> ")

        if action.lower() == 'quit':
            sys.exit()

        elif action.lower() == 'sleep':
            sleep()

        #------------inventory---------#
        elif action.lower() == 'inventory':
            inventory()

        #---------- map ----------#
        elif action.lower() == 'map':
            map()

        #------------- magical book ---------#
        elif action.lower() == 'magical book':
            magicaBook()

        #---------- missions -----------#
        elif action.lower() == 'missions':
            missions()

        #---------- craft ------------#
        elif action.lower() == 'craft':
            craft()

#-------- commands ---------#
def inventory():
    print("\n")
    print("--------------------------------------------------------------------------------------------------")
    print("#                                         healing potions                                        #")
    print(myPlayer.healing_potion)
    print("--------------------------------------------------------------------------------------------------")
    print("#                                          magical stick                                         #")
    print(myPlayer.magical_stick)
    print("--------------------------------------------------------------------------------------------------")
    print("#                                               hp                                               #")
    print(myPlayer.hp)
    print("--------------------------------------------------------------------------------------------------")
    print("#                                               mp                                               #")
    print(myPlayer.mp)
    print("--------------------------------------------------------------------------------------------------")
    print("#                                            location                                            #")
    print(myPlayer.location_com)
    print("--------------------------------------------------------------------------------------------------")
    print("#                                          magic learnt                                          #")
    print(myPlayer.magic_learnt)
    print("--------------------------------------------------------------------------------------------------")

    if myPlayer.magical_staff >= 1:
        print("#                                you have a powerful magical staff                               #")
        print("--------------------------------------------------------------------------------------------------")

    if myPlayer.magical_book >= 1:
        print("#                                you have a magical book that says                               #")
        print("#    aWYgeW91IGNhbiByZWFkIHRoaXMgaXQgbWVhbnMgdGhhdCB5b3UgYXJlIGEgcG93ZXJmdWwgbWFnaWMgdXNlcg==    #")
        print("--------------------------------------------------------------------------------------------------")

    print("\n#######################################")
    print("#    what would you like to equip?    #")
    print("#######################################")
    equip = input("> ")

    if myPlayer.magical_staff >= 1:
        if equip.lower() == 'equip magical staff':
            print("\n######################################")
            print("#    you equipped a magical staff    #")
            print("######################################")
            mymagic.explosion_damage = 500
            mymagic.fire_damage = 100
            mymagic.water_damage = 50

def magicaBook():
    print("\n#############################")
    print("#    your magical points    #")
    print(mymagic.magical_points)
    print("#############################")
    print("-------------------------")
    print("#    explosion magic    #")
    print("-------------------------")
    print("#     healing magic     #")
    print("-------------------------")
    print("#      fire magic       #")
    print("-------------------------")
    print("#      water magic      #")
    print("-------------------------")
    print("\nwhat would you like to learn?")
    acceptable_magic = ['explosion magic', 'healing magic', 'fire magic', 'water magic']
    magic = input("> ")

    if magic == 'explosion magic':
        print("\n###################################")
        print("#    you learnt explosion magic   #")
        print("###################################")
        myPlayer.magic_learnt = 'explosion magic'
        mymagic.magical_points -= explosion_magic_points

    elif magic == 'healing magic':
        print("\n##################################")
        print("#    you learnt healing magic    #")
        print("##################################")
        myPlayer.magic_learnt = 'healing magic'
        mymagic.magical_points -= healing_magic_points

    elif magic == 'fire magic':
        print("\n###############################")
        print("#    you learnt fire magic    #")
        print("###############################")
        myPlayer.magic_learnt = 'fire magic'
        mymagic.magical_points -= fire_magic_points

    elif magic == 'water magic':
        print("\n################################")
        print("#    you learnt water magic    #")
        print("################################")
        myPlayer.magic_learnt = 'water magic'
        mymagic.magical_points -= water_magic_points

def sleep():
    print("\n##############################################")
    print("#    you go to sleep and wake up next day    #")
    print("##############################################")
    myPlayer.hp = myPlayer.healing_com
    myPlayer.mp = myPlayer.mp_com

def missions():
    print("\n----------------------------------------")
    print("you can choose which one of the missions")
    print("----------------------------------------")
    print("#              kill quest              #")
    print("----------------------------------------")
    print("\nwhich mission would you like to choose?")
    acceptable_missions = ['kill quest', '', '', '', '', '']
    missions = input("> ")

    if missions.lower() == 'kill quest':
        print("\n#####################################")
        print("#    prepare yourself for battle    #")
        print("#####################################")
        quests()

def shop():
    print("\n" + "###############################")
    print("#     Welcome to the shop     #")
    print("###############################")
    print("\n" + "=============================")
    print("#    gold    #")
    print(myPlayer.money)
    print("##############")
    print("-----------------------")
    print("#    sword upgrade    #")
    print("-----------------------")
    print("#      mp upgrade     #")
    print("-----------------------")
    print("#      hp upgrade     #")
    print("-----------------------")
    print("#    magical stick    #")
    print("-----------------------")
    print("#    healing potion   #")
    print("-----------------------")
    print("#     a pet dragon    #")
    print("-----------------------")
    print("\nwhat would you like to buy?")
    acceptable_buys = ['sword upgrade', 'mp upgrade', 'hp upgrade', 'magical stick', 'healing potion', 'a pet dragon']
    buy = input("> ")

    #-------- sword_upgrade ---------#
    if buy.lower() == 'sword upgrade':

        if myPlayer.money >= player_damage_money:
            print("\n######################################")
            print("#    thank you for buying my item    #")
            print("######################################")
            myPlayer.money -= player_damage_money
            myPlayer.sword_d += player_damage

        elif myPlayer.money < player_damage_money:
            print("\n#########################################################")
            print("#    you do not have enough money to buy this item!     #")
            print("#########################################################")

    #-------- mp_damage ----------#
    elif buy.lower() == 'mp upgrade':

        if myPlayer.money >= mp_damage_money:
            print("\n######################################")
            print("#    thank you for buying my item    #")
            print("######################################")
            myPlayer.money -= mp_damage_money
            myPlayer.mp += mp_damage
            myPlayer.mp_com += mp_damage

        elif myPlayer.money < mp_damage_money:
            print("\n#########################################################")
            print("#    you do not have enough money to buy this item!     #")
            print("#########################################################")

    #--------- hp_upgrade ---------#
    elif buy.lower() == 'hp upgrade':

        if myPlayer.money >= hp_upgrade_money:
            print("\n######################################")
            print("#    thank you for buying my item    #")
            print("######################################")
            myPlayer.money -= hp_upgrade_money
            myPlayer.hp += hp_upgrade
            myPlayer.healing_com += hp_upgrade

        elif myPlayer.money < hp_upgrade_money:
            print("\n#########################################################")
            print("#    you do not have enough money to buy this item!     #")
            print("#########################################################")

    #--------- magical stick -----------#
    elif buy.lower() == 'magical stick':

        if myPlayer.money >= magical_stick_money:
            print("\n######################################")
            print("#    thank you for buying my item    #")
            print("######################################")
            myPlayer.money -= magical_stick_money
            myPlayer.magical_stick += magical_stick

        elif myPlayer.money < magical_stick_money:
            print("\n#########################################################")
            print("#    you do not have enough money to buy this item!     #")
            print("#########################################################")

    #---------- healing potion ---------#
    elif buy.lower() == 'healing potion':

        if myPlayer.money >= healing_potion_money:
            print("\n######################################")
            print("#    thank you for buying my item    #")
            print("######################################")
            myPlayer.money -= healing_potion_money
            myPlayer.healing_potion += healing_potion

        elif myPlayer.money < healing_potion_money:
            print("\n#########################################################")
            print("#    you do not have enough money to buy this item!     #")
            print("#########################################################")

def readNews():
    value = random.randint(1, 3)
    print("\n##################")
    print("#    the news    #")
    print("##################")

    if value == 1:
        print("#              the new cargo update              #")
        print("#          the cargo update will feature         #")
        print("#    a new mission the player can choose from    #")
        print("#     the mission is about deliver the cargo     #")
        print("                   -coming soon-                  ")

    elif value == 2:
        print("#              the new magical book update             #")
        print("#         the magical book update will feature         #")
        print("#     some new magical things the player can equip     #")
        print("#    such as a new magical book and a magical staff    #")
        print("                      -coming soon-                     ")

    elif value == 3:
        print("#             the new dungeon update             #")
        print("#        the dungeon update will feature         #")
        print("#    a new mission the player can choose from    #")
        print("#    the mission is about exploring a dungeon    #")
        print("                   -coming soon-                  ")

def map():
    print("\n##################################")
    print("    where would you like to go    ")
    print("##################################")
    print("----------------------------------")
    print("                up                ")
    print("----------------------------------")
    print("               down               ")
    print("----------------------------------")
    print("               left               ")
    print("----------------------------------")
    print("               right              ")
    print("----------------------------------")
    print("\nwhere would you like to go?")
    acceptable_location = ['City', 'forest', 'home', 'town', 'village', 'bar']
    location = input("> ")

    #------------- 4e ----------------#
    if myPlayer.location_com == '4e':
        if location.lower() == 'up':
            myPlayer.location_com = '4d'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4f'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1e'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5e'
            location_com()

    #-------------- 4d -------------#
    elif myPlayer.location_com == '4d':
        if location.lower() == 'up':
            myPlayer.location_com = '4c'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4e'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1d'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5d'
            location_com()

    #----------- 4c ----------#
    elif myPlayer.location_com == '4c':
        if location.lower() == 'up':
            myPlayer.location_com = '4b'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4d'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1c'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5c'
            location_com()

    #----------- 4b ----------#
    elif myPlayer.location_com == '4b':
        if location.lower() == 'up':
            myPlayer.location_com = '4a'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4c'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1b'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5b'
            location_com()

    #----------- 4a ----------#
    elif myPlayer.location_com == '4a':
        if location.lower() == 'up':
            myPlayer.location_com = '4i'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4b'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1a'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5a'
            location_com()

    #----------- 4i ----------#
    elif myPlayer.location_com == '4i':
        if location.lower() == 'up':
            myPlayer.location_com = '4h'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4a'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1i'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5i'
            location_com()

    #----------- 4h ----------#
    elif myPlayer.location_com == '4h':
        if location.lower() == 'up':
            myPlayer.location_com = '4g'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4i'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1h'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5h'
            location_com()

    #----------- 4g ----------#
    elif myPlayer.location_com == '4g':
        if location.lower() == 'up':
            myPlayer.location_com = '4f'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4h'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1g'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5g'
            location_com()

    #----------- 4f ----------#
    elif myPlayer.location_com == '4f':
        if location.lower() == 'up':
            myPlayer.location_com = '4e'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '4g'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '1f'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '5f'
            location_com()

    #------------- 5e ----------------#
    elif myPlayer.location_com == '5e':
        if location.lower() == 'up':
            myPlayer.location_com = '5d'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5f'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4e'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6e'
            location_com()

    #------------- 5d ----------------#
    elif myPlayer.location_com == '5d':
        if location.lower() == 'up':
            myPlayer.location_com = '5c'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5e'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4d'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6d'
            location_com()

    #------------- 5c ----------------#
    elif myPlayer.location_com == '5c':
        if location.lower() == 'up':
            myPlayer.location_com = '5b'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5d'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4c'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6c'
            location_com()

    #------------- 5b ----------------#
    elif myPlayer.location_com == '5b':
        if location.lower() == 'up':
            myPlayer.location_com = '5a'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5c'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4b'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6b'
            location_com()

    #------------- 5a ----------------#
    elif myPlayer.location_com == '5a':
        if location.lower() == 'up':
            myPlayer.location_com = '5i'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5b'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4a'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6a'
            location_com()

    #------------- 5i ----------------#
    elif myPlayer.location_com == '5i':
        if location.lower() == 'up':
            myPlayer.location_com = '5h'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5a'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4i'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6i'
            location_com()

    #------------- 5h ----------------#
    elif myPlayer.location_com == '5h':
        if location.lower() == 'up':
            myPlayer.location_com = '5g'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5i'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4h'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6h'
            location_com()

    #------------- 5g ----------------#
    elif myPlayer.location_com == '5g':
        if location.lower() == 'up':
            myPlayer.location_com = '5f'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5h'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4g'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6g'
            location_com()

    #------------- 5f ----------------#
    elif myPlayer.location_com == '5f':
        if location.lower() == 'up':
            myPlayer.location_com = '5e'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '5g'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '4f'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '6f'
            location_com()

    #------------- 6e ----------------#
    elif myPlayer.location_com == '6e':
        if location.lower() == 'up':
            myPlayer.location_com = '6d'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6f'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5e'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7e'
            location_com()

    #------------- 6d ----------------#
    elif myPlayer.location_com == '6d':
        if location.lower() == 'up':
            myPlayer.location_com = '6c'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6e'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5d'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7d'
            location_com()

    #------------- 6c ----------------#
    elif myPlayer.location_com == '6c':
        if location.lower() == 'up':
            myPlayer.location_com = '6b'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6d'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5c'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7c'
            location_com()

    #------------- 6b ----------------#
    elif myPlayer.location_com == '6b':
        if location.lower() == 'up':
            myPlayer.location_com = '6a'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6c'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5b'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7b'
            location_com()

    #------------- 6a ----------------#
    elif myPlayer.location_com == '6a':
        if location.lower() == 'up':
            myPlayer.location_com = '6i'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6b'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5a'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7a'
            location_com()

    #------------- 6i ----------------#
    elif myPlayer.location_com == '6i':
        if location.lower() == 'up':
            myPlayer.location_com = '6h'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6a'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5i'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7i'
            location_com()

    #------------- 6h ----------------#
    elif myPlayer.location_com == '6h':
        if location.lower() == 'up':
            myPlayer.location_com = '6g'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6i'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5h'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7h'
            location_com()

    #------------- 6g ----------------#
    elif myPlayer.location_com == '6g':
        if location.lower() == 'up':
            myPlayer.location_com = '6f'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6h'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5g'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7g'
            location_com()

    #------------- 6f ----------------#
    elif myPlayer.location_com == '6f':
        if location.lower() == 'up':
            myPlayer.location_com = '6e'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '6g'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '5f'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '7f'
            location_com()

    #------------- 7e ----------------#
    elif myPlayer.location_com == '7e':
        if location.lower() == 'up':
            myPlayer.location_com = '7d'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7f'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6e'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8e'
            location_com()

    #------------- 7d ----------------#
    elif myPlayer.location_com == '7d':
        if location.lower() == 'up':
            myPlayer.location_com = '7c'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7e'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6d'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8d'
            location_com()

    #------------- 7c ----------------#
    elif myPlayer.location_com == '7c':
        if location.lower() == 'up':
            myPlayer.location_com = '7b'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7d'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6c'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8c'
            location_com()

    #------------- 7b ----------------#
    elif myPlayer.location_com == '7b':
        if location.lower() == 'up':
            myPlayer.location_com = '7a'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7c'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6b'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8b'
            location_com()

    #------------- 7a ----------------#
    elif myPlayer.location_com == '7a':
        if location.lower() == 'up':
            myPlayer.location_com = '7i'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7b'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6a'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8a'
            location_com()

    #------------- 7i ----------------#
    elif myPlayer.location_com == '7i':
        if location.lower() == 'up':
            myPlayer.location_com = '7h'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7a'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6i'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8i'
            location_com()

    #------------- 7h ----------------#
    elif myPlayer.location_com == '7h':
        if location.lower() == 'up':
            myPlayer.location_com = '7g'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7i'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6h'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8h'
            location_com()

    #------------- 7g ----------------#
    elif myPlayer.location_com == '7g':
        if location.lower() == 'up':
            myPlayer.location_com = '7f'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7h'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6g'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8g'
            location_com()

    #------------- 7f ----------------#
    elif myPlayer.location_com == '7f':
        if location.lower() == 'up':
            myPlayer.location_com = '7e'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '7g'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '6f'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '8f'
            location_com()

    #------------- 8e ----------------#
    elif myPlayer.location_com == '8e':
        if location.lower() == 'up':
            myPlayer.location_com = '8d'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8f'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7e'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1e'
            location_com()

    #------------- 8d ----------------#
    elif myPlayer.location_com == '8d':
        if location.lower() == 'up':
            myPlayer.location_com = '8c'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8e'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7d'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1d'
            location_com()

    #------------- 8c ----------------#
    elif myPlayer.location_com == '8c':
        if location.lower() == 'up':
            myPlayer.location_com = '8b'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8d'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7c'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1c'
            location_com()

    #------------- 8b ----------------#
    elif myPlayer.location_com == '8b':
        if location.lower() == 'up':
            myPlayer.location_com = '8a'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8c'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7b'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1b'
            location_com()

    #------------- 8a ----------------#
    elif myPlayer.location_com == '8a':
        if location.lower() == 'up':
            myPlayer.location_com = '8i'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8b'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7a'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1a'
            location_com()

    #------------- 8i ----------------#
    elif myPlayer.location_com == '8i':
        if location.lower() == 'up':
            myPlayer.location_com = '8h'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8a'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7i'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1i'
            location_com()

    #------------- 8h ----------------#
    elif myPlayer.location_com == '8h':
        if location.lower() == 'up':
            myPlayer.location_com = '8g'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8i'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7h'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1h'
            location_com()

    #------------- 8g ----------------#
    elif myPlayer.location_com == '8g':
        if location.lower() == 'up':
            myPlayer.location_com = '8f'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8h'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7g'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1g'
            location_com()

    #------------- 8f ----------------#
    elif myPlayer.location_com == '8f':
        if location.lower() == 'up':
            myPlayer.location_com = '8e'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '8g'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '7f'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '1f'
            location_com()

    #------------- 1e ----------------#
    elif myPlayer.location_com == '1e':
        if location.lower() == 'up':
            myPlayer.location_com = '1d'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1f'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8e'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4e'
            location_com()

    #------------- 1d ----------------#
    elif myPlayer.location_com == '1d':
        if location.lower() == 'up':
            myPlayer.location_com = '1c'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1e'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8d'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4d'
            location_com()

    #------------- 1c ----------------#
    elif myPlayer.location_com == '1c':
        if location.lower() == 'up':
            myPlayer.location_com = '1b'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1d'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8c'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4c'
            location_com()

    #------------- 1b ----------------#
    elif myPlayer.location_com == '1b':
        if location.lower() == 'up':
            myPlayer.location_com = '1a'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1c'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8b'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4b'
            location_com()

    #------------- 1a ----------------#
    elif myPlayer.location_com == '1a':
        if location.lower() == 'up':
            myPlayer.location_com = '1i'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1b'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8a'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4a'
            location_com()

    #------------- 1i ----------------#
    elif myPlayer.location_com == '1i':
        if location.lower() == 'up':
            myPlayer.location_com = '1h'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1a'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8i'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4i'
            location_com()

    #------------- 1h ----------------#
    elif myPlayer.location_com == '1h':
        if location.lower() == 'up':
            myPlayer.location_com = '1g'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1i'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8h'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4h'
            location_com()

    #------------- 1g ----------------#
    elif myPlayer.location_com == '1g':
        if location.lower() == 'up':
            myPlayer.location_com = '1f'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1h'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8g'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4g'
            location_com()

    #------------- 1f ----------------#
    elif myPlayer.location_com == '1f':
        if location.lower() == 'up':
            myPlayer.location_com = '1e'
            location_com()

        elif location.lower() == 'down':
            myPlayer.location_com = '1g'
            location_com()

        elif location.lower() == 'left':
            myPlayer.location_com = '8f'
            location_com()

        elif location.lower() == 'right':
            myPlayer.location_com = '4f'
            location_com()

def craft():
    print("\n--------------------------------------")
    print("#                stick               #")
    print(item.stick)
    print("--------------------------------------")
    print("#                stone               #")
    print(item.stone)
    print("--------------------------------------")
    print("#                wood                #")
    print(item.wood)
    print("--------------------------------------")
    print("#                iron                #")
    print(item.iron)
    print("--------------------------------------")
    print("######################################")
    print("#    what would you like to craft    #")
    print("######################################")
    craft = input("> ")

    if craft.lower() == 'club':
        if item.stick >= 2:
            print("\n##############################")
            print("#    You just made a club    #")
            print("##############################")
            itemCrafted.club = 'club'
        elif item.stick < 2:
            print("\n#########################################################")
            print("#    you do not have enough sticks to make this item    #")
            print("#########################################################")


#------ quest -------#
def quests():
    print("\n----------------------------------")
    print("#       you can use attack       #")
    print("----------------------------------")
    print("#    you can use magic learnt    #")
    print(myPlayer.magic_learnt)
    print("----------------------------------")
    print("\n" + "==========================")
    print("you're in combat what should you do?")
    quest = input("> ")

    if myPlayer.hp <= 0:
        myPlayer.game_over = True
        print("\n##################")
        print("#    game over   #")
        print("##################")

    elif myPlayer.monster_health <= 0:
        print("\n############################")
        print("#    you won the Battle    #")
        print("############################")
        value2 = random.randint(1, 2)

        #-------- you found a chest behind the monster ---------#
        if value2 == 1:
            print("\n##############################################")
            print("#    you found a chest behind the monster    #")
            print("##############################################")
            print("----------------------------------------------")
            print("#                    open                    #")
            print("----------------------------------------------")
            print("#                    leave                   #")
            print("----------------------------------------------")
            print("\n===================================")
            print("#    what would you like to do    #")
            chest = input("> ")

            #--------- open ----------#
            if chest.lower() == 'open':
                print("\n######################################################################################")
                print("#             you open the chest and you find a powerful magical staff               #")
                print("#              this magical item give you an advantage in every combat               #")
                print("#    this magical item is very effective if the player has chosen explosion Magic    #")
                print("######################################################################################")
                myPlayer.magical_staff += 1

        #-------- leave --------#
            elif chest.lower() == 'leave':
                print("\n######################################")
                print("#    you'll leave the chest alone    #")
                print("######################################")

        #------ you found a door behind the monster ---------#
        elif value2 == 2:
            print("\n#############################################")
            print("#    you found a door behind the monster    #")
            print("#############################################")
            print("----------------------------------------------")
            print("#                    open                    #")
            print("----------------------------------------------")
            print("#                    leave                   #")
            print("----------------------------------------------")
            print("\n===================================")
            print("#    what would you like to do    #")
            door = input("> ")

            if door.lower() == 'open':
                print("\n##################################################################################################")
                print("#                       you open the door and inside you find a big library                      #")
                print("#         in the library you find a table on the table there is a magical book that says         #")
                print("#    aWYgeW91IGNhbiByZWFkIHRoaXMgaXQgbWVhbnMgdGhhdCB5b3UgYXJlIGEgcG93ZXJmdWwgbWFnaWMgdXNlcg==    #")
                print("#                                  you can't read this text yet                                  #")
                print("##################################################################################################")
                myPlayer.magical_book += 1

            elif door.lower() == 'leave':
                print("\n#####################################")
                print("#    you'll leave the door alone    #")
                print("#####################################")

        #------- the reward ---------#
        myPlayer.monster_health = 550
        myPlayer.money += kill_quest_money_reward
        prompt()

    #----------- attack ----------#
    elif quest.lower() == 'attack':
        value = random.randint(1, 6)

        if value < 5:
            myPlayer.hp -= myPlayer.monster_damage
            print(myPlayer.hp)
            print(myPlayer.monster_health)

            if value > 2:
                myPlayer.monster_health -= myPlayer.sword_d
                quests()

            elif value <= 2:
                print("\n#############################")
                print("#    your attack failed     #")
                print("#############################")
                print(myPlayer.hp)
                print(myPlayer.monster_health)
                quests()

        elif value >= 5:
            print("\n################################")
            print("#    monster attack failed     #")
            print("################################")
            print(myPlayer.hp)
            print(myPlayer.monster_health)

            if value > 2:
                myPlayer.monster_health -= myPlayer.sword_d
                print(myPlayer.hp)
                print(myPlayer.monster_health)
                quests()

            elif value <= 2:
                print("\n#############################")
                print("#    your attack failed     #")
                print("#############################")
                print(myPlayer.hp)
                print(myPlayer.monster_health)
                quests()

    #---------- explosion magic -----------#
    elif quest.lower() == 'explosion magic':
        if myPlayer.magic_learnt == 'explosion magic':
            value = random.randint(1, 6)

            if myPlayer.mp < 60:
                print("\n#####################################################")
                print("#    you do not have enough mp to use this magic    #")
                print("#####################################################")
                quests()

            elif value < 5:
                myPlayer.hp -= myPlayer.monster_damage
                print(myPlayer.hp)
                print(myPlayer.monster_health)

                if value > 2:
                    myPlayer.monster_health -= mymagic.explosion_damage
                    myPlayer.mp -= 60
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()
                elif value <= 2:
                    print("\n#############################")
                    print("#    your attack failed     #")
                    print("#############################")
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()

            elif value >= 5:
                print("\n################################")
                print("#    monster attack failed     #")
                print("################################")
                print(myPlayer.hp)
                print(myPlayer.monster_health)

                if value > 2:
                    myPlayer.monster_health -= mymagic.explosion_damage
                    quests()
                elif value <= 2:
                    print("\n#############################")
                    print("#    your attack failed     #")
                    print("#############################")
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()


    #----------- healing magic ----------#
    elif quest.lower() == 'healing magic':
        if myPlayer.magic_learnt == 'healing magic':

            if myPlayer.mp < 20:
                print("\n#####################################################")
                print("#    you do not have enough mp to use this magic    #")
                print("#####################################################")
                quests()

            elif myPlayer.hp == myPlayer.healing_com:
                print("\n#####################################")
                print("#    you have already Max health    #")
                print("#####################################")
                quests()

            elif myPlayer.hp < myPlayer.healing_com:
                myPlayer.hp += mymagic.healing

                if myPlayer.hp > myPlayer.healing_com:
                    myPlayer.hp -= 20
                    quests()

    elif quest == 'healing':
            if myPlayer.healing_potion <= 0:
                print("\n###########################################################")
                print("#    you do not have enough healing potion to use this    #")
                print("###########################################################")
                quests()

            elif myPlayer.hp == myPlayer.healing_com:
                print("\n#####################################")
                print("#    you have already Max health    #")
                print("#####################################")
                quests()

            elif myPlayer.hp < myPlayer.healing_com:
                myPlayer.hp += mymagic.healing

                if myPlayer.hp > myPlayer.healing_com:
                    myPlayer.hp -= 20
                    quests()

                else:
                    quests()

    elif quest.lower() == 'fire magic':
        if myPlayer.magic_learnt == 'fire magic':
            value = random.randint(1, 6)

            if myPlayer.mp < 20:
                print("\n#####################################################")
                print("#    you do not have enough mp to use this magic    #")
                print("#####################################################")
                quests()

            elif value < 5:
                myPlayer.hp -= myPlayer.monster_damage
                print(myPlayer.hp)
                print(myPlayer.monster_health)

                if value > 2:
                    myPlayer.monster_health -= mymagic.fire_damage
                    myPlayer.mp -= 20
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()
                elif value <= 2:
                    print("\n#############################")
                    print("#    your attack failed     #")
                    print("#############################")
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()

            elif value >= 5:
                print("\n################################")
                print("#    monster attack failed     #")
                print("################################")
                print(myPlayer.hp)
                print(myPlayer.monster_health)

                if value > 2:
                    myPlayer.monster_health -= mymagic.fire_damage
                    quests()
                elif value <= 2:
                    print("\n#############################")
                    print("#    your attack failed     #")
                    print("#############################")
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()

    elif quest.lower() == 'water magic':
        if myPlayer.magic_learnt == 'water magic':
            value = random.randint(1, 6)

            if myPlayer.mp < 20:
                print("\n#####################################################")
                print("#    you do not have enough mp to use this magic    #")
                print("#####################################################")
                quests()

            elif value < 5:
                myPlayer.hp -= myPlayer.monster_damage
                print(myPlayer.hp)
                print(myPlayer.monster_health)

                if value > 2:
                    myPlayer.monster_health -= mymagic.water_damage
                    myPlayer.mp -= 5
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()
                elif value <= 2:
                    print("\n#############################")
                    print("#    your attack failed     #")
                    print("#############################")
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()

            elif value >= 5:
                print("\n################################")
                print("#    monster attack failed     #")
                print("################################")
                print(myPlayer.hp)
                print(myPlayer.monster_health)

                if value > 2:
                    myPlayer.monster_health -= mymagic.water_damage
                    quests()
                elif value <= 2:
                    print("\n#############################")
                    print("#    your attack failed     #")
                    print("#############################")
                    print(myPlayer.hp)
                    print(myPlayer.monster_health)
                    quests()

    else:
        if myPlayer.hp > 0:
            quests()

#-------- location com -------#
def location_com():

    #----------- 4e ----------#
    if myPlayer.location_com == '4e':
        print("\n###################")
        print("#    you go home  #")
        print("###################")

    elif myPlayer.location_com == '4d':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '4c':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '4b':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '4a':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '4i':
        print("\n##########################")
        print("#    you go to the town  #")
        print("##########################")

    elif myPlayer.location_com == '4h':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '4g':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '4f':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

        #--------- 5e --------#
    elif myPlayer.location_com == '5e':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '5d':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '5c':
        print("\n##########################")
        print("#    you go to the city  #")
        print("##########################")

    elif myPlayer.location_com == '5b':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '5a':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '5i':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '5h':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '5g':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '5f':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '5d':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

        #---------- 6e -----------#
    elif myPlayer.location_com == '6e':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '6d':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '6c':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '6b':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '6a':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '6i':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '6h':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '6g':
        print("\n##########################")
        print("#    you go to the city  #")
        print("##########################")

    elif myPlayer.location_com == '6f':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

        #---------- 7e ----------#
    elif myPlayer.location_com == '7e':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '7d':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '7c':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '7b':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '7a':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '7i':
        print("\n##########################")
        print("#    you go to the city  #")
        print("##########################")

    elif myPlayer.location_com == '7h':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '7g':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '7f':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    #---------- 8e ----------#
    elif myPlayer.location_com == '8e':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '8d':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '8c':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '8b':
        print("\n##########################")
        print("#    you go to the town  #")
        print("##########################")

    elif myPlayer.location_com == '8a':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '8i':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '8h':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '8g':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '8f':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '1e':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '1d':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '1c':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '1b':
        print("\n#############################")
        print("#    you go to the Village  #")
        print("#############################")

    elif myPlayer.location_com == '1a':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '1i':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '1h':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '1g':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

    elif myPlayer.location_com == '1f':
        print("\n############################")
        print("#    you go to the forest  #")
        print("############################")

#---------- start menu -----------#
def start_game():
    return

def main_game_loop():
    while myPlayer.game_over == False:
        prompt()

def setup_game():
    question1 = "Hello, what's your name?\n"
    for charater in question1:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(0.05)

    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "what role do you want to play\n"
    question2addea = "you can play as a warrior, mage, or priest\n"

    for charater in question2:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(0.05)

    for charater in question2addea:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(0.01)

    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("you are a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("you are a " + player_job + "!\n")

    if myPlayer.job == 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 20
        myPlayer.mp_com = 20
        myPlayer.sword_d = 140
        myPlayer.money = 150
        myPlayer.healing_com = 120

    elif myPlayer.job == 'mage':
        myPlayer.hp = 40
        myPlayer.mp = 140
        myPlayer.mp_com = 140
        myPlayer.sword_d = 10
        myPlayer.money = 150
        mymagic.magical_points = 5
        myPlayer.healing_com = 40

    elif myPlayer.job == 'priest':
        myPlayer.hp = 60
        myPlayer.mp = 60
        myPlayer.mp_com = 60
        myPlayer.sword_d = 60
        myPlayer.money = 300
        myPlayer.healing_com = 60

    print("##########################")
    print("#    let's start now!    #")
    print("##########################")
    prompt()

title_screen()
setup_game()
main_game_loop()
title_screen_selections()
