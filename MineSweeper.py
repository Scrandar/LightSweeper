# Importing packages
import random
import os
import board
import neopixel
cells = 64

Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Orange = (255,128,0)
Yellow = (255,255,0)
Purple = (102,0,204)
Pink = (255,0,255)

pixels = neopixel.NeoPixel(board.D18,cells, brightness=.01, auto_write=True)

# Printing the Minesweeper Layout
def print_mines_layout():
 
    global mine_values
    
    for i in range(64):
        if numbers[i] == -1:
            pixels[i] = (255,0,0)
    for i in range(64):
        if numbers[i] == 1:
            pixels[i] = Blue
    for i in range(64):
        if numbers[i] == 2:
            pixels[i] = Green
    for i in range(64):
        if numbers[i] == 3:
            pixels[i] = Orange
    for i in range(64):
        if numbers[i] == 4:
            pixels[i] = Pink
    for i in range(64):
        if numbers[i] == 5:
            pixels[i] = Purple
    for i in range(64):
        if numbers[i] == 6:
            pixels[i] = (255,0,127)
    for i in range(64):
        if numbers[i] == 7:
            pixels[i] = (102,255,178)
    for i in range(64):
        if numbers[i] == 8:
            pixels[i] = (0,0,153)
# Function for setting up Mines
def set_mines():
 
    global numbers
    global mines_no
    # Track of number of mines already set up
    count = 0
    while count < mines_no:

        # Random number from all possible grid positions 
        val = random.randint(0, 63)
 
        # Generating row and column from the number
        pix = val
 
        # Place the mine, if it doesn't already have one
        if numbers[pix] != -1:
            count = count + 1
            numbers[pix] = -1
 
