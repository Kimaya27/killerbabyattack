#Attack Of The Killer Baby

# Imports
import pygame

#Initialize game engine
pygame.init()

# Background
start = (0, 150, 200) 
end = (255, 200, 75)

def start():
    print("Welcome To ATTACK OF THE KILLER BABY")

def end():
    print("Goodbye. Thanks for playing!")

def confirm(question):
    while True:
        answer = input(question + "(y/n)")
        if answer in ("y" , "yes"):
            return True
        elif answer in ("n" , "no"):
            return False

def play():
    num_babysitters = 3
    baby_is_alive = True

    print("Look, a precious litte baby!")

    while baby_is_alive and num_babysitters > 0:
        use_poison = confirm("Shall we use the toxic poison?")

        if use_poison:
            print("5..4..3..2..1..")
            print("POOF")
            print("The baby has vanished!")
            baby_is_alive = False
        else:
            num_babysitters -=1
            print("Oh, no! The baby just killed one of the babysitters!")
            print("Only" + str(num_babysitters) + "remain")
    if num_babysitters > 0:
        print("The killer baby has been defeated. You win!")
    else:
        print("All of the babysitters have been defeated. You lose!")

start()

playing = True

while playing:
    play()
    print("Would you like to play again?")

end()
