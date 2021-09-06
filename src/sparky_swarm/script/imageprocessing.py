
from PIL import Image
import tkinter as tk
import math
image = Image.open('/home/navid/Pictures/gear.jpeg')

class App:
    def __init__(self):
        self.root=tk.Tk()
        self.c=tk.Canvas(self.root, height=400, width=400, bg="white")
        
        self.c.pack()

        self.c.bind('<Configure>', self.create_grids)
        self.c.bind('<ButtonPress>',self.clicked)

      

    def create_grids(self,event=None):
        w = self.c.winfo_width() 
        h = self.c.winfo_height() 
        self.c.delete('grid_line') 

        # Creates all vertical lines at intevals of 100
        for i in range(0, w, 40):
            self.c.create_line([(i, 0), (i, h)], tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, h, 40):
            self.c.create_line([(0, i), (w, i)], tag='grid_line')


    def released(self, event):
        print("Released: (%s %s)" % (event.x, event.y))
        self.x1,self.y1=event.x, event.y
        self.c.create_line(A.x,A.y,A.x1,A.y1,width=5)
    def clicked(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.x,self.y=event.x, event.y
        self.c.bind('<ButtonRelease>',self.released)
        
if __name__ == '__main__':
    A=App()
    print(A)
    
    A.root.mainloop()
    # A.mainloop()