# Function for setting up the other grid values
def set_values():
 
    global numbers
    # Loop for counting each cell value
    for pix in range(0,64):
        # Skip, if it contains a mine
        if numbers[pix] == -1:
            continue

        # Check neighbors
        if pix == 15 or pix == 31 or pix == 47:
            if numbers[pix-1] == -1: 
                numbers[pix] += 1
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix+2] == -1:
                numbers[pix] += 1
            if numbers[pix-14] == -1:
                numbers[pix] += 1
            if numbers[pix-15] == -1:
                numbers[pix] += 1
        if pix == 14 or pix == 30 or pix == 46:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+4] == -1:
                numbers[pix] += 1
            if numbers[pix-12] == -1:
                numbers[pix] += 1
            if numbers[pix-13] == -1:
                numbers[pix] += 1
            if numbers[pix-14] == -1:
                numbers[pix] += 1
            if numbers[pix+2] == -1:
                numbers[pix] += 1
            if numbers[pix+3] == -1:
                numbers[pix] += 1
        if pix == 13 or pix == 29 or pix == 45:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+6] == -1:
                numbers[pix] += 1
            if numbers[pix-10] == -1:
                numbers[pix] += 1
            if numbers[pix-11] == -1:
                numbers[pix] += 1
            if numbers[pix-12] == -1:
                numbers[pix] += 1
            if numbers[pix+4] == -1:
                numbers[pix] += 1
            if numbers[pix+5] == -1:
                numbers[pix] += 1
        if pix == 12 or pix == 28 or pix == 44:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+8] == -1:
                numbers[pix] += 1
            if numbers[pix-8] == -1:
                numbers[pix] += 1
            if numbers[pix-9] == -1:
                numbers[pix] += 1
            if numbers[pix-10] == -1:
                numbers[pix] += 1
            if numbers[pix+6] == -1:
                numbers[pix] += 1
            if numbers[pix+7] == -1:
                numbers[pix] += 1
        if pix == 11 or pix == 27 or pix == 43:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+10] == -1:
                numbers[pix] += 1
            if numbers[pix-6] == -1:
                numbers[pix] += 1
            if numbers[pix-7] == -1:
                numbers[pix] += 1
            if numbers[pix-8] == -1:
                numbers[pix] += 1
            if numbers[pix+8] == -1:
                numbers[pix] += 1
            if numbers[pix+9] == -1:
                numbers[pix] += 1
        if pix == 10 or pix == 26 or pix == 42:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+12] == -1:
                numbers[pix] += 1
            if numbers[pix-4] == -1:
                numbers[pix] += 1
            if numbers[pix-5] == -1:
                numbers[pix] += 1
            if numbers[pix-6] == -1:
                numbers[pix] += 1
            if numbers[pix+10] == -1:
                numbers[pix] += 1
            if numbers[pix+11] == -1:
                numbers[pix] += 1
        if pix == 9 or pix == 25 or pix == 41:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+14] == -1:
                numbers[pix] += 1
            if numbers[pix-2] == -1:
                numbers[pix] += 1
            if numbers[pix-3] == -1:
                numbers[pix] += 1
            if numbers[pix-4] == -1:
                numbers[pix] += 1
            if numbers[pix+12] == -1:
                numbers[pix] += 1
            if numbers[pix+13] == -1:
                numbers[pix] += 1
        if pix == 8 or pix == 24 or pix == 40:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-2] == -1:
                numbers[pix] += 1
            if numbers[pix+14] == -1:
                numbers[pix] += 1
            if numbers[pix+15] == -1:
                numbers[pix] += 1

        if pix == 16 or pix == 32 or pix == 48:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-2] == -1:
                numbers[pix] += 1
            if numbers[pix+15] == -1:
                numbers[pix] += 1
            if numbers[pix+14] == -1:
                numbers[pix] += 1
        if pix == 17 or pix == 33 or pix == 49:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-4] == -1:
                numbers[pix] += 1
            if numbers[pix-3] == -1:
                numbers[pix] += 1
            if numbers[pix-2] == -1:
                numbers[pix] += 1
            if numbers[pix+14] == -1:
                numbers[pix] += 1
            if numbers[pix+13] == -1:
                numbers[pix] += 1
            if numbers[pix+12] == -1:
                numbers[pix] += 1
        if pix == 18 or pix == 34 or pix == 50:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-6] == -1:
                numbers[pix] += 1
            if numbers[pix-5] == -1:
                numbers[pix] += 1
            if numbers[pix-4] == -1:
                numbers[pix] += 1
            if numbers[pix+12] == -1:
                numbers[pix] += 1
            if numbers[pix+11] == -1:
                numbers[pix] += 1
            if numbers[pix+10] == -1:
                numbers[pix] += 1
        if pix == 19 or pix == 35 or pix == 51:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-8] == -1:
                numbers[pix] += 1
            if numbers[pix-7] == -1:
                numbers[pix] += 1
            if numbers[pix-6] == -1:
                numbers[pix] += 1
            if numbers[pix+10] == -1:
                numbers[pix] += 1
            if numbers[pix+9] == -1:
                numbers[pix] += 1
            if numbers[pix+8] == -1:
                numbers[pix] += 1
        if pix == 20 or pix == 36 or pix == 52:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-10] == -1:
                numbers[pix] += 1
            if numbers[pix-9] == -1:
                numbers[pix] += 1
            if numbers[pix-8] == -1:
                numbers[pix] += 1
            if numbers[pix+8] == -1:
                numbers[pix] += 1
            if numbers[pix+7] == -1:
                numbers[pix] += 1
            if numbers[pix+6] == -1:
                numbers[pix] += 1
        if pix == 21 or pix == 37 or pix == 53:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-12] == -1:
                numbers[pix] += 1
            if numbers[pix-11] == -1:
                numbers[pix] += 1
            if numbers[pix-10] == -1:
                numbers[pix] += 1
            if numbers[pix+6] == -1:
                numbers[pix] += 1
            if numbers[pix+5] == -1:
                numbers[pix] += 1
            if numbers[pix+4] == -1:
                numbers[pix] += 1
        if pix == 22 or pix == 38 or pix == 54:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-14] == -1:
                numbers[pix] += 1
            if numbers[pix-13] == -1:
                numbers[pix] += 1
            if numbers[pix-12] == -1:
                numbers[pix] += 1
            if numbers[pix+4] == -1:
                numbers[pix] += 1
            if numbers[pix+3] == -1:
                numbers[pix] += 1
            if numbers[pix+2] == -1:
                numbers[pix] += 1
        if pix == 23 or pix == 39 or pix == 55:
            if numbers[pix+1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+2] == -1:
                numbers[pix] += 1
            if numbers[pix-15] == -1:
                numbers[pix] += 1
            if numbers[pix-14] == -1:
                numbers[pix] += 1
        if pix == 1 or pix == 2 or pix == 3 or pix == 4 or pix == 5 or pix == 6:
            if numbers[15-pix] == -1:
                numbers[pix] += 1
            if numbers[15-pix+1] == -1:
                numbers[pix] += 1
            if numbers[15-pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+1] == -1:
                numbers[pix] += 1 
        if pix == 62 or pix == 61 or pix == 60 or pix == 59 or pix == 58 or  pix ==57:
            if numbers[(64-pix)+47] == -1:
                numbers[pix] += 1
            if numbers[(64-pix)+48] == -1:
                numbers[pix] += 1
            if numbers[(64-pix)+46] == -1:
                numbers[pix] += 1
            if numbers[pix-1] == -1:
                numbers[pix] += 1
            if numbers[pix+1] == -1:
                numbers[pix] += 1 
        if pix == 0:
            if numbers[15] == -1:
                numbers[pix] += 1
            if numbers[14] == -1:
                numbers[pix] += 1
            if numbers[1] == -1:
                numbers[pix]+=1
        if pix == 7:
            if numbers[6] == -1:
                numbers[pix] += 1
            if numbers[8] == -1:
                numbers[pix] += 1
            if numbers[9] == -1:
                numbers[pix]+=1
        if pix == 63:
            if numbers[48] == -1:
                numbers[pix] += 1
            if numbers[49] == -1:
                numbers[pix] += 1
            if numbers[62] == -1:
                numbers[pix]+=1
        if pix == 56:
            if numbers[54] == -1:
                numbers[pix] += 1
            if numbers[55] == -1:
                numbers[pix] += 1
            if numbers[57] == -1:
                numbers[pix]+=1


