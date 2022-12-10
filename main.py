import pyautogui
import tkinter as tk

root = tk.Tk()

win_width = 400
win_height = 500
clicks = 0

bg = tk.Canvas(root, width=win_width, height=win_width)
bg.pack()

#Make buttons
button1 = tk.Button(text="CLICK ME", width=5, height=5, font=("Helvetica", 30), background="lime", padx=400, pady=100)
clickCount = tk.Label(text=str(clicks) + " Clicks")
clickCount.place(x=50, y=100)

bg.create_window(win_width, win_width, window=button1)

root.mainloop()