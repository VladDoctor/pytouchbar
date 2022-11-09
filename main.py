from tkinter import *
import PyTouchBar
import random

def game(map, speed):
    global jump
    root = Tk()
    PyTouchBar.prepare_tk_windows(root)
    buttons = [0 for b in range(len(map))]

    def jumping(button):
        global jump
        jump += 1

    for chunk in range(len(map)):
        if map[chunk] == 1:
            buttons[chunk] = PyTouchBar.TouchBarItems.Button(image='trex.png', color=(PyTouchBar.Color.black), action=jumping)
        elif map[chunk] == 0:
            buttons[chunk] = PyTouchBar.TouchBarItems.Button(image='platform.png', color=(PyTouchBar.Color.black))
        elif map[chunk] == -1:
            buttons[chunk] = PyTouchBar.TouchBarItems.Button(image='cactus.png', color=(PyTouchBar.Color.black))
        elif map[chunk] == -2:
            buttons[chunk] = PyTouchBar.TouchBarItems.Button(image='loss.png', color=(PyTouchBar.Color.black))
        elif map[chunk] == 2:
            buttons[chunk] = PyTouchBar.TouchBarItems.Button(image='lucky.png', color=(PyTouchBar.Color.black))

    PyTouchBar.set_touchbar(buttons)


    root.after(1200 - speed * 100, root.destroy)
    root.mainloop()

def prepare():
    global root
    global speed
    root = Tk()

    def set_speed(stepper):
        global speed
        speed = int(stepper.value)

    def finish(points):
        root = Tk()
        label = PyTouchBar.TouchBarItems.Label(text=f'Упс:( Вы набрали: {points}')
        PyTouchBar.set_touchbar([label])
        PyTouchBar.prepare_tk_windows(root)
        root.mainloop()

    def start(button):
        global jump
        global speed
        speed = 2
        jump = 0
        map = [[1,0], 0, 0, -1, 0, -1, 0]
        points = 0

        root.destroy()
        zero_chunk = 1

        while True:
            map[0] = [1,map[1]]
            if jump == 0 and map[0] == [1,-1]:
                zero_chunk = -2
            elif jump >= 1 and map[0] == [1,0]:
                jump = 0
                zero_chunk = 1
            elif jump == 1 and map[0] == [1,-1]:
                zero_chunk = 2
                points += 1

            new_map = map[1:]
            new_map[0] = zero_chunk
            if map[-1] == 0:
                new_map.append(random.choice([0, -1]))
            else:
                new_map.append(0)
            print(map, new_map)
            map = new_map
            game(new_map, speed)

            if zero_chunk == -2:
                finish(points)

    speed_p = PyTouchBar.TouchBarItems.Stepper(min=2, max=8, action=set_speed)
    starter = PyTouchBar.TouchBarItems.Button(title='играть', color=(PyTouchBar.Color.black), action=start)

    PyTouchBar.set_touchbar([speed_p, starter])
    PyTouchBar.prepare_tk_windows(root)

    root.mainloop()

prepare()