# Recursive function to display all zero-valued neighbours  
def neighbours(pix):
     
    global mine_values
    global numbers
    global vis
 
    # If the cell is zero-valued
    if numbers[pix] == 0:

        # Display it to the user
        mine_values[pix] = numbers[pix]

        # Recursive calls for the neighbouring cells
        
    # If the cell is not zero-valued            
    if numbers[pix] != 0:
            mine_values[pix] = numbers[pix]
 
# Function for clearing the terminal
def clear():
    os.system("clear")      
 
# Function to display the instructions
def instructions():
    print("Instructions:")
    print("1. Enter row and column number to select a cell, Example \"2 3\"")
    print("2. In order to flag a mine, enter F after row and column numbers, Example \"2 3 F\"")
 
# Function to check for completion of the game
'''def check_over():
    global mine_values
    global mines_no
 
    # Count of all numbered values
    count = 0
 
    # Loop for checking each cell in the grid
    for r in range(n):
        for col in range(n):
 
            # If cell not empty or flagged
            if mine_values[pix] != ' ' and mine_values[pix] != 'F':
                count = count + 1
     
    # Count comparison          
    if count == n * n - mines_no:
        return True
    else:
        return False'''
 
# Display all the mine locations                    
def show_mines():
    global mine_values
    global numbers
    
 
    for i in range(64):
        if numbers[i] == -1:
            pixels[i] = (255,0,0)
 
 
if __name__ == "__main__":
    # Number of mines
    mines_no = 4
 
    # The actual values of the grid
    numbers = [0 for x in range(64)] 
    # The apparent values of the grid
    mine_values = [0 for x in range(64)]
    # The positions that have been flagged
    flags = []
 
    # Set the mines
    set_mines()
 
    # Set the values
    print(numbers)
    set_values()
    print(numbers)
 
    # Display the instructions
    instructions()
 
    # Variable for maintaining Game Loop
    over = False
         
    # The GAME LOOP 
    while not over:
        print_mines_layout()
        pix = int(input("enter index"))
        # If landing on a mine --- GAME OVER    
        if numbers[pix] == -1:
            
            show_mines()
            print_mines_layout()
            
            over = True
            continue
        
        # If landing on a cell with 0 mines in neighboring cells
        elif numbers[pix] == 0:
            vis = []
            mine_values[pix] = '0'
            neighbours[pix]
 
        # If selecting a cell with atleast 1 mine in neighboring cells  
        else:   
            mine_values[pix] = numbers[pix]
 
        # Check for game completion 
        '''if(check_over()):
            show_mines()
            print_mines_layout()
            print("Congratulations!!! YOU WIN")
            over = True
            continue'''
        clear()