import tkinter as tk
from tkinter import filedialog, Text
import os

# making root
root = tk.Tk()
apps = []
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        temAss = tempApps.split(',')
        print()

def addApp():
    for widgets in frame.winfo_children():
        widgets.destroy()

    filename = filedialog.askopenfilename(initialdir='/',title = 'select file',
                                          filetypes = (("executetables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame ,text = app,bg = "gray")
        label.pack()
def runapps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)
openfile = tk.Button(root, text = "Open file", padx = 10, pady = 5, fg = "white", bg = "#263D42", command = addApp)
openfile.pack()

runApps  = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg = "white", bg = "#263D42", command = runapps)
runApps.pack()


root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app+',')
