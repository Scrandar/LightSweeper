# Importing packages
import random
import os
import board
import neopixel
from tkinter import *
button_data = [
    {"row": 0, "col": 0, "value": "A1"},
    {"row": 0, "col": 1, "value": "A2"},
    {"row": 0, "col": 2, "value": "A3"},
    {"row": 0, "col": 3, "value": "A4"},
    {"row": 0, "col": 4, "value": "A5"},
    {"row": 0, "col": 5, "value": "A6"},
    {"row": 0, "col": 6, "value": "A7"},
    {"row": 0, "col": 7, "value": "A8"},

    {"row": 1, "col": 0, "value": "B1"},
    {"row": 1, "col": 1, "value": "B2"},
    {"row": 1, "col": 2, "value": "B3"},
    {"row": 1, "col": 3, "value": "B4"},
    {"row": 1, "col": 4, "value": "B5"},
    {"row": 1, "col": 5, "value": "B6"},
    {"row": 1, "col": 6, "value": "B7"},
    {"row": 1, "col": 7, "value": "B8"},

    {"row": 2, "col": 0, "value": "C1"},
    {"row": 2, "col": 1, "value": "C2"},
    {"row": 2, "col": 2, "value": "C3"},
    {"row": 2, "col": 3, "value": "C4"},
    {"row": 2, "col": 4, "value": "C5"},
    {"row": 2, "col": 5, "value": "C6"},
    {"row": 2, "col": 6, "value": "C7"},
    {"row": 2, "col": 7, "value": "C8"},

    {"row": 3, "col": 0, "value": "D1"},
    {"row": 3, "col": 1, "value": "D2"},
    {"row": 3, "col": 2, "value": "D3"},
    {"row": 3, "col": 3, "value": "D4"},
    {"row": 3, "col": 4, "value": "D5"},
    {"row": 3, "col": 5, "value": "D6"},
    {"row": 3, "col": 6, "value": "D7"},
    {"row": 3, "col": 7, "value": "D8"},

    {"row": 4, "col": 0, "value": "E1"},
    {"row": 4, "col": 1, "value": "E2"},
    {"row": 4, "col": 2, "value": "E3"},
    {"row": 4, "col": 3, "value": "E4"},
    {"row": 4, "col": 4, "value": "E5"},
    {"row": 4, "col": 5, "value": "E6"},
    {"row": 4, "col": 6, "value": "E7"},
    {"row": 4, "col": 7, "value": "E8"},

    {"row": 5, "col": 0, "value": "F1"},
    {"row": 5, "col": 1, "value": "F2"},
    {"row": 5, "col": 2, "value": "F3"},
    {"row": 5, "col": 3, "value": "F4"},
    {"row": 5, "col": 4, "value": "F5"},
    {"row": 5, "col": 5, "value": "F6"},
    {"row": 5, "col": 6, "value": "F7"},
    {"row": 5, "col": 7, "value": "F8"},

    {"row": 6, "col": 0, "value": "G1"},
    {"row": 6, "col": 1, "value": "G2"},
    {"row": 6, "col": 2, "value": "G3"},
    {"row": 6, "col": 3, "value": "G4"},
    {"row": 6, "col": 4, "value": "G5"},
    {"row": 6, "col": 5, "value": "G6"},
    {"row": 6, "col": 6, "value": "G7"},
    {"row": 6, "col": 7, "value": "G8"},

    {"row": 7, "col": 0, "value": "H1"},
    {"row": 7, "col": 1, "value": "H2"},
    {"row": 7, "col": 2, "value": "H3"},
    {"row": 7, "col": 3, "value": "H4"},
    {"row": 7, "col": 4, "value": "H5"},
    {"row": 7, "col": 5, "value": "H6"},
    {"row": 7, "col": 6, "value": "H7"},
    {"row": 7, "col": 7, "value": "H8"},

    {"row": 0, "col": 8, "value": "Restart"},
    {"row": 0, "col": 8, "value": "Flag"},

]
USING_RPI = False

