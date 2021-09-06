# from tkinter import *

# class Test(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         frame = Frame(parent)
        
#         self.canvas = Canvas(frame, bg='white' , width=300, height=100)
#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(0, weight=1)
#         self.canvas.grid(row=0, column=0, sticky='nesw')
        
#         self.canvas.grid(row=1, column=1, sticky='nesw')
#         frame.grid()

# root = Tk()
# Test(root)
# root.mainloop()

from tkinter import *

canvas_width = 500
canvas_height = 150

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_line( x1, y1, x2, y2, fill = python_green )
   
#    create_line([(0, i), (w, i)], tag='grid_line')

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()