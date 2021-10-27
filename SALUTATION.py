from tkinter import *

fen = Tk ()

fram = Frame (fen, relief=RIDGE, borderwidth=2)
fram.pack (fill=BOTH, expand=1)

label = Label (fram, text = "Salutation les monde")
label.pack (fill=X, expand=1)

btn = Button (fram, text="Exit", command=fen.destroy)
btn.pack (side=BOTTOM)
fen.mainloop()