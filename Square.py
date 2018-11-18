from constants import *
import sys

class Square:
    def __init__(self, square_char):
        self.char = square_char
        self.assign_type(square_char)

    def assign_type(self, square_char):
        self.type = None

        if(square_char == OUTSIDE_SQUARE):
            self.type = "Outside"

        elif(square_char == CELLAR_SQUARE):
            self.type = "Cellar"

        elif(square_char in ROOM_SQUARES):
            self.type = "Room"
            self.room_number = square_char

        elif(square_char in STARTING_SQUARES):
            self.type = "Starting"
            self.character_letter = square_char

        elif(square_char == WALKING_SQUARE):
            self.type = "Walking"
            self.is_doorway = False
            #not a doorway because it'd have a different character if it was (but those are also a Walking Square type)

        elif(square_char == DOORWAY_LEFT):
            self.type = "Walking"
            self.is_doorway = True
            self.doorway_direction = "Left"

        elif(square_char == DOORWAY_RIGHT):
            self.type = "Walking"
            self.is_doorway = True
            self.doorway_direction = "Right"

        elif(square_char == DOORWAY_UP):
            self.type = "Walking"
            self.is_doorway = True
            self.doorway_direction = "Up"

        elif(square_char == DOORWAY_DOWN):
            self.type = "Walking"
            self.is_doorway = True
            self.doorway_direction = "Down"

        if(self.type == None):
            print("Error. Unknown square detected.")
            sys.exit(0)


    def get_char(self):
        return self.char

    def get_type(self):
        return self.type
