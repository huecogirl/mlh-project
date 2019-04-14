
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw
import digitRec




class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='compute', command=self.get_digit)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='clear', command=self.clear)
        self.brush_button.grid(row=0, column=1)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)


    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = 100
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=100, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def get_digit(self):
        self.c.postscript(file="digit.ps", colormode="color")
        img = Image.open("digit.ps")
        img.save("digit.png", "png")
        self.filename = "digit.png"
        digitRec.get_digit(self.filename)
        self.c.delete("all")
    def clear(self):
        self.c.delete("all")

if __name__ == '__main__':
    Paint()
