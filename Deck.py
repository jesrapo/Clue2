from random import randint

class Deck:
    #a deck of cards

    def __init__(self, list_of_cards = None):
        #make an empty deck
        self.card_list = []
        self.deck_size = 0

        #if there's a list of cards given, load them all in
        if(list_of_cards):
            for current_card in list_of_cards:
                self.add_card(current_card)

        #shuffle the deck
        self.shuffle()

    def add_card(self, card_name):
        self.card_list.append(card_name)
        self.deck_size += 1

    def print_deck(self):
        for current_card in self.card_list:
            print(current_card)

    def draw_card(self):
        #takes the top card, removes it, and returns its value
        self.deck_size -= 1

    def get_deck_size(self):
        return self.deck_size

    def shuffle(self):
        #randomly re-arranges the contents of the deck
        new_deck = []
        new_deck_size = 0
        
        #move each card to a new deck, deleting it as you go and changing the deck size of both accordingly
        while(self.deck_size > 0):
            #choose a random card from the current deck
            upper = self.deck_size - 1
            random_card_number = randint(0, upper)
            random_card = self.card_list[random_card_number]

            #delete that card from the old deck
            del self.card_list[random_card_number]
            self.deck_size -= 1

            #add that card to the new deck
            new_deck.append(random_card)
            new_deck_size += 1

        #set the old deck to the new deck, size and contents
        self.deck_size = new_deck_size
        self.card_list = new_deck
        
