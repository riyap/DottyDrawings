from tkinter import  *
color = 'black'
def red():
    global color
    color = 'red'
def orange():
    global color
    color = 'orange'
def yellow():
    global color
    color = 'yellow'
def green():
    global color
    color = 'lime green'
def lime_green():
    global color
    color = 'green'
def light_blue ():
    global color
    color = 'light blue'
def blue ():
    global color
    color = 'blue'
def purple():
    global color
    color = 'purple'
def pink():
    global color
    color = 'pink'
def brown():
    global color
    color = 'brown'
def black():
    global color
    color = 'black'
def gray():
    global color
    color = 'gray'

tk = Tk()
tk.title( "Dotty Drawings")
frame = Frame(tk)
frame.pack()

r = Button(frame, bg = 'red', command = red, width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'orange', command = orange , width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'yellow', command = yellow , width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'lime green', command = lime_green, width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'green', command = green, width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'light blue', command =light_blue , width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'blue', command = blue, width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'purple', command = purple , width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'pink', command = pink, width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'brown', command = brown , width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'black', command = black , width = 5)
r.pack(side = LEFT)
r = Button(frame, bg = 'gray', command = gray , width = 5)
r.pack(side = LEFT)

canvas = Canvas(tk, width = 500, height = 300, bg = 'white', cursor = 'dot')
canvas.pack(expand = YES, fill = BOTH)

def paint(event):
    global color
    x1, y1 = (event.x -5), (event.y -5)
    x2, y2 = (event.x +5), (event.y +5)
    canvas.create_oval(x1,y1,x2,y2, fill = color, outline = color)
canvas.bind("<B1-Motion>", paint)

def clear():
    canvas.delete(ALL)
clear = Button(frame, text = "Clear", command = clear, width = 5)
clear.pack(side = RIGHT)

def erase():
    global color
    color = 'white'
e = Button(frame, text = 'Erase', command = erase, width = 5)
e.pack(side = RIGHT)
#seeing changes on github
tk.mainloop()

    
