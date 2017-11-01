from Tkinter import *
root = Tk()

canvas = Canvas(root, height=600, width=600)
canvas.grid()

#Make three objects on the canvas
#board = canvas.create_grid()
a = canvas.create_line(0, 0, 600, 0, fill="black", width=30)
a1 = canvas.create_line(0, 0, 0, 600, fill="black", width=30)
a2 = canvas.create_line(0, 600, 600, 600, fill="black", width=30)
a3 = canvas.create_line(600, 0, 600, 600, fill="black", width=30)

b1 = canvas.create_line(0, 200, 600, 200, fill="black", width=10)
b2 = canvas.create_line(0, 400, 600, 400, fill="black", width=10)

c1 = canvas.create_line(200, 0, 200, 600, fill="black", width=10)
c2 = canvas.create_line(400, 0, 400, 600, fill="black", width=10)

x1 = canvas.create_line(50, 50, 150, 150, fill="maroon", width=10 ) 
x2 = canvas.create_line(50, 150, 150, 50, fill="maroon", width=10 )

v1 = canvas.create_line(250, 250, 350, 350, fill="maroon", width=10 )
v2 = canvas.create_line(250, 350, 350, 250, fill="maroon", width=10 )

g1 = canvas.create_line(550, 550, 450, 450, fill="maroon", width=10 )
g2 = canvas.create_line(550, 450, 450, 550, fill="maroon", width=10 ) 

i = canvas.create_oval(550, 250, 450, 350, fill="dark blue", )

u = canvas.create_oval(350, 550, 250, 450, fill="dark blue", )


o = canvas.create_oval(50, 250, 150, 350, fill="dark blue", )

root.mainloop() 