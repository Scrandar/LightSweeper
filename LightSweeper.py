# Importing packages
import random
import os
import board
import neopixel
from time import sleep
from tkinter import *
FlagMode = False
mines_no = 4
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

    {"row": 1, "col": 8, "value": "Win"},
    {"row": 0, "col": 8, "value": "Flag"},

]
USING_RPI = True

class Grid(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.setupGUI()

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

    def setupGUI(self):
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
        global pix
        
        if button_value=="A1":
           Game_check(0)
            
        if button_value=="B1":
            Game_check(1)
            
        if button_value=="C1":
            Game_check(2)
            
        if button_value=="D1":
            Game_check(3)
            
        if button_value=="E1":
            Game_check(4)
            
        if button_value=="F1":
            Game_check(5)
            
        if button_value=="G1":
            Game_check(6)
            
        if button_value=="H1":
            Game_check(7)

            
        if button_value=="A2":
            Game_check(15)
            
        if button_value=="B2":
            Game_check(14)
            
        if button_value=="C2":
            Game_check(13)
            
        if button_value=="D2":
            Game_check(12)
        if button_value=="E2":
            Game_check(11)
        if button_value=="F2":
            Game_check(10)
        if button_value=="G2":
            Game_check(9)
        if button_value=="H2":
            Game_check(8)
        if button_value=="A3":
            Game_check(16)
        if button_value=="B3":
            Game_check(17)
        if button_value=="C3":
            Game_check(18)
        if button_value=="D3":
            Game_check(19)
        if button_value=="E3":
            Game_check(20)
        if button_value=="F3":
            Game_check(21)
        if button_value=="G3":
            Game_check(22)
        if button_value=="H3":
            Game_check(23)
        if button_value=="A4":
            Game_check(31)
        if button_value=="B4":
            Game_check(30)
        if button_value=="C4":
            Game_check(29)
        if button_value=="D4":
            Game_check(28)
        if button_value=="E4":
            Game_check(27)
        if button_value=="F4":
            Game_check(26)
        if button_value=="G4":
            Game_check(25)
        if button_value=="H4":
            Game_check(24)
        if button_value=="A5":
            Game_check(32)
        if button_value=="B5":
            Game_check(33)
        if button_value=="C5":
            Game_check(34)
        if button_value=="D5":
            Game_check(35)
        if button_value=="E5":
            Game_check(36)
        if button_value=="F5":
            Game_check(37)
        if button_value=="G5":
            Game_check(38)
        if button_value=="H5":
            Game_check(39)
        if button_value=="A6":
            Game_check(47)
        if button_value=="B6":
            Game_check(46)
        if button_value=="C6":
            Game_check(45)
        if button_value=="D6":
            Game_check(44)
        if button_value=="E6":
            Game_check(43)
        if button_value=="F6":
            Game_check(42)
        if button_value=="G6":
            Game_check(41)
        if button_value=="H6":
            Game_check(40)
        if button_value=="A7":
            Game_check(48)
        if button_value=="B7":
            Game_check(49)
        if button_value=="C7":
            Game_check(50)
        if button_value=="D7":
            Game_check(51)
        if button_value=="E7":
            Game_check(52)
        if button_value=="F7":
            Game_check(53)
        if button_value=="G7":
            Game_check(54)
        if button_value=="H7":
            Game_check(55)
        if button_value=="A8":
            Game_check(63)
        if button_value=="B8":
            Game_check(62)
        if button_value=="C8":
            Game_check(61)
        if button_value=="D8":
            Game_check(60)
        if button_value=="E8":
            Game_check(59)
        if button_value=="F8":
            Game_check(58)
        if button_value=="G8":
            Game_check(57)
        if button_value=="H8":
            Game_check(56)

        if button_value == "Flag":
            FlagSet(button_value)

        if button_value == "Win":
            win()
            


class MainGUI(Grid):
    def __init__(self, master):
        Frame.__init__(self, master)
        Grid.__init__(self,master)

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

pixels.fill((255,255,255))

# Printing the Minesweeper Layout
def print_mines_layout():
 
    global shown
    
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
            pixels[i] = Pink
    for i in range(64):
        if actual[i] == 4 and i in vis:
            pixels[i] = Cyan
    
    
    for pix in range(64):
        if shown[pix] == 5:
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
    global FlagMode
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
def FlagSet(button):
    global FlagMode
    if button == "Flag":
        if FlagMode == False:
            FlagMode = True
        else: FlagMode = False
    print(f"Flag mode {FlagMode}")
        

    
    
    

# Recursive function to display all zero-valued vis.append  
def neighbors(pix):
    global vis
    global shown
    global actual
    #if pix not in vis:
        #vis.append(pix)
    if actual[pix] == 0:
        vis.append(pix)
        shown[pix] = actual[pix]

        if pix == 15 or pix == 31 or pix == 47:
            if actual[pix-1] == 0: 
                vis.append(pix-1)
                
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix+2] == 0:
                vis.append(pix+2)
            if actual[pix-14] == 0:
                vis.append(pix-14)
            if actual[pix-15] == 0:
                vis.append(pix-15)
        if pix == 14 or pix == 30 or pix == 46:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix+1)
            if actual[pix+4] == 0:
                vis.append(pix+4)
            if actual[pix-12] == 0:
                vis.append(pix-12)
            if actual[pix-13] == 0:
                vis.append(pix-13)
            if actual[pix-14] == 0:
                vis.append(pix-14)
            if actual[pix+2] == 0:
                vis.append(pix+2)
            if actual[pix+3] == 0:
                vis.append(pix+3)
        if pix == 13 or pix == 29 or pix == 45:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix+6] == 0:
                vis.append(pix+6)
            if actual[pix-10] == 0:
                vis.append(pix-10)
            if actual[pix-11] == 0:
                vis.append(pix-11)
            if actual[pix-12] == 0:
                vis.append(pix-12)
            if actual[pix+4] == 0:
                vis.append(pix+4)
            if actual[pix+5] == 0:
                vis.append(pix+5)
        if pix == 12 or pix == 28 or pix == 44:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix+8] == 0:
                vis.append(pix+8)
            if actual[pix-8] == 0:
                vis.append(pix-8)
            if actual[pix-9] == 0:
                vis.append(pix-9)
            if actual[pix-10] == 0:
                vis.append(pix-10)
            if actual[pix+6] == 0:
                vis.append(pix+6)
            if actual[pix+7] == 0:
                vis.append(pix+7)
        if pix == 11 or pix == 27 or pix == 43:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix+10] == 0:
                vis.append(pix+10)
            if actual[pix-6] == 0:
                vis.append(pix-6)
            if actual[pix-7] == 0:
                vis.append(pix-7)
            if actual[pix-8] == 0:
                vis.append(pix-8)
            if actual[pix+8] == 0:
                vis.append(pix+8)
            if actual[pix+9] == 0:
                vis.append(pix+9)
        if pix == 10 or pix == 26 or pix == 42:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix+12] == 0:
                vis.append(pix+12)
            if actual[pix-4] == 0:
                vis.append(pix-4)
            if actual[pix-5] == 0:
                vis.append(pix-5)
            if actual[pix-6] == 0:
                vis.append(pix-6)
            if actual[pix+10] == 0:
                vis.append(pix+10)
            if actual[pix+11] == 0:
                vis.append(pix+11)
        if pix == 9 or pix == 25 or pix == 41:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix+14] == 0:
                vis.append(pix+14)
            if actual[pix-2] == 0:
                vis.append(pix-2)
            if actual[pix-3] == 0:
                vis.append(pix-3)
            if actual[pix-4] == 0:
                vis.append(pix-4)
            if actual[pix+12] == 0:
                vis.append(pix+12)
            if actual[pix+13] == 0:
                vis.append(pix+13)
        if pix == 8 or pix == 24 or pix == 40:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix-2] == 0:
                vis.append(pix-2)
            if actual[pix+14] == 0:
                vis.append(pix+14)
            if actual[pix+15] == 0:
                vis.append(pix+15)

        if pix == 16 or pix == 32 or pix == 48:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix-2] == 0:
                vis.append(pix-2)
            if actual[pix+15] == 0:
                vis.append(pix+15)
            if actual[pix+14] == 0:
                vis.append(pix+14)
        if pix == 17 or pix == 33 or pix == 49:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix-4] == 0:
                vis.append(pix-4)
            if actual[pix-3] == 0:
                vis.append(pix-3)
            if actual[pix-2] == 0:
                vis.append(pix-2)
            if actual[pix+14] == 0:
                vis.append(pix+14)
            if actual[pix+13] == 0:
                vis.append(pix+13)
            if actual[pix+12] == 0:
                vis.append(pix+12)
        if pix == 18 or pix == 34 or pix == 50:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix-6] == 0:
                vis.append(pix-6)
            if actual[pix-5] == 0:
                vis.append(pix-5)
            if actual[pix-4] == 0:
                vis.append(pix-4)
            if actual[pix+12] == 0:
                vis.append(pix+12)
            if actual[pix+11] == 0:
                vis.append(pix+11)
            if actual[pix+10] == 0:
                vis.append(pix+10)
        if pix == 19 or pix == 35 or pix == 51:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix-8] == 0:
                vis.append(pix-8)
            if actual[pix-7] == 0:
                vis.append(pix-7)
            if actual[pix-6] == 0:
                vis.append(pix-6)
            if actual[pix+10] == 0:
                vis.append(pix+10)
            if actual[pix+9] == 0:
                vis.append(pix+9)
            if actual[pix+8] == 0:
                vis.append(pix+8)
        if pix == 20 or pix == 36 or pix == 52:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix-10] == 0:
                vis.append(pix-10)
            if actual[pix-9] == 0:
                vis.append(pix-9)
            if actual[pix-8] == 0:
                vis.append(pix-8)
            if actual[pix+8] == 0:
                vis.append(pix+8)
            if actual[pix+7] == 0:
                vis.append(pix+7)
            if actual[pix+6] == 0:
                vis.append(pix+6)
        if pix == 21 or pix == 37 or pix == 53:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix-12] == 0:
                vis.append(pix-12)
            if actual[pix-11] == 0:
                vis.append(pix-11)
            if actual[pix-10] == 0:
                vis.append(pix-10)
            if actual[pix+6] == 0:
                vis.append(pix-6)
            if actual[pix+5] == 0:
                vis.append(pix+5)
            if actual[pix+4] == 0:
                vis.append(pix+4)
        if pix == 22 or pix == 38 or pix == 54:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix-14] == 0:
                vis.append(pix-14)
            if actual[pix-13] == 0:
                vis.append(pix-13)
            if actual[pix-12] == 0:
                vis.append(pix-12)
            if actual[pix+4] == 0:
                vis.append(pix+4)
            if actual[pix+3] == 0:
                vis.append(pix+3)
            if actual[pix+2] == 0:
                vis.append(pix+2)
        if pix == 23 or pix == 39 or pix == 55:
            if actual[pix+1] == 0:
                vis.append(pix+1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix+2] == 0:
                vis.append(pix+2)
            if actual[pix-15] == 0:
                vis.append(pix-15)
            if actual[pix-14] == 0:
                vis.append(pix-14)
        if pix == 1 or pix == 2 or pix == 3 or pix == 4 or pix == 5 or pix == 6:
            if actual[15-pix] == 0:
                vis.append(15-pix)
            if actual[15-pix+1] == 0:
                vis.append(15-pix+1)
            if actual[15-pix-1] == 0:
                vis.append(15-pix-1)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix+1] == 0:
                vis.append(pix+1) 
        if pix == 62 or pix == 61 or pix == 60 or pix == 59 or pix == 58 or  pix ==57:
            if actual[(64-pix)+47] == 0:
                vis.append((64-pix)+47)
            if actual[(64-pix)+48] == 0:
                vis.append((64-pix)+48)
            if actual[(64-pix)+46] == 0:
                vis.append((64-pix)+46)
            if actual[pix-1] == 0:
                vis.append(pix-1)
            if actual[pix+1] == 0:
                vis.append(pix+1) 
        if pix == 0:
            if actual[15] == 0:
                vis.append(15)
            if actual[14] == 0:
                vis.append(14)
            if actual[1] == 0:
                vis.append(1)
        if pix == 7:
            if actual[6] == 0:
                vis.append(6)
            if actual[8] == 0:
                vis.append(8)
            if actual[9] == 0:
                vis.append(9)
        if pix == 63:
            if actual[48] == 0:
                vis.append(48)
            if actual[49] == 0:
                vis.append(49)
            if actual[62] == 0:
                vis.append(62)
        if pix == 56:
            if actual[54] == 0:
                vis.append(54)
            if actual[55] == 0:
                vis.append(55)
            if actual[57] == 0:
                vis.append(57)          
    if actual[pix] != 0:
        shown[pix] = actual[pix]
 
