import pyautogui
import time
import keyboard
import random

def main():
    while True:
        try:
            milli1 = int(input("Enter the minimum delay in milliseconds:\n"))
            break
        except:
            print("The input must be an integer.")

    while True:
        try:
            milli2 = int(input("Enter the maximum delay in milliseconds:\n"))
            break
        except:
            print("The input must be an integer.")
    
    print(f"The autoclicker delay is between {milli1} and {milli2} milliseconds.")
    while True:
        try:
            delays = str(input("Do you wish to see the delays of your clicks? (Y/N):\n"))
            if delays == "Y":
                break
            elif delays == "y":
                break
            elif delays == "N":
                break
            elif delays == "n":
                break
            else:
                print("You must enter a valid command (Y/N)")
        except:
            print("You must enter a valid command (Y/N)")
    print("Press enter to start")
    print("Hold 'p' to pause, hold 'c' to continue, hold 's' to stop.")
    input()
    while True:
        timer = (random.randint(milli1, milli2) / 1000)
        time.sleep(timer)
        if delays == "y":
            print(timer)
        elif delays == "Y":
            print(timer)
        pyautogui.click()
        if keyboard.is_pressed("p"):
            while True:
                if keyboard.is_pressed("c"):
                    break
        elif keyboard.is_pressed("s"):
            break
main()
