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

]
USING_RPI = False

class Title(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.setupGUI()

    def setupGUI(self):
        button1 = Button(self, text="Easy", command=self.easy)
        button1.grid(row=0, column=1)

        button2 = Button(self, text="Normal", command=self.normal)
        button2.grid(row=1, column=1)

        button3 = Button(self, text="Hard", command=self.hard)
        button3.grid(row=2, column=1)

        self.pack()

    def easy(self):
        self.pack_forget()
        Grid.__init__(self, self.master)

    def normal(self):
        self.pack_forget()
        Grid.__init__(self, self.master)
    
    def hard(self):
        self.pack_forget()
        Grid.__init__(self, self.master)

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
        display = self.display["text"]

class MainGUI(Title, Grid):
    def __init__(self, master):
        Frame.__init__(self, master)
        Title.__init__(self, master)

window = Tk()
window.title("Please Work")
t = MainGUI(window)
window.mainloop()