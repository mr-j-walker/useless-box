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
    if interval == -1:
       interval = random.randint(1,5)
    sleep(interval)
    os.system('cls' if os.name == 'nt' else 'clear')

def toggleSwitch(switch):
    if not switch:
        loadingAnimation()
    else:
        loadingAnimation()
    switch = not switch
    print("\nThe switch has been flipped " + ("off" if not switch else "on"))
    sleep(1)
    return switch

def main():
    switch = False
    while True:
        clear()
        print("\nThe switch is " + ("off" if not switch else "on"))
        choice = input("\nWould you like to turn it on? (y/n)\n").upper()
        if choice == "Y":
            switch = toggleSwitch(switch)
        elif choice == "N":
            return
        else:
            loadingAnimation()
        
        if switch:
            switch = toggleSwitch(switch)
    

if __name__ == "__main__":
    main()