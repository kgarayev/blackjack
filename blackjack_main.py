import random

# creating a card class
# a blueprint for one single card in a game (deck)
class Card:

    def __init__(self, suit, value):

        # protected instance attributes
        self._suit = suit
        self._value = value

    
    # configuring the getter (no need for the setter, since no need to change once initialised)
    # read-only attribute
    @property
    def suit(self):
        return self._suit

    # read-only attribute
    @property
    def value(self):
        return self._value

    # a method to display the card
    def show(self):
        print(f"{self._value} of {self._suit}")


# creating a deck class
class Deck:

    # defining a class attribute
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
    
    # initialising, but not taking any arguments as an input
    def __init__(self):

        # instance attribute, protected
        # no need for getters or setters - no need to access this externally
        self._cards = []

        # after creating an instance (above), build the deck immediately by calling a build method
        # a build method is defined below
        self.build()

    # build method - to build a deck
    def build(self):

        # iterating through a class attribute suits
        for suit in Deck.suits:
            for value in Deck.values:
                # creating a card instance with a suit and a value
                # appending this instance into the list of cards in the deck that is being built
                # to build a deck by appending the instances of a Card class
                self._cards.append(Card(suit, value))

    # show a deck
    def show(self):
        for card in self._cards:
            # call a show method of a card instance (which belongs to a Card class defined above)
            card.show()
    
    # shuffling all cards in a deck using a Fisher-Yates Shuffle Algorithm
    def shuffle(self):

        # iterate from total number of cards (minus 1) until card 1 (decrementing)
        for i in range(len(self._cards)-1, 0, -1):

            # use random mobule to generate a random number
            rand = random.randint(0, i)

            # swap the card in the "rand" position with the card in the "i" position
            self._cards[i], self._cards[rand] = self._cards[rand], self._cards[i]

    
    # defining a method to draw a card from a deck
    def draw(self):

        # if a deck is not empty
        if self._cards:
            
            # remove a card from the deck and return the card that has been removed
            return self._cards.pop()

    
# Player class:
class Player:

    # initialising is_dealer as False (by default a regular player is not a dealer unless otherwise specified)
    def __init__(self, name, is_dealer=False):

        self._name = name

        # cards of each player, protected
        self._hand = []
        self._is_dealer = is_dealer

    # a getter for the name (no need for a setter)
    @property
    def name(self):
        return self._name

    # a getter for the is_dealer attribute:
    @property
    def is_dealer(self):
        return self._is_dealer

    
    # defining a draw method
    # for a player to draw a card from a specific deck
    def draw(self, deck):

        # appending a card instance from a deck (popped from the deck and appended to the hand)
        self._hand.append(deck.draw())

        # return itself (recursively) to then be able to chain the methods
        return self
    
    # a show hand method (in a user-friendly format)
    def show_hand(self, reveal_card=False):

        # if a player is not a dealer, then show each card in the player's hand
        if not self.is_dealer:
            for card in self._hand:
                card.show()
        else:
            # reveal the first card, and the second is going to be hinnden
            for i in range(len(self._hand)-1):
                self._hand[i].show()

            # if the reveal_card argument is True, then dealer can reveal the card
            if reveal_card:
                self._hand[-1].show()
            else:
                print("X")
    
    # define a method to discard a card
    def discard(self):
        return self._hand.pop()

    # define the method to find the total value of a hand of a player
    def get_hand_value(self):

        # 8 different potential values (if all 4No. Aces are drawn)
        value1 = 0
        value2 = 0
        value3 = 0
        value4 = 0
        value5 = 0
        value6 = 0
        value7 = 0
        value8 = 0

        # add the values
        for card in self._hand:
            card_content = card.value

            # check if the card content (value) is numerical (integer), then add to the value
            if isinstance(card_content, int):
                if value2 == 0:
                    value1 += card_content

                elif value3 == 0:
                    value1 += card_content
                    value2 += card_content
                
                elif value5 == 0:
                    value1 += card_content
                    value2 += card_content
                    value3 += card_content
                    value4 += card_content
                
                else:
                    value1 += card_content
                    value2 += card_content
                    value3 += card_content
                    value4 += card_content
                    value5 += card_content
                    value6 += card_content
                    value7 += card_content
                    value8 += card_content

            # if the card has a letter value
            else:

                # if the letter is A (ace)
                # split the sum to count Ace as both 1 and 11

                if card_content == "A":
                    if value2 == 0:
                        value2 = value1
                        value1 += 1
                        value2 += 11

                    elif value3 == 0:
                        value3 = value1
                        value4 = value2
                        value1 += 1
                        value2 += 1
                        value3 += 11
                        value4 += 11

                    elif value5 == 0:
                        value5 = value1
                        value6 = value3
                        value7 = value2
                        value8 = value4
                        value1 += 1
                        value2 += 1
                        value3 += 1
                        value4 += 1
                        value5 += 11
                        value6 += 11
                        value7 += 11
                        value8 += 11

                # otherwise, just add 10 (corresponding to J, Q, K)
                else:
                    if value2 == 0:
                        value1 += 10

                    elif value3 == 0:
                        value1 += 10
                        value2 += 10
                
                    elif value5 == 0:
                        value1 += 10
                        value2 += 10
                        value3 += 10
                        value4 += 10
                
                    else:
                        value1 += 10
                        value2 += 10
                        value3 += 10
                        value4 += 10
                        value5 += 10
                        value6 += 10
                        value7 += 10
                        value8 += 10


        # construct the list of potential final values
        final_value = [value1, value2, value3, value4, value5, value6, value7, value8]

        return final_value