class Title(Grid):
    def __init__(self, master):
        #Frame.__init__(self, master)
        self.setupGUI(master)

    def setupGUI(self, master):
        button1 = Button(self, text="Easy", command=lambda: self.easy(master))
        button1.grid(row=0, column=1)

        button2 = Button(self, text="Normal", command=lambda: self.normal(master))
        button2.grid(row=1, column=1)

        button3 = Button(self, text="Hard", command=lambda: self.hard(master))
        button3.grid(row=2, column=1)

        self.pack()

    def easy(self, master):
        global mines_no
        self.pack_forget()
        Grid.__init__(self, master)
        mines_no=4

    def normal(self, master):
        global mines_no
        self.pack_forget()
        Grid.__init__(self, master)
        mines_no=6
    
    def hard(self, master):
        global mines_no
        self.pack_forget()
        Grid.__init__(self, master)
        mines_no=8

class Grid(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.setup_GUI()

    def make_button(self, row, col, value):
        bg_color = "white"

        button = Button(
            self, 
            font=("Arial", 30), 
            text=value,
            bg=bg_color,
            borderwidth=1,
            highlightthickness=0,
            width=5,
            activebackground="white",
            command=lambda: self.handle_button_press(value)
        )

        button.grid(row=row, column=col, sticky=NSEW)

    def setup_GUI(self):
        self.display = Label(self, text="", anchor=E, bg="white", fg="black", height=1, font=("Arial", 40))
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)

        for row in range(8):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(8):
            Grid.columnconfigure(self, col, weight=1)

        for button in button_data:
            self.make_button(button["row"], button["col"], button["value"])

        self.pack(fill=BOTH, expand = 1)

    def handle_button_press(self, button_value):
        global pos
        if button_value=="A1":
            pos=0
        elif button_value=="B1":
            pos=1
        elif button_value=="C1":
            pos=2
        elif button_value=="D1":
            pos=3
        elif button_value=="E1":
            pos=4
        elif button_value=="F1":
            pos=5
        elif button_value=="G1":
            pos=6
        elif button_value=="H1":
            pos=7
        elif button_value=="A2":
            pos=15
        elif button_value=="B2":
            pos=14
        elif button_value=="C2":
            pos=13
        elif button_value=="D2":
            pos=12
        elif button_value=="E2":
            pos=11
        elif button_value=="F2":
            pos=10
        elif button_value=="G2":
            pos=9
        elif button_value=="H2":
            pos=8
        elif button_value=="A3":
            pos=16
        elif button_value=="B3":
            pos=17
        elif button_value=="C3":
            pos=18
        elif button_value=="D3":
            pos=19
        elif button_value=="E3":
            pos=20
        elif button_value=="F3":
            pos=21
        elif button_value=="G3":
            pos=22
        elif button_value=="H3":
            pos=23
        elif button_value=="A4":
            pos=31
        elif button_value=="B4":
            pos=30
        elif button_value=="C4":
            pos=29
        elif button_value=="D4":
            pos=28
        elif button_value=="E4":
            pos=27
        elif button_value=="F4":
            pos=26
        elif button_value=="G4":
            pos=25
        elif button_value=="H4":
            pos=24
        elif button_value=="A5":
            pos=32
        elif button_value=="B5":
            pos=33
        elif button_value=="C5":
            pos=34
        elif button_value=="D5":
            pos=35
        elif button_value=="E5":
            pos=36
        elif button_value=="F5":
            pos=37
        elif button_value=="G5":
            pos=38
        elif button_value=="H5":
            pos=39
        elif button_value=="A6":
            pos=47
        elif button_value=="B6":
            pos=46
        elif button_value=="C6":
            pos=45
        elif button_value=="D6":
            pos=44
        elif button_value=="E6":
            pos=43
        elif button_value=="F6":
            pos=42
        elif button_value=="G6":
            pos=41
        elif button_value=="H6":
            pos=40
        elif button_value=="A7":
            pos=48
        elif button_value=="B7":
            pos=49
        elif button_value=="C7":
            pos=50
        elif button_value=="D7":
            pos=51
        elif button_value=="E7":
            pos=52
        elif button_value=="F7":
            pos=53
        elif button_value=="G7":
            pos=54
        elif button_value=="H7":
            pos=55
        elif button_value=="A8":
            pos=63
        elif button_value=="B8":
            pos=62
        elif button_value=="C8":
            pos=61
        elif button_value=="D8":
            pos=60
        elif button_value=="E8":
            pos=59
        elif button_value=="F8":
            pos=58
        elif button_value=="G8":
            pos=57
        elif button_value=="H8":
            pos=56
            
        return pos

        #display = self.display["text"]

