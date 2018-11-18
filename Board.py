from constants import *
from Square import *
import sys

class Board:
    def __init__(self, room_list, weapon_list, player_list):
        #use open("map.txt") or something like that

        self.make_board()
        self.add_rooms()
        self.add_weapons()
        self.add_players()


    def make_board(self):
        #import the board from file MAP_FILE_NAME, and save it as a list of lists of squares
        are_there_still_rows = True

        self.rows = []
        #list of rows (made up of Squares)

        self.open_file()

        self.how_many_rows = self.find_how_many_rows()
        for i in range(self.how_many_rows):
            self.add_row()

    def find_how_many_rows(self):
        #count how many rows there are until the delimiter

        the_file = open(MAP_FILE_NAME)
        is_file_still_going = True
        how_many_rows = 0

        while(is_file_still_going):
            #read the file, line by line, adding 1 to the count every time you don't hit the delimiter

            current_row = the_file.readline()
            if(current_row == DELIMITER):
                is_file_still_going = False
            else:
                how_many_rows +=1

        return how_many_rows

    def get_board_size_x(self):
        the_file = open(MAP_FILE_NAME)
        is_line_still_going = True
        how_many_chars = 0

        while(is_line_still_going):
            #read the line, char by char, adding 1 to the count every time you don't hit the endline

            current_char = the_file.read(1)
            if(current_char == '\n'):
                is_line_still_going = False
            else:
                how_many_chars +=1

        return how_many_chars
        
    def get_board_size_y(self):
        #wrapper to get the y-size of the board
        return self.find_how_many_rows()

    def add_row(self):
        new_row = []
        row_is_not_over = True

        while(row_is_not_over):
            #add Square objects to the row on loop until you reach the endline character
            row_is_not_over = self.add_next_square_char(new_row)

        #add the row to the list of rows
        self.rows.append(new_row)

    def add_next_square_char(self, current_row):
        next_square_char = self.my_file.read(1)

        if(next_square_char == "\n"):
            #if we've reached the end of the line, end the loop
            return False
        else:
            #if we haven't reached the end of the line, add this Square to the row
            new_square_object = Square(next_square_char)
            current_row.append(new_square_object)
            return True

    def open_file(self):
        #opens the file object as a member variable, or exits the program if there's no file with the filename given
        try:
            self.my_file = open(MAP_FILE_NAME)
        except FileNotFoundError:
            sys.exit("Sorry, but there's no map, so there's no game. Goodbye.")

    def add_rooms(self):
        self.physical_rooms = []

        for current_room in ROOM:
            #new_room = Room(current_room)
            self.physical_rooms.append(current_room)

        #self.add_walls()

    def add_weapons(self):
        self.physical_weapons = []
        for current_weapon in WEAPON:
            self.physical_weapons.append(current_weapon)

    def add_players(self):
        self.physical_players = []
        for current_player in PLAYER:
            self.physical_players.append(current_player)

    def print_board(self):
        #print the board, one row at a time (trademark 2018)
        for current_row in self.rows: 
            #print each row
            for j, current in enumerate(current_row):
                #print the character for each square in each row
                print(current_row[j].get_char(), end = " ")
            print()

    def get_square_type(self, x_coordinate, y_coordinate):
        #returns the type of the square at a given location
        square_object = self.rows[x_coordinate][y_coordinate]
        square_type = square_object.get_type()
        return square_type

    def get_square_char(self, x_coordinate, y_coordinate):
        #returns the char of the square at a given location
        square_object = self.rows[x_coordinate][y_coordinate]
        square_char = square_object.get_char()
        return square_char

