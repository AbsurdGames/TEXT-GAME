# Hello! This little game is created by Pau Cava.
# It's a little text game inspired in the old ones
# of this genere.
# 
# Hope you enjoy!
# Pau.


                    ##################################################
                    #                    MODULES                     #
                    ##################################################


import os
import time
from texts import *
from colorama import Fore

                    ##################################################
                    #                   MAIN GAME                    #
                    ##################################################


def show_estate(stage, alive):
    print(Fore.LIGHTYELLOW_EX + "- Current status -> stage:",stage,",alive:", alive) 





print("TEXT ADVENTURE ------------------------------------------------------------------- 0.0.1")

usr_name = input("-Welcom user, enter your nickname: ")
print("-Hello,",usr_name," your adventure is ready to begin. ")

time.sleep(0.8)

#Little space
os.system("clear")
time.sleep(3)



                    ##################################################
                    #        DIALGUE1 - SCENE1 - CAVE ENTRANCE       #
                    ##################################################
                    
                    #INFO: All characters alive yet.

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
            show_estate(1, True)
        
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
        show_estate(1, True)


                    ##################################################
                    #      DIALGUE2 - SCENE1 - SUBTERRANEAN LAKE     #
                    ##################################################
    

    os.system("clear")

    print(text2)




                    ##################################################
                    #                       END                      #
                    ##################################################

else:
    os.system("clear")
    print(Fore.RED + "----------------------------- YOU HAVE REACHED AN END -----------------------------")
    show_estate(1, True)