class MainGUI(Title, Grid):
    def __init__(self, master):
        Frame.__init__(self, master)
        Title.__init__(self, master)

cells = 64

off = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Orange = (255,128,0)
Yellow = (255,255,0)
Purple = (102,0,204)
Pink = (255,0,255)
Cyan = (0,255,255)

pixels = neopixel.NeoPixel(board.D18,cells, brightness=.01, auto_write=True)
FlagMode = False

# Printing the Minesweeper Layout
def print_mines_layout():
 
    global shown
    pixels.fill((255,255,255))
    for i in range(64):
        if actual[i] == 0 and i in vis:
            pixels[i] = off

    '''for i in range(64):
        if actual[i] == -1 and i in vis:
            pixels[i] = (255,0,0)'''
    for i in range(64):
        if actual[i] == 1 and i in vis:
            pixels[i] = Blue
    for i in range(64):
        if actual[i] == 2 and i in vis:
            pixels[i] = Green
    for i in range(64):
        if actual[i] == 3 and i in vis:
            pixels[i] = Cyan
    for i in range(64):
        if actual[i] == 4 and i in vis:
            pixels[i] = Pink
    for i in range(64):
        if actual[i] == 5 and i in vis:
            pixels[i] = Purple
    for i in range(64):
        if actual[i] == 6 and i in vis:
            pixels[i] = (255,0,127)
    for i in range(64):
        if actual[i] == 7 and i in vis:
            pixels[i] = (102,255,178)
    for i in range(64):
        if actual[i] == 8 and i in vis:
            pixels[i] = (0,0,153)
    
    for pix in range(64):
        if pix in flags:
            pixels[pix] = Orange

# Function for setting up Mines
def set_mines():
 
    global actual
    global mines_no
    # Track of number of mines already set up
    count = 0
    while count < mines_no:

        # Random number from all possible grid positions 
        val = random.randint(0, 63)
 
        # Generating row and column from the number
        pix = val
 
        # Place the mine, if it doesn't already have one
        if actual[pix] != -1:
            count = count + 1
            mines.append(pix)
            actual[pix] = -1
 
