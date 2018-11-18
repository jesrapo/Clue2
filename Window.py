from tkinter import *
from constants import *
from tkinter.font import Font


class Window:
    def __init__(self, size_x, size_y, board):
        root = Tk()
        root.title("CLUE")
        board_size_x = board.get_board_size_x()
        board_size_y = board.get_board_size_y()
        my_font = Font(family="Helvetica", size=12)

        #screen_width = root.winfo_screenwidth()
        #screen_height = root.winfo_screenheight()

        for i in range(board_size_y):
            for j in range(board_size_x):
                #current_char = board.get_square_char(i, j)
                current_char = ""
                current_type = board.get_square_type(i, j)
                '''
                if(current_type == "Starting"):
                    square = Button(mainframe)
                    square.config(text = current_char, width = 300, height = 300, bd = 1, font = my_font)
                    square.config(image = self.photo, activebackground = "red", text = current_char)
                '''
                #make the square
                square = Label(root, text = current_char, font = my_font, width = SQUARE_WIDTH, height = SQUARE_HEIGHT)

                #configure the square differently depending on type
                if(current_type == "Starting"):
                    square.config(bg = STARTING_COLOR)

                elif(current_type == "Room" or current_type == "Cellar"):
                    square.config(bg = ROOM_COLOR)

                elif(current_type == "Walking"):
                    square.config(bg = WALKING_COLOR)

                elif(current_type == "Outside"):
                    square.config(bg = OUTSIDE_COLOR)

                square.grid(row = i, column = j)

        root.mainloop()
