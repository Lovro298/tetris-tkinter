from re import I
from tkinter import *

import random 


class Lik(object):

    LIK_TO_IDX = { 'palica' : 0, 'kocka' : 1 }

    BARVE = [ ['green', 'dark green'],  ['yellow', 'gold'] ]

    def __init__(self, vrsta, frame, canvas, x0, y0, stranica, i, j, rotacija):
        self.vrsta = vrsta
        self.ix = Lik.LIK_TO_IDX[vrsta]
        self.frame = frame
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.i = i
        self.j = j
        self.a = stranica
        self.rotacija = rotacija
        self.elementi = []

        self.narisi()

    def narisi(self):
        if (self.vrsta == 'palica'):
            barva = Lik.BARVE[self.ix][0]
            barvaObrobe = Lik.BARVE[self.ix][1]
            
            if (self.rotacija in [0, 180]):
                # risi vodoravno
                for k in range(4):
                    x1 = self.x0 + self.a * (self.j + k)
                    y1 = self.y0 + self.a * self.i 
                    x2 = self.x0 + self.a * (self.j + 1 + k)
                    y2 = self.y0 + self.a * (self.i + 1)
                    kv = self.canvas.create_rectangle(x1, y1, x2, y2, fill = barva, outline = barvaObrobe)
                    self.elementi.append(kv)
            elif (self.rotacija in [90, 270]):
                # risi navpicno
                for k in range(4):
                    x1 = self.x0 + self.a * self.j
                    y1 = self.y0 + self.a * (self.i + k) 
                    x2 = self.x0 + self.a * (self.j + 1)
                    y2 = self.y0 + self.a * (self.i + 1 + k)
                    kv = self.canvas.create_rectangle(x1, y1, x2, y2, fill = barva, outline = barvaObrobe)
                    self.elementi.append(kv)
            None
        elif (self.vrsta == 'kocka'):
            barva = Lik.BARVE[self.ix][0]
            barvaObrobe = Lik.BARVE[self.ix][1]
            for k in range(2):
                for l in range(2):
                    x1 = self.x0 + self.a * (self.j + l)
                    y1 = self.y0 + self.a * (self.i + k) 
                    x2 = self.x0 + self.a * (self.j + 1 + l)
                    y2 = self.y0 + self.a * (self.i + 1 + k)
                    kv = self.canvas.create_rectangle(x1, y1, x2, y2, fill = barva, outline = barvaObrobe)
                    self.elementi.append(kv)
            None

    def premakni_navzdol(self, n):
        if (n == 0):
            return
        else:
            print(self.elementi)
            for element in self.elementi:
                # (x1, y1, x2, y2) = self.canvas.itemcget(element, 'coords')
                (x1, y1, x2, y2) = self.canvas.coords(element)
                print(x1, y1, x2, y2)
                #self.canvas.itemconfigure(element,  x = (x1 + 10), y = (y1 + 10))
                self.canvas.move(element,  0, 40)
                
            self.frame.after(500, lambda : self.premakni_navzdol(n - 1))
        None

    def animate(self):
        self.frame.after(500, lambda : self.premakni_navzdol(12))


def make_grid_arr():
    
    squareArr = []

    for i in range(200):
        squareArr.append(i+1)

    return squareArr


def colored_square(canvas,field):
    return canvas.itemconfig(field, fill="green")


def tetrominos():


    l = [[5,15,25,26], [15,16,17,7], [5,6,16,26], [5,6,7,15]]
    straight = [[4,5,6,7],[5,15,25,35]]
    square = [[5,6,15,16]]
    t = [[4,5,6,15], [5,15,16,25], [5,14,15,16], [6,15,16,26]]
    skew = [[15,16,6,7],[26,16,17,7]]

    tetrominoArr=[l, straight, square, t, skew]
    #print(tetrominoArr)

    rand = random.randrange(0,4)

    return tetrominoArr[rand]

def display_shape(c,canvas, field):

    if len(c)>1:
        randIndex = random.randrange(0,len(c)-1)
    else:
        randIndex = 0


    for k in (c[randIndex]):
        if field == k:
            print(k)
            return colored_square(canvas,field)

def make_grid(canvas):

    arr = make_grid_arr()

    c = tetrominos()
    

    for i in range(20):     #i=height
        for j in range(10):         #j=width
            field = canvas.create_rectangle(j*40, i*40, (j+1)*40,(i+1)*40, fill="red")
            #print(field)
            display_shape(c,canvas,field)

def main():
    
    window = Tk()
    window.withdraw()
    window.title("Tetris")

    canvas = Canvas(window, width=400, height=800, background="grey")
    canvas.pack()

    make_grid(canvas)
    palica0 = Lik('palica', window, canvas, 0, 0, 40, 16, 5, 0)
    palica90 = Lik('palica', window, canvas, 0, 0, 40, 4, 3, 90)
    palica = Lik('kocka', window, canvas, 0, 0, 40, 10, 5, 0)

    palica90.animate()

    window.deiconify()
    window.mainloop()

if __name__ == "__main__":
    main()