# Function for setting up the other grid values
def set_values():
 
    global actual
    # Loop for counting each cell value
    for pix in range(0,64):
        # Skip, if it contains a mine
        if actual[pix] == -1:
            continue

        # Check neighbors
        if pix == 15 or pix == 31 or pix == 47:
            if actual[pix-1] == -1: 
                actual[pix] += 1
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix+2] == -1:
                actual[pix] += 1
            if actual[pix-14] == -1:
                actual[pix] += 1
            if actual[pix-15] == -1:
                actual[pix] += 1
        if pix == 14 or pix == 30 or pix == 46:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+4] == -1:
                actual[pix] += 1
            if actual[pix-12] == -1:
                actual[pix] += 1
            if actual[pix-13] == -1:
                actual[pix] += 1
            if actual[pix-14] == -1:
                actual[pix] += 1
            if actual[pix+2] == -1:
                actual[pix] += 1
            if actual[pix+3] == -1:
                actual[pix] += 1
        if pix == 13 or pix == 29 or pix == 45:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+6] == -1:
                actual[pix] += 1
            if actual[pix-10] == -1:
                actual[pix] += 1
            if actual[pix-11] == -1:
                actual[pix] += 1
            if actual[pix-12] == -1:
                actual[pix] += 1
            if actual[pix+4] == -1:
                actual[pix] += 1
            if actual[pix+5] == -1:
                actual[pix] += 1
        if pix == 12 or pix == 28 or pix == 44:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+8] == -1:
                actual[pix] += 1
            if actual[pix-8] == -1:
                actual[pix] += 1
            if actual[pix-9] == -1:
                actual[pix] += 1
            if actual[pix-10] == -1:
                actual[pix] += 1
            if actual[pix+6] == -1:
                actual[pix] += 1
            if actual[pix+7] == -1:
                actual[pix] += 1
        if pix == 11 or pix == 27 or pix == 43:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+10] == -1:
                actual[pix] += 1
            if actual[pix-6] == -1:
                actual[pix] += 1
            if actual[pix-7] == -1:
                actual[pix] += 1
            if actual[pix-8] == -1:
                actual[pix] += 1
            if actual[pix+8] == -1:
                actual[pix] += 1
            if actual[pix+9] == -1:
                actual[pix] += 1
        if pix == 10 or pix == 26 or pix == 42:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+12] == -1:
                actual[pix] += 1
            if actual[pix-4] == -1:
                actual[pix] += 1
            if actual[pix-5] == -1:
                actual[pix] += 1
            if actual[pix-6] == -1:
                actual[pix] += 1
            if actual[pix+10] == -1:
                actual[pix] += 1
            if actual[pix+11] == -1:
                actual[pix] += 1
        if pix == 9 or pix == 25 or pix == 41:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+14] == -1:
                actual[pix] += 1
            if actual[pix-2] == -1:
                actual[pix] += 1
            if actual[pix-3] == -1:
                actual[pix] += 1
            if actual[pix-4] == -1:
                actual[pix] += 1
            if actual[pix+12] == -1:
                actual[pix] += 1
            if actual[pix+13] == -1:
                actual[pix] += 1
        if pix == 8 or pix == 24 or pix == 40:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix-2] == -1:
                actual[pix] += 1
            if actual[pix+14] == -1:
                actual[pix] += 1
            if actual[pix+15] == -1:
                actual[pix] += 1

        if pix == 16 or pix == 32 or pix == 48:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix-2] == -1:
                actual[pix] += 1
            if actual[pix+15] == -1:
                actual[pix] += 1
            if actual[pix+14] == -1:
                actual[pix] += 1
        if pix == 17 or pix == 33 or pix == 49:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix-4] == -1:
                actual[pix] += 1
            if actual[pix-3] == -1:
                actual[pix] += 1
            if actual[pix-2] == -1:
                actual[pix] += 1
            if actual[pix+14] == -1:
                actual[pix] += 1
            if actual[pix+13] == -1:
                actual[pix] += 1
            if actual[pix+12] == -1:
                actual[pix] += 1
        if pix == 18 or pix == 34 or pix == 50:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix-6] == -1:
                actual[pix] += 1
            if actual[pix-5] == -1:
                actual[pix] += 1
            if actual[pix-4] == -1:
                actual[pix] += 1
            if actual[pix+12] == -1:
                actual[pix] += 1
            if actual[pix+11] == -1:
                actual[pix] += 1
            if actual[pix+10] == -1:
                actual[pix] += 1
        if pix == 19 or pix == 35 or pix == 51:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix-8] == -1:
                actual[pix] += 1
            if actual[pix-7] == -1:
                actual[pix] += 1
            if actual[pix-6] == -1:
                actual[pix] += 1
            if actual[pix+10] == -1:
                actual[pix] += 1
            if actual[pix+9] == -1:
                actual[pix] += 1
            if actual[pix+8] == -1:
                actual[pix] += 1
        if pix == 20 or pix == 36 or pix == 52:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix-10] == -1:
                actual[pix] += 1
            if actual[pix-9] == -1:
                actual[pix] += 1
            if actual[pix-8] == -1:
                actual[pix] += 1
            if actual[pix+8] == -1:
                actual[pix] += 1
            if actual[pix+7] == -1:
                actual[pix] += 1
            if actual[pix+6] == -1:
                actual[pix] += 1
        if pix == 21 or pix == 37 or pix == 53:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix-12] == -1:
                actual[pix] += 1
            if actual[pix-11] == -1:
                actual[pix] += 1
            if actual[pix-10] == -1:
                actual[pix] += 1
            if actual[pix+6] == -1:
                actual[pix] += 1
            if actual[pix+5] == -1:
                actual[pix] += 1
            if actual[pix+4] == -1:
                actual[pix] += 1
        if pix == 22 or pix == 38 or pix == 54:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix-14] == -1:
                actual[pix] += 1
            if actual[pix-13] == -1:
                actual[pix] += 1
            if actual[pix-12] == -1:
                actual[pix] += 1
            if actual[pix+4] == -1:
                actual[pix] += 1
            if actual[pix+3] == -1:
                actual[pix] += 1
            if actual[pix+2] == -1:
                actual[pix] += 1
        if pix == 23 or pix == 39 or pix == 55:
            if actual[pix+1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+2] == -1:
                actual[pix] += 1
            if actual[pix-15] == -1:
                actual[pix] += 1
            if actual[pix-14] == -1:
                actual[pix] += 1
        if pix == 1 or pix == 2 or pix == 3 or pix == 4 or pix == 5 or pix == 6:
            if actual[15-pix] == -1:
                actual[pix] += 1
            if actual[15-pix+1] == -1:
                actual[pix] += 1
            if actual[15-pix-1] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+1] == -1:
                actual[pix] += 1 
        if pix == 62 or pix == 61 or pix == 60 or pix == 59 or pix == 58 or  pix ==57:
            if actual[(64-pix)+47] == -1:
                actual[pix] += 1
            if actual[(64-pix)+48] == -1:
                actual[pix] += 1
            if actual[(64-pix)+46] == -1:
                actual[pix] += 1
            if actual[pix-1] == -1:
                actual[pix] += 1
            if actual[pix+1] == -1:
                actual[pix] += 1 
        if pix == 0:
            if actual[15] == -1:
                actual[pix] += 1
            if actual[14] == -1:
                actual[pix] += 1
            if actual[1] == -1:
                actual[pix]+=1
        if pix == 7:
            if actual[6] == -1:
                actual[pix] += 1
            if actual[8] == -1:
                actual[pix] += 1
            if actual[9] == -1:
                actual[pix]+=1
        if pix == 63:
            if actual[48] == -1:
                actual[pix] += 1
            if actual[49] == -1:
                actual[pix] += 1
            if actual[62] == -1:
                actual[pix]+=1
        if pix == 56:
            if actual[54] == -1:
                actual[pix] += 1
            if actual[55] == -1:
                actual[pix] += 1
            if actual[57] == -1:
                actual[pix]+=1


