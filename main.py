# Hello! This little game is created by Pau Cava.
# It's a little text game inspired in the old ones
# of this genere.
# 
# Hope you enjoy and try to not get trapped in the cave!
# Pau.


                    ##################################################
                    #                    MODULES                     #
                    ##################################################

import os
import time
from texts import *
from colorama import Fore

                    ##################################################
                    #                 CHARACTER STATS                #
                    ##################################################

def show_usr_estate(stage, alive, life_points):
    print(Fore.LIGHTYELLOW_EX + "- Current user status -> stage:",
          stage, ",life points:", life_points, ", alive:", alive)


def show_axel_estate(stage, alive, life_points):
    print(Fore.LIGHTYELLOW_EX + "- Axel current status -> stage:",
          stage, ",life points:", life_points, ", alive:", alive)


def show_chuck_estate(stage, alive, life_points):
    print(Fore.LIGHTYELLOW_EX + "- Chuck current status -> stage:",
          stage, ",life points:", life_points, ", alive:", alive)

usr_alive = True
usr_life_points = 100

chuck_alive = True
chuck_life_points = 100

axel_alive = True
axel_life_points = 100


                   ##################################################
                   #                   MAIN GAME                    #
                   ##################################################



print("THE CLIFF ------------------------------------------------------------------- 0.0.1")

usr_name = input("-Welcom user, enter your nickname: ")
print("-Hello,",usr_name," your adventure is ready to begin. ")

time.sleep(1.5)

#Little space
os.system("clear")
time.sleep(3)





                    ##################################################
                    #        DIALGUE1 - SCENE1 - CAVE ENTRANCE       #
                    ##################################################
   
                    #INFO: All characters alive yet, this is a prologue

#Print fisrt text

print(text)

time.sleep(4)

os.system("clear")


#First dialogue

print(Fore.RED + "\n𝘾𝙝𝙪𝙘𝙠: I see it! The entrance is there!")
time.sleep(2)
print(Fore.CYAN + usr_name + ": Should we enter? ")
time.sleep(1)
print(Fore.GREEN + "𝘼𝙭𝙚𝙡: Guys... What if we get trapped in the cave?")

decision1 = input(Fore.WHITE + "- Will they enter? y/n ")

#First decision

if decision1 == "y" or decision1 == "Y":
    print(Fore.LIGHTYELLOW_EX + "- They have entered the cave, now there's no turning back... ")
    

    time.sleep(2)
    os.system("clear")

    print(Fore.RED + "𝘾𝙝𝙪𝙘𝙠: * Turns on the lantern *")

    print(Fore.GREEN + "𝘼𝙭𝙚𝙡: I'm not sure doing this is a good idea...")

    #Enter / not
    decision2 = input(Fore.WHITE + "- Continue with the expedition or leave the cave as Axel says? y/n ")

    if decision2 == "y" or decision2 == "Y":
        print(Fore.LIGHTYELLOW_EX + "- They go inner in the cave, the walls are slowly getting more small... ")
        
        #Show state y / n
        decision3 = input("- Do you want to see your estate before continuing the adventure? y/n ")
        
        if decision3 == "y" or decision3 == "Y":
            show_usr_estate(1, usr_alive, usr_life_points)
        
        else:
            pass
        
        time.sleep(2)

        os.system("clear")

        print(Fore.CYAN + usr_name + ": Is it just me or the walls are getting smaller? ")
        
        time.sleep(1)

        print(Fore.GREEN + "𝘼𝙭𝙚𝙡: No, I see it too.")

        time.sleep(0.4)

        print(Fore.RED + "𝘾𝙝𝙪𝙘𝙠: Don't be scared now! We are almost arriving to the subterranean lake!")

        time.sleep(4)
    
    else:
        os.system("clear")
        print(Fore.RED + "----------------------------- YOU HAVE REACHED AN END -----------------------------")
        show_usr_estate(1, usr_alive, usr_life_points)


                    ##################################################
                    #      DIALGUE2 - SCENE1 - SUBTERRANEAN LAKE     #
                    ##################################################
    
    #Clear the terminal for more clean view.
    os.system("clear")

    print(text2)

    time.sleep(4)
    
    os.system("clear")
    print(Fore.RED + "𝘾𝙝𝙪𝙘𝙠: There is it! The lake is there!")
     
    time.sleep(2)

    print(Fore.GREEN + "𝘼𝙭𝙚𝙡: I'm to scared Chuck, I think I'm going home")

    time.sleep(2)

    print(Fore.CYAN + usr_name + ": Yes I'll think I go with you Axel...")

    time.sleep(2)

    print(Fore.RED + "𝘼𝙭𝙚𝙡: Oh, really? Well fuck you, I'm going to do this by myself! ")

    time.sleep(3)


    print(Fore.LIGHTYELLOW_EX + "- You and Axel go to the entrance but you both fall off a cliff that wan't there before...\n")

    #Rest life points

    axel_life_points = axel_life_points - 50
    
    usr_life_points = usr_life_points - 50

    show_usr_estate(2, usr_alive, usr_life_points)
    
    time.sleep(2)

    show_axel_estate(2, axel_alive, axel_life_points)
    

                    ##################################################
                    #          DIALGUE1 - SCENE2 - THE CLIFF         #
                    ##################################################
    time.sleep(5)

    os.system("clear")

    print(Fore.CYAN + usr_name + ": Axel? Axel where are you, I can't see anithing...")

    time.sleep(2)

    print(Fore.GREEN + "𝘼𝙭𝙚𝙡:", usr_name, "! I'm here!")
    
    time.sleep(1.4)

    print(Fore.CYAN + usr_name + ": * Turns on it's lanter * Oh there are you! ")

    time.sleep(3)

    print(Fore.BLACK + " 𝙖 𝙨𝙩𝙧𝙖𝙣𝙜𝙚 𝙛𝙞𝙜𝙪𝙧𝙚 𝙬𝙖𝙡𝙠𝙨 𝙥𝙧𝙤𝙥𝙚𝙧𝙡𝙮 𝙩𝙤 𝙩𝙝𝙚𝙢...")

    time.sleep(5)

    print(Fore.BLACK + "ՏԵɾɑղցҽ ʍɑղ: There had past a lot of years since I saw a human...")

    time.sleep(2)

    print(Fore.BLACK + "ՏԵɾɑղցҽ ʍɑղ: Why are you here? ")

    time.sleep(2)

    print(Fore.GREEN + "𝘼𝙭𝙚𝙡: * scared * We fell off a cliff... ")

    time.sleep(1.3)

    print(Fore.CYAN + usr_name + ": ")

                    ##################################################
                    #                       END                      #
                    ##################################################

#They don't enter the cave
else:
    os.system("clear")
    print(Fore.RED + "----------------------------- YOU HAVE REACHED AN END -----------------------------")
    show_usr_estate(1, usr_alive, usr_life_points)
