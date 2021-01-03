#################################################################
#  CSE 231 Project 10
#
#  Classes
#       The rules of Basra is displayed
#       User is asked if they would like to play
#           If y or Y is inputted, game begins
#           If n or N is inputted, program quits
#       After game starts, cards are distributed to both players
#       Game alternates between player 1 and 2 until the deck is empty
#       After game ends, score and winner is displayed
#       User is asked if they would like to play again
#################################################################

from cards import Card
from cards import Deck
from itertools import zip_longest,chain,combinations #for displaying the table and sum

def distribute_cards(deck,p1_cards,p2_cards,t_cards,round1): #Function to distribute cards
    
    if round1 == True:
        for card_1 in range(4):
            p1_cards.append(deck.deal())
        for card_2 in range(4):
            p2_cards.append(deck.deal())
        for card_t in range(4):
            t_cards.append(deck.deal())
    else:
        for card_1 in range(4):
            p1_cards.append(deck.deal())
        for card_2 in range(4):
            p2_cards.append(deck.deal())

def get_card_index(card,cards_list): #Function to find where a card is located
    
    if card in cards_list:
        index = 0
        for cards in cards_list:
            if card == cards:
                return index
            else:
                index += 1
    else:
        return None

def get_matching_cards(card,t_cards): #Function to find matching cards
    
    matches = []
    for cards in t_cards:
        match = Card.equal_value(card,cards)
        if match == True:
            matches.append(cards)
        
    return matches

def numeric_card(card): #Function to find numeric cards
    
    rank = Card.rank(card)
    if rank <= 10:
        return True
    else:
        return False

def remove_cards(cards_list,cards): #Function to remove cards from decks
    
    for card in cards:
        if card in cards_list:
            index = get_card_index(card,cards_list)
            cards_list.remove(cards_list[index])

def get_sum_matching_cards(card,t_cards): #Function to get the sum of cards
    '''this function return a list of cards that add up to card rank,
    if the card is Jack, Queen or king, the function returns empty list'''

    matching_sum_list=[]
    numeric_list=[]

    # make a list of the numeric cards on the table
    if len(t_cards)>1:
        for i in t_cards:
            if numeric_card(i):
                numeric_list.append(i)

    # collect pairs of numeric cards that sum to card
    if len(numeric_list) > 1:
        # collect combinations of length 2, i.e. pairs, of cards
        # only if the ranks of the pair sum to card's rank
        matching_sum_pair = [seq for seq in combinations(numeric_list, 2) \
                         if seq[0].rank() + seq[1].rank() == card.rank()]
        # combine the list of lists into one list
        matching_sum_list = list(chain(*matching_sum_pair))
    
    return matching_sum_list


def sum_rank(cards): #optional
    
    card_sum = 0
    for card in cards:
        rank = Card.rank(card)
        card_sum += rank
    return card_sum

def jack_play(card,player,pile,basra,t_cards): #Function for when jack is played
    
    if t_cards == []:
        t_cards.append(card)
        player.remove(card)
    else:
        jacks = 0
        for cards in t_cards:
            rank = Card.rank(cards)
            jacks += rank
            pile.append(cards)
        t_cards.clear()
        if jacks % 11 == 0:
            basra.append(card)
        else:
            pile.append(card)
        player.remove(card)

def seven_diamond_play(card,player,pile,basra,t_cards): #Function for 7 of diamonds
    
    if t_cards == []:
        t_cards.append(card)
        player.remove(card)
    else:
        sums = sum_rank(t_cards)
        for cards in t_cards:
            pile.append(cards)
        t_cards.clear()
        if sums <= 10:
            basra.append(card)
        else:
            pile.append(card)
        player.remove(card)