# Recursive function to display all zero-valued neighbours  
def neighbours(pix):
    if pix not in vis:
        vis.append(pix)
        if actual[pix] == 0:
            shown[pix] = actual[pix]

            if pix == 15 or pix == 31 or pix == 47:
                if actual[pix-1] == 0: 
                    neighbours(pix-1)
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix+2] == 0:
                    neighbours(pix+2)
                if actual[pix-14] == 0:
                    neighbours(pix-14)
                if actual[pix-15] == 0:
                    neighbours(pix-15)
            if pix == 14 or pix == 30 or pix == 46:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix+1)
                if actual[pix+4] == 0:
                    neighbours(pix+4)
                if actual[pix-12] == 0:
                    neighbours(pix-12)
                if actual[pix-13] == 0:
                    neighbours(pix-13)
                if actual[pix-14] == 0:
                    neighbours(pix-14)
                if actual[pix+2] == 0:
                    neighbours(pix+2)
                if actual[pix+3] == 0:
                    neighbours(pix+3)
            if pix == 13 or pix == 29 or pix == 45:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix+6] == 0:
                    neighbours(pix+6)
                if actual[pix-10] == 0:
                    neighbours(pix-10)
                if actual[pix-11] == 0:
                    neighbours(pix-11)
                if actual[pix-12] == 0:
                    neighbours(pix-12)
                if actual[pix+4] == 0:
                    neighbours(pix+4)
                if actual[pix+5] == 0:
                    neighbours(pix+5)
            if pix == 12 or pix == 28 or pix == 44:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix+8] == 0:
                    neighbours(pix+8)
                if actual[pix-8] == 0:
                    neighbours(pix-8)
                if actual[pix-9] == 0:
                    neighbours(pix-9)
                if actual[pix-10] == 0:
                    neighbours(pix-10)
                if actual[pix+6] == 0:
                    neighbours(pix+6)
                if actual[pix+7] == 0:
                    neighbours(pix+7)
            if pix == 11 or pix == 27 or pix == 43:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix+10] == 0:
                    neighbours(pix+10)
                if actual[pix-6] == 0:
                    neighbours(pix-6)
                if actual[pix-7] == 0:
                    neighbours(pix-7)
                if actual[pix-8] == 0:
                    neighbours(pix-8)
                if actual[pix+8] == 0:
                    neighbours(pix+8)
                if actual[pix+9] == 0:
                    neighbours(pix+9)
            if pix == 10 or pix == 26 or pix == 42:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix+12] == 0:
                    neighbours(pix+12)
                if actual[pix-4] == 0:
                    neighbours(pix-4)
                if actual[pix-5] == 0:
                    neighbours(pix-5)
                if actual[pix-6] == 0:
                    neighbours(pix-6)
                if actual[pix+10] == 0:
                    neighbours(pix+10)
                if actual[pix+11] == 0:
                    neighbours(pix+11)
            if pix == 9 or pix == 25 or pix == 41:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix+14] == 0:
                    neighbours(pix+14)
                if actual[pix-2] == 0:
                    neighbours(pix-2)
                if actual[pix-3] == 0:
                    neighbours(pix-3)
                if actual[pix-4] == 0:
                    neighbours(pix-4)
                if actual[pix+12] == 0:
                    neighbours(pix+12)
                if actual[pix+13] == 0:
                    neighbours(pix+13)
            if pix == 8 or pix == 24 or pix == 40:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix-2] == 0:
                    neighbours(pix-2)
                if actual[pix+14] == 0:
                    neighbours(pix+14)
                if actual[pix+15] == 0:
                    neighbours(pix+15)

            if pix == 16 or pix == 32 or pix == 48:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix-2] == 0:
                    neighbours(pix-2)
                if actual[pix+15] == 0:
                    neighbours(pix+15)
                if actual[pix+14] == 0:
                    neighbours(pix+14)
            if pix == 17 or pix == 33 or pix == 49:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix-4] == 0:
                    neighbours(pix-4)
                if actual[pix-3] == 0:
                    neighbours(pix-3)
                if actual[pix-2] == 0:
                    neighbours(pix-2)
                if actual[pix+14] == 0:
                    neighbours(pix+14)
                if actual[pix+13] == 0:
                    neighbours(pix+13)
                if actual[pix+12] == 0:
                    neighbours(pix+12)
            if pix == 18 or pix == 34 or pix == 50:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix-6] == 0:
                    neighbours(pix-6)
                if actual[pix-5] == 0:
                    neighbours(pix-5)
                if actual[pix-4] == 0:
                    neighbours(pix-4)
                if actual[pix+12] == 0:
                    neighbours(pix+12)
                if actual[pix+11] == 0:
                    neighbours(pix+11)
                if actual[pix+10] == 0:
                    neighbours(pix+10)
            if pix == 19 or pix == 35 or pix == 51:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix-8] == 0:
                    neighbours(pix-8)
                if actual[pix-7] == 0:
                    neighbours(pix-7)
                if actual[pix-6] == 0:
                    neighbours(pix-6)
                if actual[pix+10] == 0:
                    neighbours(pix+10)
                if actual[pix+9] == 0:
                    neighbours(pix+9)
                if actual[pix+8] == 0:
                    neighbours(pix+8)
            if pix == 20 or pix == 36 or pix == 52:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix-10] == 0:
                    neighbours(pix-10)
                if actual[pix-9] == 0:
                    neighbours(pix-9)
                if actual[pix-8] == 0:
                    neighbours(pix-8)
                if actual[pix+8] == 0:
                    neighbours(pix+8)
                if actual[pix+7] == 0:
                    neighbours(pix+7)
                if actual[pix+6] == 0:
                    neighbours(pix+6)
            if pix == 21 or pix == 37 or pix == 53:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix-12] == 0:
                    neighbours(pix-12)
                if actual[pix-11] == 0:
                    neighbours(pix-11)
                if actual[pix-10] == 0:
                    neighbours(pix-10)
                if actual[pix+6] == 0:
                    neighbours(pix-6)
                if actual[pix+5] == 0:
                    neighbours(pix+5)
                if actual[pix+4] == 0:
                    neighbours(pix+4)
            if pix == 22 or pix == 38 or pix == 54:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix-14] == 0:
                    neighbours(pix-14)
                if actual[pix-13] == 0:
                    neighbours(pix-13)
                if actual[pix-12] == 0:
                    neighbours(pix-12)
                if actual[pix+4] == 0:
                    neighbours(pix+4)
                if actual[pix+3] == 0:
                    neighbours(pix+3)
                if actual[pix+2] == 0:
                    neighbours(pix+2)
            if pix == 23 or pix == 39 or pix == 55:
                if actual[pix+1] == 0:
                    neighbours(pix+1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix+2] == 0:
                    neighbours(pix+2)
                if actual[pix-15] == 0:
                    neighbours(pix-15)
                if actual[pix-14] == 0:
                    neighbours(pix-14)
            if pix == 1 or pix == 2 or pix == 3 or pix == 4 or pix == 5 or pix == 6:
                if actual[15-pix] == 0:
                    neighbours(15-pix)
                if actual[15-pix+1] == 0:
                    neighbours(15-pix+1)
                if actual[15-pix-1] == 0:
                    neighbours(15-pix-1)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix+1] == 0:
                    neighbours(pix+1) 
            if pix == 62 or pix == 61 or pix == 60 or pix == 59 or pix == 58 or  pix ==57:
                if actual[(64-pix)+47] == 0:
                    neighbours((64-pix)+47)
                if actual[(64-pix)+48] == 0:
                    neighbours((64-pix)+48)
                if actual[(64-pix)+46] == 0:
                    neighbours((64-pix)+46)
                if actual[pix-1] == 0:
                    neighbours(pix-1)
                if actual[pix+1] == 0:
                    neighbours(pix+1) 
            if pix == 0:
                if actual[15] == 0:
                    neighbours(15)
                if actual[14] == 0:
                    neighbours(14)
                if actual[1] == 0:
                    neighbours(1)
            if pix == 7:
                if actual[6] == 0:
                    neighbours(6)
                if actual[8] == 0:
                    neighbours(8)
                if actual[9] == 0:
                    neighbours(9)
            if pix == 63:
                if actual[48] == 0:
                    neighbours(48)
                if actual[49] == 0:
                    neighbours(49)
                if actual[62] == 0:
                    neighbours(62)
            if pix == 56:
                if actual[54] == 0:
                    neighbours(54)
                if actual[55] == 0:
                    neighbours(55)
                if actual[57] == 0:
                    neighbours(57)          
        if actual[pix] != 0:
            shown[pix] = actual[pix]
 