# define the main class (logic) of the game
class CardGame:
    INSTRUCTIONS = """\n | Welcome to our version of the Blackjack Game |
=================================================================================
The goal is to get as close to 21 as possible, without going over 21. 
Each card has a value and a suit. The values are added for the final result.

The game starts by dealing two cards to the player (you) and to the dealer.            
You are playing against the dealer. On each turn, you must choose if you
would like to take another card or stand to stop the game and see if you won.

The game ends if the total value of the player's hand goes over 21,
and if the total value of the hand is below 21, the game continues
until the player chooses to stand.

When the game ends or when the player chooses to stand,
the total value of each hand is calculated.  
The value that is closest to 21 without going over it wins the game.
If the total value is over 21, the player or dealer automatically lose the game.
=================================================================================
"""

    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

        # call a method (written below) to start the game
        self.start_game()

    
    # define a start game method
    def start_game(self):

        # display the instructions
        print(CardGame.INSTRUCTIONS)

        # initialise a turn counter
        turn = 1

        # shuffle the cards in the deck
        self.deck.shuffle()

        # method chaining
        # draw cards twice, one after another
        self.player.draw(self.deck).draw(self.deck)
        self.dealer.draw(self.deck).draw(self.deck)

        # add an infinite loop because the number of turns is unknown
        while True:

            # display the turn number
            print(f"== Turn No.: {turn} ==")

            # display the Dealer's hand
            print("\nThe Dealer's Hand is: ")
            self.dealer.show_hand()

            # display the Player's hand
            print("\nYour Hand is: ")
            self.player.show_hand()

            # obtain the values for the cards
            hand1 = self.player.get_hand_value()[0]
            hand2 = self.player.get_hand_value()[1]
            hand3 = self.player.get_hand_value()[2]
            hand4 = self.player.get_hand_value()[3]
            hand5 = self.player.get_hand_value()[4]
            hand6 = self.player.get_hand_value()[5]
            hand7 = self.player.get_hand_value()[6]
            hand8 = self.player.get_hand_value()[7]

            # check 
            if hand2 == 0:
                if hand1 > 21:
                    print("\nThe total value of your hand is over 21. You lost.")
                    break
            elif hand3 == 0:
                if (hand1 > 21) and (hand2 > 21):
                    print("\nThe total value of your hand is over 21. You lost.")
                    break
            elif hand5 == 0:
                if (hand1 > 21) and (hand2 > 21) and (hand3 > 21) and (hand4 > 21):
                    print("\nThe total value of your hand is over 21. You lost.")
                    break
            else:
                if (hand1 > 21) and (hand2 > 21) and (hand3 > 21) and (hand4 > 21) and (hand5 > 21) and (hand6 > 21) and (hand7 > 21) and (hand8 > 21):
                    print("\nThe total value of your hand is over 21. You lost.")
                    break            

            if (hand1 == 21) or (hand2 == 21) or (hand3 == 21) or (hand4 == 21) or (hand5 == 21) or (hand6 == 21) or (hand7 == 21) or (hand8 == 21):
                print("\nYou have a BackJack!")
                break

            # assign the choice of a player
            choice = self.ask_choice()

            # increment the turn
            turn += 1

            # understand the choice and act
            if choice == 1:
                self.player.draw(self.deck)
            else:
                break

        # obtain value(s) of the player's hand
        phand1 = self.player.get_hand_value()[0]
        phand2 = self.player.get_hand_value()[1]
        phand3 = self.player.get_hand_value()[2]
        phand4 = self.player.get_hand_value()[3]
        phand5 = self.player.get_hand_value()[4]
        phand6 = self.player.get_hand_value()[5]
        phand7 = self.player.get_hand_value()[6]
        phand8 = self.player.get_hand_value()[7]

        # print out the value(s) of a player's hand
        if phand2 == 0:
            print(f"\nValue of your hand is: {phand1}")
        
        elif phand3 == 0:
            if phand2 > 21:
                print(f"\nValue of your hand is: {phand1}")
            else:
                print(f"\nValue of your hand is: {phand1} and/or {phand2}")

        elif phand5 == 0:
            print(f"\nValue of your hand is: {phand1} and/or {phand2} and/or {phand3} and/or {phand4}")
            
        else:
            print(f"\nValue of your hand is: {phand1} and/or {phand2} and/or {phand3} and/or {phand4} and/or {phand5} and/or {phand6} and/or {phand7} and/or {phand8}")


        # obtain value(s) of the dealer's hand
        dhand1 = self.dealer.get_hand_value()[0]
        dhand2 = self.dealer.get_hand_value()[1]
        dhand3 = self.dealer.get_hand_value()[2]
        dhand4 = self.dealer.get_hand_value()[3]
        dhand5 = self.dealer.get_hand_value()[4]
        dhand6 = self.dealer.get_hand_value()[5]
        dhand7 = self.dealer.get_hand_value()[6]
        dhand8 = self.dealer.get_hand_value()[7]

        # print the value(s) of the dealer's hand
        if dhand2 == 0:
            print(f"\nValue of Dealer's hand is: {dhand1}")
        
        elif dhand3 == 0:
            if dhand2 > 21:
                print(f"\nValue of Dealer's hand is: {dhand1}")
            else:
                print(f"\nValue of Dealer's hand is: {dhand1} and/or {dhand2}")

        elif dhand5 == 0:
            print(f"\nValue of Dealer's hand is: {dhand1} and/or {dhand2} and/or {dhand3} and/or {dhand4}")
            
        else:
            print(f"\nValue of Dealer's hand is: {dhand1} and/or {dhand2} and/or {dhand3} and/or {dhand4} and/or {dhand5} and/or {dhand6} and/or {dhand7} and/or {dhand8}")

        print("\nThe Dealer's Hand was: ")
        self.dealer.show_hand(True)

 
        # checking player's hand for more than 21
        if phand2 == 0:
            if phand1 > 21:
                print("\nThe total value of your hand is over 21. You lost.")
                return
        elif phand3 == 0:
            if (phand1 > 21) and (phand2 > 21):
                print("\nThe total value of your hand is over 21. You lost.")
                return
        elif phand5 == 0:
            if (phand1 > 21) and (phand2 > 21) and (phand3 > 21) and (phand4 > 21):
                print("\nThe total value of your hand is over 21. You lost.")
                return
        else:
            if (phand1 > 21) and (phand2 > 21) and (phand3 > 21) and (phand4 > 21) and (phand5 > 21) and (phand6 > 21) and (phand7 > 21) and (phand8 > 21):
                print("\nThe total value of your hand is over 21. You lost.")
                return


        # checking dealer's hand for more than 21
        if dhand2 == 0:
            if dhand1 > 21:
                print("\nYou win! Congratulations!")
                return
        elif dhand3 == 0:
            if (dhand1 > 21) and (dhand2 > 21):
                print("\nYou win! Congratulations!")
                return
        elif dhand5 == 0:
            if (dhand1 > 21) and (dhand2 > 21) and (dhand3 > 21) and (dhand4 > 21):
                print("\nYou win! Congratulations!")
                return
        else:
            if (dhand1 > 21) and (dhand2 > 21) and (dhand3 > 21) and (dhand4 > 21) and (dhand5 > 21) and (dhand6 > 21) and (dhand7 > 21) and (dhand8 > 21):
                print("\nYou win! Congratulations!")    
                return      

        
        # making a list of potential values for player and dealer
        player_hand = [phand1, phand2, phand3, phand4, phand5, phand6, phand7, phand8]

        # discarding the values more than 21
        for item in player_hand:
            if item > 21:
                item = 0
            else:
                continue
        
        # making a list of potential values for player and dealer
        dealer_hand = [dhand1, dhand2, dhand3, dhand4, dhand5, dhand6, dhand7, dhand8]

        # discarding the values more than 21
        for item in dealer_hand:
            if item > 21:
                item = 0
            else:
                continue
        
        
        # identifying the maximum value up to 21 for player and dealer
        max_player = max(player_hand)
        max_dealer = max(dealer_hand)

        # checking the final conditions to decide the winner
        if max_player == 21 or max_player > max_dealer:
            print("\nYou win! Congratulations!")
        elif max_dealer > max_player:
            print("\nYou lose.")
        else:
            print("\nWe have a tie.")

    # defining the choice selection method
    def ask_choice(self):
        print("\nWhat do you want to do?")
        print("1 - Ask for another card")
        print("2 - Stand")
        
        # infinite loop until the input is correct
        while True:
            choice = int(input("\nPlease enter your choice (1 or 2): "))
            if choice != 1 and choice != 2:
                continue
            else:
                break
        
        return choice


# the main body of the programm
# create instances deck, player, dealer and the game

deck = Deck()

ad = input("What is your name? ")
you = Player(ad)

dealer = Player("Dealer", True)
game = CardGame(deck, you, dealer)