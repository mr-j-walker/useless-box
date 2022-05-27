from time import sleep
import os, random

def loadingAnimation(interval = 0):
    if interval > 10:
        clear()
        return
    else:
        clear(random.random())
        print("".join(["." for i in range(interval)]))
        loadingAnimation(interval + 1)

def clear(interval = 0):
    sleep(interval)
    os.system('cls' if os.name == 'nt' else 'clear')

def toggleSwitch(switch):
    if not switch:
        loadingAnimation(10)
    else:
        loadingAnimation()
    switch = not switch
    print("The switch has been flipped " + ("off" if not switch else "on"))
    sleep(1)
    return switch

def main():
    switch = False
    while True:
        clear()
        print("The switch is " + ("off" if not switch else "on"))
        choice = input("\nWould you like to turn it on? (y/n)\n").upper()
        if choice == "Y":
            switch = toggleSwitch(switch)
        elif choice == "N":
            return
        
        if switch:
            switch = toggleSwitch(switch)
    

if __name__ == "__main__":
    main()