# Function for clearing the terminal
def clear():
    os.system("clear")      

 
# Function to check for completion of the game
def check_over():
    global shown
    global mines_no
 
    # Count of all numbered values
    count = 0
    # Loop for checking each cell in the grid
    for pix in range(64):
        # If cell not empty or flagged
        if shown[pix] != 0 and pix not in flags:
            count = count + 1
     
    # Count comparison          
    if count == 64 - mines_no:
        return True
    else:
        return False
 
# Display all the mine locations                    
def show_mines():
    global shown
    global actual
     
    for pix in range(64):
        if actual[pix] == -1:
            pixels[pix] = Red
        if actual[pix] != -1:
            pixels[pix] = off
 
 
if __name__ == "__main__":
    window = Tk()
    window.title("Please Work")
    t = MainGUI(window)
    window.mainloop()
 
    # The actual values of the grid
    actual = [0 for x in range(64)] 
    # The apparent values of the grid
    shown = [0 for x in range(64)]
    # The positions that have been flagged
    flags = []
    # Set the mines
    mines = []
    set_mines()
 
    # Set the values
    #print(actual)
    set_values()
    #print(actual)
 
    # Variable for maintaining Game Loop
    over = False
         
    # The GAME LOOP 
    while not over:
        print_mines_layout()
        pix = int(input("enter index"))
        # If flagging a mine position
        if FlagMode == True:    
            if actual[pix] == -1:
                flags.append(pix)
                print_mines_layout()
                continue
        # Landing on mine
        elif FlagMode == False:
            if actual[pix] == -1:
                show_mines()
                print_mines_layout()
                
                over = True
                continue
        # Flagging any other space
        elif FlagMode == True:
            if actual[pix] != -1:
                print_mines_layout
                continue

        # If landing on a cell with 0 mines in neighboring cells
        elif actual[pix] == 0:
            vis = []
            shown[pix] = 0
            neighbours(pix)
 
        # If selecting a cell with atleast 1 mine in neighboring cells  
        else:   
            shown[pix] = actual[pix]
 
        # Check for game completion 
        if(check_over()):
            print_mines_layout()
            over = True
            continue
        clear()