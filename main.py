import tkinter as tk
from tkinter import messagebox
import time

class GUI:

  def __init__(self):
    #Create window
    self.root = tk.Tk()
    self.root.geometry("500x300")#Resolution
    self.root.title("CPS")#App Title
    self.root.configure(bg="#18122B")#Background color

    #Vars
    self.clicks = 0
    self.timer = 0
    self.score = 0
    self.CPSOn = False

    #Texts
    self.title = tk.Label(self.root, text="Clicks-per-Second", font=('Comic Sans MS', 20), background="#BFACE2", foreground="#18122B", borderwidth=5)
    self.title.pack(pady=15)

    self.statsLabel = tk.Label(self.root, text=f"Clicks/s: {self.clicks} Score: {self.score} Timer: {self.timer}", font=('Comic Sans MS', 14), background="#BFACE2", foreground="#18122B", borderwidth=5)
    self.statsLabel.pack(pady=5)

    #Set columns for buttons in one row
    self.timerButtonFrame = tk.Frame(self.root)
    self.timerButtonFrame.columnconfigure(0, weight=1)
    self.timerButtonFrame.columnconfigure(1, weight=1)
    self.timerButtonFrame.columnconfigure(2, weight=1)
    self.timerButtonFrame.columnconfigure(3, weight=1)

    #Timer Buttons
    self.oneSecBtn = tk.Button(self.timerButtonFrame, text="1 Second", font=('Comic Sans MS', 10), background="#645CBB", foreground="#18122B", activebackground="#A084DC",command=lambda:self.changeTimer(1))
    self.oneSecBtn.grid(row=0, column=0, sticky=tk.W+tk.E)

    self.fiveSecBtn = tk.Button(self.timerButtonFrame, text="5 Seconds", font=('Comic Sans MS', 10), background="#645CBB", foreground="#18122B", activebackground="#A084DC",command=lambda:self.changeTimer(5))
    self.fiveSecBtn.grid(row=0, column=1, sticky=tk.W+tk.E)

    self.tenSecBtn = tk.Button(self.timerButtonFrame, text="10 Seconds", font=('Comic Sans MS', 10), background="#645CBB", foreground="#18122B", activebackground="#A084DC",command=lambda:self.changeTimer(10))
    self.tenSecBtn.grid(row=0, column=2, sticky=tk.W+tk.E)

    self.fifthTeenSecBtn = tk.Button(self.timerButtonFrame, text="15 Seconds", font=('Comic Sans MS', 10), background="#645CBB", foreground="#18122B", activebackground="#A084DC",command=lambda:self.changeTimer(15))
    self.fifthTeenSecBtn.grid(row=0, column=3, sticky=tk.W+tk.E)

    self.timerButtonFrame.pack(fill='x', padx=10, pady=10)

    #Click button
    self.clickButton = tk.Button(self.root, text="Click to Start", font=("Comic Sans MS", 16), background="#BFACE2", foreground="#18122B", activebackground="#674188",command=self.updateStats)
    self.clickButton.pack(pady=20)

    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    self.root.mainloop()

  def updateStats(self):
    if self.timer >= 0:
      self.CPSOn = True
      self.score += 1
      self.statsLabel.configure(text=f"Clicks/s: {self.clicks} Score: {self.score} Timer: {self.timer}")
      self.calculateCPS()
    elif self.timer == 0:
      self.CPSOn = False

  #Change Timer Time
  def changeTimer(self, time):
    self.timer = time
    self.statsLabel.configure(text=f"Clicks/s: {self.clicks} Score: {self.score} Timer: {self.timer}")

  def updateTimer(self):
    if self.CPSOn == True:
      self.timer -= 1
      time.sleep(1)
      self.root.after(1000, self.updateTimer)#Call update every second

  def calculateCPS(self):
    pass

  def showResult(self):
    messagebox.showinfo(title="Results",message=f"Your average Clicks Per Seconds are {self.clicks}")

  #Prevent accidental closing
  def on_closing(self):
    if messagebox.askyesno(title="Quit?", message="Are you sure you wanna quit now ?"):
      self.root.destroy()

if __name__ == "__main__":
  app = GUI()
  app.mainloop()