def play(card,player,pile,basra,t_cards): #Function for when a card is played
    
    if t_cards == []:
        t_cards.append(card)
        player.remove(card)
    elif Card.rank(card) == 11:
        jack_play(card,player,pile,basra,t_cards)
    elif Card.rank(card) == 7 and Card.suit(card) == 2:
        seven_diamond_play(card,player,pile,basra,t_cards)
    elif Card.rank(card) > 11:
        match = get_matching_cards(card,t_cards)
        if match == []:
            t_cards.append(card)
        else:
            for cards in match:
                pile.append(cards)
            remove_cards(t_cards,match)
            if t_cards == []:
                basra.append(card)
            else:
                pile.append(card)
        player.remove(card)
    elif numeric_card(card) == True:
        count = 0
        matching = get_matching_cards(card,t_cards)
        sum_matching = get_sum_matching_cards(card,t_cards)
        if matching != []:
            for cards2 in matching:
                pile.append(cards2)
            remove_cards(t_cards,matching)
        else:
            count += 1
        if sum_matching != []:
            for cards3 in sum_matching:
                pile.append(cards3)
            remove_cards(t_cards,sum_matching)
        else:
            count += 1
        if count == 2:
            t_cards.append(card)
        if count <= 1:
            if t_cards == []:
                basra.append(card)
            else:
                pile.append(card)
        player.remove(card)

def compute_score(p1_pile,p2_pile,basra_1,basra_2): #Function to compute score
    
    player1_score = 0
    player2_score = 0
    if len(p1_pile) >= 27:
        player1_score += 30
    if len(p2_pile) >= 27:
        player2_score += 30
    for cards in basra_1:
        if numeric_card(cards) == True:
            player1_score += 10
        if Card.rank(cards) > 11:
            player1_score += 20
        if Card.rank(cards) == 11:
            player1_score += 30
    for cards in basra_2:
        if numeric_card(cards) == True:
            player2_score += 10
        if Card.rank(cards) > 11:
            player2_score += 20
        if Card.rank(cards) == 11:
            player2_score += 30
            
    return (player1_score,player2_score)
        
def display_table(t_cards,p1_cards,p2_cards):  #Function to display the table
    '''Display the game table.'''
    print("\n"+36*"=")
    print("{:^36s}".format('Player1'))
    print(9*" ", end = ' ')
    for card in p1_cards:
        print("{:>3s}".format(str(card)),end = ' ')
    print()
    print(9*" " + " {0[0]:>3d} {0[1]:>3d} {0[2]:>3d} {0[3]:>3d}".format(range(4)))
    table = zip_longest(*[iter(t_cards)]*4,fillvalue=0)
    hline = "\n" + 36*"-" 
    str_ = hline + '\n '
    for row in table:
        str_ += 9*" "
        for c in range(0, 4):
            str_ += ("{:>3s}".format(str(row[c])) \
                     if row[c] is not 0 else ' ') +' '
        str_ += '\n'
    str_ += hline + '\n '
    print (str_)

    print(9*" " + " {0[0]:>3d} {0[1]:>3d} {0[2]:>3d} {0[3]:>3d}".format(range(4)))
    print(9*" ", end = ' ')
    for card in p2_cards:
        print("{:>3s}".format(str(card)),end = ' ')
    print()
    print("{:^36s}".format('Player2'))
    print(36*"=")
            
    
