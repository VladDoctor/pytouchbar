import PyTouchBar
from tkinter import *

root = Tk()
PyTouchBar.prepare_tk_windows(root)

def event(button):
    print('Hello world')

button = PyTouchBar.TouchBarItems.Button(title='Hello world', color=(0.1,0.2,0.3), action=event) #если убрать color, то норм
PyTouchBar.set_touchbar([button])

root.mainloop()
