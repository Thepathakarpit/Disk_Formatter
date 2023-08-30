import pyautogui as auto
import time


auto.hotkey("win","d") #takes to homescreen by minimizing all windows
auto.hotkey("win","r") #opens Run
auto.write("cmd") #writes cmd
auto.press("enter") #presses enter
time.sleep(2)#waits 2 seconds since it takes time to boot cmd sometimes.
auto.write("diskpart")
auto.press("enter")
time.sleep(1)
auto.write("list disk")
auto.press("enter")
#Below command displays a message.
auto.alert("GO BACK TO INITIAL WINDOW (where you ran this program) and Enter number of Disk you want to Erase and Format from the list on the screen")
n=input("Enter the Number of Disk"+"\n")

auto.hotkey("win","d")
auto.hotkey("win","r")
auto.write("cmd") 
auto.press("enter") 
time.sleep(2)
auto.write("diskpart")
auto.press("enter")
time.sleep(1)
auto.write("list disk")
auto.press("enter")
auto.write("select disk "+n)
auto.press("enter")
auto.write("clean")
auto.press("enter")
auto.write("create partition primary")
auto.press("enter")
auto.write("format fs = ntfs")
auto.press("enter")
auto.write("assign")
auto.press("enter")
