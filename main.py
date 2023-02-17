import tkinter as tk
from tkinter import messagebox
import time

#Create window
root = tk.Tk()
root.geometry("500x300")#Resolution
root.title("CPS")#App Title
root.configure(bg="#18122B")#Background color

#Vars
clicks = 0
timer = 0
score = 0
CPSOn = False

#Functions
def updateStats():
  global CPSOn, timer, score, clicks, statsLabel
  if timer > 0:
    CPSOn = True
    score += 1
    print(f"{timer} {CPSOn}")
    statsLabel.configure(text=f"Clicks/s: {clicks} Score: {score} Timer: {timer}")
    calculateCPS()
  elif timer == 0:
    CPSOn = False

#Change Timer Time
def changeTimer(time):
  global clicks, score, timer, statsLabel
  timer = time
  statsLabel.configure(text=f"Clicks/s: {clicks} Score: {score} Timer: {timer}")

def updateTimer():
  global CPSOn, timer, root
  root.after(1000, updateTimer)#Call update every second
  if CPSOn == True:
    timer -= 1
    print(timer)
    time.sleep(1)

def calculateCPS():
  pass

def showResult():
  global clicks
  messagebox.showinfo(title="Results",message=f"Your average Clicks Per Seconds are {clicks}")

#Prevent accidental closing
def on_closing():
  if messagebox.askyesno(title="Quit?", message="Are you sure you wanna quit now ?"):
    root.destroy()

#Texts
title = tk.Label(root, text="Clicks-per-Second", font=('Comic Sans MS', 20), background="#BFACE2", foreground="#18122B", borderwidth=5)
title.pack(pady=15)

statsLabel = tk.Label(root, text=f"Clicks/s: {clicks} Score: {score} Timer: {timer}", font=('Comic Sans MS', 14), background="#BFACE2", foreground="#18122B", borderwidth=5)
statsLabel.pack(pady=5)

#Set columns for buttons in one row
timerButtonFrame = tk.Frame(root)
timerButtonFrame.columnconfigure(0, weight=1)
timerButtonFrame.columnconfigure(1, weight=1)
timerButtonFrame.columnconfigure(2, weight=1)
timerButtonFrame.columnconfigure(3, weight=1)

#Timer Buttons
oneSecBtn = tk.Button(timerButtonFrame, text="1 Second", font=('Comic Sans MS', 10), background="#645CBB", foreground="#18122B", activebackground="#A084DC",command=lambda:changeTimer(1))
oneSecBtn.grid(row=0, column=0, sticky=tk.W+tk.E)

fiveSecBtn = tk.Button(timerButtonFrame, text="5 Seconds", font=('Comic Sans MS', 10), background="#645CBB", foreground="#18122B", activebackground="#A084DC",command=lambda:changeTimer(5))
fiveSecBtn.grid(row=0, column=1, sticky=tk.W+tk.E)

tenSecBtn = tk.Button(timerButtonFrame, text="10 Seconds", font=('Comic Sans MS', 10), background="#645CBB", foreground="#18122B", activebackground="#A084DC",command=lambda:changeTimer(10))
tenSecBtn.grid(row=0, column=2, sticky=tk.W+tk.E)

fifthTeenSecBtn = tk.Button(timerButtonFrame, text="15 Seconds", font=('Comic Sans MS', 10), background="#645CBB", foreground="#18122B", activebackground="#A084DC",command=lambda:changeTimer(15))
fifthTeenSecBtn.grid(row=0, column=3, sticky=tk.W+tk.E)

timerButtonFrame.pack(fill='x', padx=10, pady=10)

#Click button
clickButton = tk.Button(root, text="Click to Start", font=("Comic Sans MS", 16), background="#BFACE2", foreground="#18122B", activebackground="#674188",command=updateStats)
clickButton.pack(pady=20)

updateTimer()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
