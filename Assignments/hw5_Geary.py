# Shane T Geary
# CINF: 108
# 10/06/2025
# University at Albany

# Card Game - Core Program

# Import random Library for purpose of shuffling cards
import random

# Deck of cards defined as a dictionary called 'deck'.  Each card is identified
#  by a unique key between 1 - 52 (no Jokers).  The value of each card is list
#  containing 3 values:  The first item is the suit:
#   C = Clubs
#   H = Hearts
#   S = Spades
#   D = Diamonds
#  The second item is the face value of the card:  (2 - 10, J = Jack, Q = Queen, K = King, A = Ace)
#  The third item is the actual value of the card (J = 11, Q = 12, K = 13, and A = 14 for the purpose of the game).  

deck = {
    	1:['C','A',14], 2:['C','2',2], 3:['C','3',3], 4:['C','4',4], 5:['C','5',5], 6:['C','6',6], 7:['C','7',7], 8:['C','8',8], 
    	9:['C','9',9], 10:['C','10',10], 11:['C','J',11], 12:['C','Q',12], 13:['C','K',13], 14:['H','A',14], 15:['H','2',2],
        16:['H','3',3], 17:['H','4',4], 18:['H','5',5], 19:['H','6',6], 20:['H','7',7], 21:['H','8',8], 22:['H','9',9],
        23:['H','10',10], 24:['H','J',11], 25:['H','Q',12], 26:['H','K',13], 27:['S','A',14], 28:['S','2',2], 29:['S','3',3],
        30:['S','4',4], 31:['S','5',5], 32:['S','6',6], 33:['S','7',7], 34:['S','8',8], 35:['S','9',9], 36:['S','10',10],
        37:['S','J',11], 38:['S','Q',12], 39:['S','K',13], 40:['D','A',14], 41:['D','2',2], 42:['D','3',3], 43:['D','4',4],
        44:['D','5',5], 45:['D','6',6], 46:['D','7',7], 47:['D','8',8], 48:['D','9',9], 49:['D','10',10], 
        50:['D','J',11], 51:['D','Q',12], 52:['D','K',13]
    }

# Create a list containing the keys for the 52 cards
unshuffled = list(deck.keys())

# Shuffle this list of keys (which will then refer to the cards listed above in randome order)
shuffled = random.sample(unshuffled, len(unshuffled))

# For testing only -- please remove comments / add back in for you verify understanding
'''
print("Here's the shuffled deck keys:\n", shuffled, '\n')
'''

# Number of cards in each hand (for War, each player gets 1/2 of the deck)
num_cards = int(len(shuffled)/2)

# Deal the cards to the two players (user and computer player)
user_hand = []
computer_hand = []
for draw in range(num_cards):
    user_hand.append(shuffled.pop(0))
    computer_hand.append(shuffled.pop(0))

# For testing only -- please remove comments / add back in for you verify understanding
"""
print("Player's hand:")
for card in user_hand:
    print(deck[card], end=' ')
print('\n')

print("Computer's hand:")
for card in computer_hand:
    print(deck[card], end=' ')
print('\n')
"""

# ----- STOP commenting out ---------

# Begin program -- The Card Game of War

# Write a loop to iterate through each play of the game:
#  show the user's next card next to the computer player's next card.  Say who wins and then:
#  if the user wins, they keep their card and add to the END of their list of cards AND they get to
#  keep the computer's card as well (also place at END of list)
#  If the computer player wins, do the opposite.
#  If both players draw the same-valued card, discard both
#  Once one player is out of cards, end the game and state the winner.  Note that it may also be possible (depending
#   on the shuffle) that nobody wins the game and it goes on forever.  If you suspect this happening, just run your
#   program again and start a new game.

'''
The rest of the program you will write goes here
'''

gameEnd = False # Flag to begin and end game loop
nextRound = True # Flag to begin and end round instance

while not gameEnd: # Begin game loop
    if nextRound: # Begin game round instance
        drawPlayerCard = deck[user_hand[0]] # Find first card in user's hand
        
        drawComputerCard = deck[computer_hand[0]] # Find first card in computer's hand
        print(f'Your card: {drawPlayerCard[0] + drawPlayerCard[1]}')
        print(f'Computer player card: {drawComputerCard[0] + drawComputerCard[1]}')
        
        if drawPlayerCard[2] > drawComputerCard[2]:
            user_hand.append(user_hand.pop(0))
            user_hand.append(computer_hand.pop(0))
            print('You won this round - cards added to the end of your pile')
            print(f'Player cards: {len(user_hand)} Computer cards: {len(computer_hand)}')
            nextRound = False
        elif drawComputerCard[2] > drawPlayerCard[2]:
            computer_hand.append(computer_hand.pop(0))
            computer_hand.append(user_hand.pop(0))
            print('Computer has won this round - cards added to the end of its pile')
            print(f'Player cards: {len(user_hand)} Computer cards: {len(computer_hand)}')
            nextRound = False
        elif drawPlayerCard[2] == drawComputerCard[2]:
            user_hand.pop(0)
            computer_hand.pop(0)
            print('Draw! Both cards discarded')
            print(f'Player cards: {len(user_hand)} Computer cards: {len(computer_hand)}')
            nextRound = False

    elif len(user_hand) == 0:
        print('Computer won the game!')
        gameEnd = True
    elif len(computer_hand) == 0:
        print('You won the game!')
        gameEnd = True
    else:
        playerInput = input('Hit P to play next round or Q to QUIT: ')
        if playerInput == 'p':
            print('Next round')
            nextRound = True
        elif playerInput == 'q':
            print('Game end \n')
            gameEnd = True