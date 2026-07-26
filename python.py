import tkinter as tk
import webbrowser

root = tk.Tk()

def command():
  webbrowser.open("https://www.youtube.com")

l1 = tk.Label(root, text="Click The Button")
l1.pack()

b1 = tk.Button(root, text="Click Me",command=command)
b1.pack()

root.mainloop()