def main(): #Function that brings all other functions together in one place
    '''main function'''
    RULES = '''
    Basra Card Game:
        This game belongs to a category of card games called “fishing cards games”. 
        Each player in turn matches a card from their hand with one (or more) of those 
        lying face-up on the table and then takes them. 
        If the card which the player played out does not match one of the existing cards, 
        it stays on the table.
    To win, you have to collect more points.'''
    
    print(RULES) 
    D = Deck()
    p1_cards = [] # card in hands player1
    p2_cards = [] #card in hands player2
    t_cards = []   # card on the floor
    p1_pile = [] # for player1
    p2_pile = [] # for player2
    basra_1 = []
    basra_2 = []
    p1_turn = (0,2,4,6)
    p2_turn = (1,3,5,7)
    game = True
    game_quit = False
    
    answer = input("Would you like to play? y/Y or n/N?")
    while answer!='n':
        print(" ---------Start The game--------")
        D.shuffle()
        while game == True: #replace by the correct condition
            for rounds in range(6):
                if rounds == 0:
                    distribute_cards(D,p1_cards,p2_cards,t_cards,True)
                    print('Dealing the cards, 4 cards for each player, 4 cards on the table')
                    print('Cards left:  {}'.format(D.__len__()))
                    display_table(t_cards,p1_cards,p2_cards)
                else:
                    distribute_cards(D,p1_cards,p2_cards,t_cards,False)
                    print('')
                    print('------Start new round-----')
                    print('Dealing the cards, 4 cards for each player')
                    print('Cards left:  {}'.format(D.__len__()))
                    display_table(t_cards,p1_cards,p2_cards)
                for turn in range(8):
                    while turn in p1_turn:
                        card_index = input("Player {:d} turn: -> ".format(1))
                        if card_index == 'q':
                            game = False
                            game_quit = True
                            break
                        try:
                            play(p1_cards[int(card_index)],p1_cards,p1_pile,basra_1,t_cards)
                        except:
                            print('Please enter a valid card index, 0 <= index <= {:d}'.format(len(p1_cards)-1))
                        else:
                            display_table(t_cards,p1_cards,p2_cards)
                            break
                    if game_quit == True:
                        break
                    while turn in p2_turn:
                        card_index = input("Player {:d} turn: -> ".format(2))
                        if card_index == 'q':
                            game = False
                            game_quit = True
                            break
                        try:
                            play(p2_cards[int(card_index)],p2_cards,p2_pile,basra_2,t_cards)
                        except:
                            print('Please enter a valid card index, 0 <= index <= {:d}'.format(len(p2_cards)-1))
                        else:
                            display_table(t_cards,p1_cards,p2_cards)
                            break
                    if game_quit == True:
                        break
                turn = 0
                if t_cards != []:
                    if game == True:
                        if turn in p1_turn:
                            p1_pile.append(t_cards)
                        else:
                            p2_pile.append(t_cards)
                        t_cards = []
                        display_table(t_cards,p1_cards,p2_cards)
                if game == False:
                    break
            if D.is_empty() == True:
                display_table(t_cards,p1_cards,p2_cards)
                score = compute_score(p1_pile,p2_pile,basra_1,basra_2)
                print('player 1:  {}'.format(score[0]))
                print('player 2:  {}'.format(score[1]))
                print('')
                if score[0] > score[1]:
                    print('Player 1 is the winner')
                    game = False
                else:
                    print('Player 2 is the winner')
                    game = False
                    
# useful strings to match tests (put them in a loop to reprompt on bad input)
# print('Please enter a valid card index, 0 <= index <= {:d}'.format(len(p1_cards)-1))
# card_index = input("Player {:d} turn: -> ".format(turn))

# remember to clear the data structures before the next game
# deck.reset()
# p1_cards.clear() # card in hands player1
# p2_cards.clear() #card in hands player2
# t_cards.clear()   # card on the floor
# p1_pile.clear() # pile for player1
# p2_pile.clear() # pile for player2
# basra_1.clear() # basra for player1
# basra_2.clear() #basra for player2
        if game_quit == True:
            break
        answer = input("Would you like to play? y/Y or n/N? ")
        if answer.lower() == 'y':
            D.reset()
            p1_cards.clear() # card in hands player1
            p2_cards.clear() #card in hands player2
            t_cards.clear()   # card on the floor
            p1_pile.clear() # pile for player1
            p2_pile.clear() # pile for player2
            basra_1.clear() # basra for player1
            basra_2.clear() #basra for player2
    print('Thanks for playing. See you again soon.')
    
    
      
# main function, the program's entry point
if __name__ == "__main__":
    main()