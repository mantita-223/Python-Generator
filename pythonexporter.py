from dataclasses import dataclass
from tkinter import *
import easygui
checkicon = "check.jpeg"
windowtitle = "untitled"
squares = list()
def wintitle():
    windowtitle = easygui.enterbox("Enter the window title and click 'OK'. If you click 'CANCEL', the window title will be UNTITLED.", "Set window title")


@dataclass
class Square:
    x1: int = None
    y1: int = None
    x2: int = None
    y2: int = None
    color: str = None


def export_squares():
    # import json

    global squares
    # squares_list = [
    #     (square.x1, square.y1, square.x2, square.y2, square.color) for square in squares
    # ]
    # squares_json = json.dumps(squares_list)
    # my_file.write(squares_json)

    with open("exported.py", "w+") as my_file:
        my_file.write(
            "# this code is python code. Put this code in a .py file for it to work."
        )
        my_file.write("\nfrom tkinter import *")
        my_file.write("\nwindow = Tk()")
        my_file.write("\nwindow.title('" + windowtitle + "')")
        my_file.write("\ngamearea = Canvas(window, width=600, height=376)")
        my_file.write("\ngamearea.pack()")
        for square in squares:
            my_file.write(f"\ngamearea.create_rectangle({square.x1}, {square.y1}, {square.x2}, {square.y2}, fill='{square.color}')")
        my_file.write("\nwindow.mainloop()")

        my_file.close()
    easygui.msgbox("Exported Successfully!", "Success!")



def create_square(square: Square = None):
    pass


def create_square_from_user_input() -> Square:
    square = Square()
    square.x1 = int(easygui.enterbox("x1 (number)"))
    square.y1 = int(easygui.enterbox("y1 (number)"))
    square.x2 = int(easygui.enterbox("x2 (number)"))
    square.y2 = int(easygui.enterbox("y2 (number)"))
    msg = "Select the color of the square:"
    title = "Color Selection"
    choices = [
        "red",
        "yellow",
        "green",
        "cyan",
        "blue",
        "navyblue",
        "grey",
        "orange",
        "black",
        "white",
        "brown",
    ]
    square.color = easygui.choicebox(msg, title, choices)
    return square


def squaremakingprocess():
    square = create_square_from_user_input()
    global squares
    squares.append(square)
    print(f"New square added: {squares}")
    drawarea.create_rectangle(
        square.x1, square.y1, square.x2, square.y2, fill=square.color
    )


root = Tk()

root.title("Game Engine Exporter Test")

root.configure(bg="blue")
drawarea = Canvas(root, width=600, height=376)
drawarea.pack()

sq = Button(root, text="Create Square", command=squaremakingprocess)
sq.pack()
settitle = Button(root, text="Set Window Title", command=wintitle)
settitle.pack()
exportbutton = Button(root, text="Export", command=export_squares)
exportbutton.pack()

root.mainloop()