# Function for clearing the terminal
def clear():
    os.system("clear")      

 
# Display all the mine locations                    
def show_mines():
    global shown
    global actual
     
    for pix in range(64):
        if actual[pix] == -1:
            pixels[pix] = Red
        if actual[pix] != -1:
            pixels[pix] = off

def mine_set(mines):
    global mines_no
    mines_no = mines

def win():
    for i in range(64):
        pixels[i] = Green
        sleep(.06)
        pixels[i] = Blue
    for i in range(64):
        if i % 2 == 0:
            pixels[i] = Red
        
        
        
        

global actual
global shown
global flags
global mines
global vis

# The actual values of the grid
actual = [0 for x in range(64)] 
# The apparent values of the grid
shown = [0 for x in range(64)]
# The positions that have been flagged
flags = []
# Set the mines
mines = []
set_mines()
vis =[]
# Set the values
#print(actual)
set_values()
print(actual)
counter = 0

# Variable for maintaining Game Loop

global Game_check
# The Game
def Game_check(pix):
    global counter
    #print(f"{pix} worked")
    # If flagging a mine position
    if FlagMode == True:
        if actual[pix] == -1:
            counter += 1
            print(f"{counter}")
            actual[pix] = 5
            vis.append(pix)
            print_mines_layout()
        if actual[pix] != -1:
            
            actual[pix] = 5
            vis.append(pix)
            print_mines_layout()
    # Landing on mine
    elif actual[pix] == -1:
        show_mines()
            #print_mines_layout()
            
    # If landing on a cell with 0 mines in neighboring cells
    if actual[pix] == 0:
        vis.append(pix)
        #shown[pix] = 0
        #neighbors(pix)
        print_mines_layout()
        
        #pixels.fill((0,0,0))
    
    # If selecting a cell with atleast 1 mine in neighboring cells  
    else:
        vis.append(pix)   
        shown[pix] = actual[pix]
    print_mines_layout()

    if counter == 4:
        win()
        

window = Tk()
window.title("Please Work")
t = MainGUI(window)
window.mainloop()

