from random import randint

'''Global Variables'''
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  
deck = cards * 4
user = []
comp = []

points_dict = { "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}

class Game:
    ''' A class that defines the go-fish game 

        Attributes
        ===========
        cards : list
            All types of cards in a deck of playing cards
        
        deck : list
            4 of each type of cards to make up a full deck of playing cards

        user : list
            Cards in user hand

        comp : list
            Cards in computer hand

        Methods
        =========
        draw_card() : 
            draws a single card and removes it from deck

            Returns : str
        
        deal_cards() : 
            deals cards for user and computer

        go_fish() : 
            Prints go fish and draws a card    

            Returns : str
    '''

    def __init__(self, cards, deck, user, comp):
        self.cards = cards
        self.deck = deck
        self.user = []
        self.comp = []

        ''' A constructor for the Game class

            Parameters
            ===========
            cards : list
                All types of cards in a deck of playing cards
        
            deck : list
                4 of each type of cards to make up a full deck of playing cards

            user : list
                Cards in user hand

            comp : list
                Cards in computer hand
        '''

    def draw_card() -> str:
        '''draws a single card and removes it from deck

            Returns : str 
        '''

        if len(deck) > 0: 
            card = deck[randint(0, len(deck)-1)]
            deck.remove(card)
            return card
        else:
            print("Deck is out of cards")       
            return None
    
    def deal_cards():
        '''deals cards for user and computer'''

        for i in range(7):
            user.append(Game.draw_card())
            comp.append(Game.draw_card())

        user.sort()

    def go_fish(hand:list) -> str:
        ''' Prints go fish and draws a card

            Parameters
            ===========
            hand : list
                Hand for player of current turn
            
            Return : str
        '''

        print("Go fish!")

        card = Game.draw_card()

        hand.append(card)
        hand.sort()

        if hand is user:
            print("Now adding " + card + " to you hand.")
        else:
            print("The computer has drawn a card.")

        return card


class Hand:
    ''' A class that defines interaction between player hands 

        Attributes
        ===========
            comp : list
                Cards in computer hand
            
            user : list
                Cards in user hand

            giver : list
                Hand of player card is being transferred from

            taker : list
                Hand of player card is being transferred to

            card : str
                Specific card being transferred from giver to taker

            card_counts : list
                Counts number of each card in user hand

            Returns : tuple

        Methods
        =========
            give_cards() : 
                Passes cards from one hand to another

                Returns : tuple
            
            display() : 
                Display the contents of the hands

            ask_user() : 
                Asks the user to request a card  

            ask_comp() : 
                Computer requests a card from the user 
    '''

    def __init__(self, comp, user):
        self.comp = comp
        self.user = user
        ''' Constructor for Hand class

            Parameters
            ===========
            comp : list
                Cards in computer hand
            
            user : list
                Cards in user hand
        '''

    def give_cards(giver:list, taker:list, card:str) -> tuple: 
        ''' Passes cards from one hand to another

            Parameters
            ===========
                giver : list
                    Hand of player card is being transferred from

                taker : list
                    Hand of player card is being transferred to

                card : str
                    Specific card being transferred from giver to taker
            
            Returns : tuple
        '''

        print("Transfering card " + card)

        while(card in giver):
            giver.remove(card)
            taker.append(card)

        taker.sort()

        return giver, taker

    def display():
        ''' Display the contents of the hands'''

        print("The computer has ", len(comp), " cards.")
        print("Your cards are: ")
        card_counts = []
        for card in set(user):
            card_counts.append((user.count(card), card)) 
        card_counts.sort(reverse = True)
        for pair in card_counts:
            print(pair[1], ":", pair[0]) 

    def ask_user():
        ''' Asks the user to request a card'''

        invalid = True

        while(invalid):

            print("What card would you like? ")

            resp = input("Enter one of your cards: " + str(set(user)) + ": ")
            resp = resp.upper() #addition to check lower cases as well

            if resp in user:
                invalid = False
            else:
                print("Invalid response")

        if resp in comp:
            print("Computer has card")
            Hand.give_cards(comp, user, resp) 
        else:
            print("Computer does not have card")
            Game.go_fish(user)

    def ask_comp():
        '''Computer requests a card from the user'''

        potential_cards = []
        for card in set(comp):
            count = comp.count(card)
            if count != 4: 
                potential_cards.append(card)

        if (len(potential_cards) > 0):
            index = randint(0, len(potential_cards) - 1)
            resp = potential_cards[index]
        else:
            # the computer has only books!
            resp = Game.comp[randint(0, len(comp) - 1)]


        print("The computer is requesting", resp)
        input("Press enter to continue. ")

        if resp in user:
            print("You have this card")
            Hand.give_cards(user, comp, resp)
        else:
            print("You do not have card")
            Game.go_fish(comp)
    
class Endgame:
    ''' A class that defines functions that occur at the end of the go-fish game 

        Attributes
        ===========
            user : list
                Cards in user hand

            comp : list
                Cards in computer hand

            card : str
                    Specific card in deck

            cards : list
                All types of cards in a deck of playing cards
            
            resp : str
                Takes in response from user on whether they want to play again or not
        
            comp_score : int
                Contains comp score
 
            user_score() : int
                Contains comp score

        Methods
        =========
            play_again() : 
                prompts user if they wish to play again

                Returns : bool
            
            is_game_over() : 
                Determines if game is over

                Returns : bool

            score() : str
                Scores players once game is over and determines winner
    '''
    def __init__(self, user, comp):
        self.user = user
        self.comp = comp
        ''' Constructor for Endgame class 

            Parameters
            ===========
                comp : list
                    Cards in computer hand
            
                user : list
                    Cards in user hand
        '''

    def play_again() -> bool:
        ''' prompts user if they wish to play again

            Returns : bool
        '''

        while(True):

            resp = input("Would you like to play again? (Y/N): ")
            resp = resp.upper()

            if resp == "Y":
                user.clear()
                comp.clear()

                for card in cards:
                    for i in range(4):
                        deck.append(card)
                        
                return True

            if resp == "N":
                return False
                

            print("Invalid input")

    def is_game_over():
        ''' Determines if game is over
        
            Returns : bool
        '''
        # check that deck is empty ?
        if len(deck) > 0:
            return False

        for card in set(comp):
            count = comp.count(card)
            if count != 4:
                return False

        for card in set(user):
            count = user.count(card)
            if count != 4:
                return False

        return True

    def score():
        ''' Scores players once game is over and determines winner'''
        
        comp_score = 0
        for card in set(comp):
            comp_score += points_dict[card]

        user_score = 0
        for card in set(user):
            user_score += points_dict[card]

        print("Your score is ", user_score)
        print("The computer's score is ", comp_score)

        if user_score > comp_score:
            print("You win! Well done!")
        elif user_score < comp_score:
            print("You lost. Better luck next time!")
        else:
            print("You tied! Good match!")

class start_game:
    ''' A class that prints welcome message 

        Methods
        =========
            welcome_message() : 
                Statement welcoming user and explaining game
    '''
    def welcome_message():
        '''Statement welcoming user and explaining game'''

        print('''Welcome to the best game 'Go Fish' ever - cuz this is Sakeena's version!
Here's what you need to know:
1. You're trying to collect "books" or 4 of as many cards as you can 
   (hint: there's only 4 of each card)

2. The score for books is based on the card
   - Aces are worth the highest & 2s are worth 
     the lowest (sorry 2s :_( )
                
Ok! That's it! Good luuuckkk :)
        
''')

 
if __name__ == "__main__":
    ''' Main method for go-fish program that runs go-fish

        Methods
        ========
        game() :
            Calls all methods to run through entire game of go-fish
    '''

    def game():
        """Runs a full game of go fish"""

        start_game.welcome_message()
        Game.deal_cards()

        while(not Endgame.is_game_over()):
            Hand.ask_user() #asks user to request card
            if Endgame.is_game_over():
                break
            input("Press enter to continue ")
            Hand.ask_comp() #asks computer to request card
            input("Press enter to continue ")
            Hand.display() #displays hand

        print("The game is over!")
        Endgame.score() 
        if Endgame.play_again():
            game()
    game()
    '''Calls method game'''



