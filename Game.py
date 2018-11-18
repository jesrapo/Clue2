from constants import *
from Deck import *
from Board import *
from Window import *

'''
self.user_character
self.weapon_deck
self.player_deck
self.room_deck
self.board

'''

class Game:
    def __init__(self):
        self.set_up_game()
        #self.start_game()

    def set_up_game(self):

        self.user_character = self.get_user_character()
        self.make_decks()
        self.make_board()
        #print("PRINTING BOARD")
        #self.board.print_board()
        #print("BOARD JUST PRINTED")
        self.open_window()

        #not necessary
        #self.add_rooms_weapons_players_to_board()

        '''
        self.put_cards_in_confidential_file()
        self.deal_cards()
        self.put_extras_in_middle()
        self.start_game()
        '''
        #once done designing these, nest 'em all! cuz why not?!

    def open_window(self):
        size_x = self.board.get_board_size_x()
        size_y = self.board.get_board_size_y()
        game_window = Window(size_x, size_y, self.board)

    def get_user_character(self):
        return "Colonel Mustard"

    def make_decks(self):

        #make a shuffled weapons deck
        self.weapon_deck = Deck(WEAPON)

        #make players deck, shuffle
        self.player_deck = Deck(PLAYER)

        #make rooms deck, shuffle
        self.room_deck = Deck(ROOM)

        
    def make_board(self):
        self.board = Board(ROOM, WEAPON, PLAYER)
