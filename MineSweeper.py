# Importing packages
import random
import os
import board
import neopixel
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
    # Number of mines
    mines_no = 4
 
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