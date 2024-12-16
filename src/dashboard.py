from tkinter import *

raiz = Tk()
raiz.title("PCT")
# raiz.resizable(True, False)
raiz.iconbitmap("./visuals/icon.ico")
raiz.geometry("850x650")
raiz.config(bg="#ececec")

miFrame=Frame()
miFrame.pack(side="top")
miFrame.config(bg="#0052a6")
miFrame.config(width="850", height="85")



raiz.mainloop()