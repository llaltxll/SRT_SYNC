import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Open file", "show your most fat place and press the pines")

B = Tkinter.Button(top, text ="Michael", command = helloCallBack)

B.pack()
top.mainloop()
