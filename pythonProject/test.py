from symtable import Class

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
from random import shuffle
ranks_to_value = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
                      'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = ranks_to_value[rank]

    def __str__(self):
        return self.rank + ' ' + self.suit



class Deck:
    def __init__(self):
        self.all_cards = []
    def makeDeck(self):
        for suit in suits:
            for rank in ranks_to_value.keys():
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

class Bankroll:
    def __init__(self,money):
        self.money = money
        self.bet = 0
    def make_bet(self,bet):
        self.bet = bet
        self.money -= bet
    def win(self):
        self.money += (self.bet * 2)
    def tie(self):
        self.money += self.bet
    def __str__(self):
        return 'You have ' + str(self.money) + ' dollars'

class PlayerHand:
    def __init__(self):
        self.hand = [card_deck.deal(),card_deck.deal()]

    def hit(self):
        self.hand.append(card_deck.deal())

class DealerHand():
    def __init__(self):
        self.comp_hand=[card_deck.deal(),card_deck.deal()]
    def dealer_hit(self):
        self.comp_hand.append(card_deck.deal())

if __name__ == '__main__':
    bank = Bankroll(int(input('Please Enter Your Total Money: ')))
    while True:
        dealer_plays = True
        my_summation = 0
        ace_amount = 0
        card_deck = Deck()
        card_deck.makeDeck()
        card_deck.shuffle()
        if input('Would you like to play now?(Y or N)  ') == 'Y'.lower():
            bank.make_bet(int(input('Please enter the amount you would like to bet: ')))
        else:
            break
        my_hand = PlayerHand()
        other_hand = DealerHand()
        print("The Dealer's first card is a " + other_hand.comp_hand[0].__str__())
        while True:
            print('Your current cards are: ')
            for card in my_hand.hand:
                print(card)
            hit_stand = input('Would you like to hit or stand?("Hit" or "Stand) ')
            if hit_stand.lower() == 'hit':
                my_hand.hit()
                print('You got a ' + my_hand.hand[-1].__str__())
            else:
                for card in my_hand.hand:
                    my_summation += card.value
                    if card.rank == 'Ace':
                        ace_amount += 1
                if my_summation > 21 and ace_amount > 0:
                    my_summation -= (ace_amount * 10)
                    ace_amount = 0
                break
            my_summation = 0
            for card in my_hand.hand:
                my_summation += card.value
                if card.rank == 'Ace':
                    ace_amount +=1

            if my_summation > 21:
                if ace_amount == 0:
                    print('Sorry you lost')
                    dealer_plays = False
                    print(bank)
                    break
                else:
                    my_summation -= (ace_amount *10)
                    ace_amount = 0
                if my_summation > 21:
                    print('Sorry you lost')
                    dealer_plays = False
                    print(bank)
                    break


        while dealer_plays:
            d_ace_amount = 0
            other_summation = 0
            print('The Dealer has: ')
            for card in other_hand.comp_hand:
                print(card)
                other_summation += card.value
                if card.rank == 'Ace':
                    d_ace_amount +=1
            if other_summation > 21:
                if d_ace_amount == 0:
                    print('YOU WON')
                    bank.win()
                    print(bank)
                    break
                else:
                    other_summation -= 10
                    d_ace_amount -= 1
            if other_summation > my_summation:
                print('Sorry you lost')
                print(bank)
                break
            if other_summation == my_summation == 21:
                print('You tied')
                bank.tie()
                print(bank)
                break
            elif my_summation > other_summation:
                other_hand.dealer_hit()
                print('The dealer got a ' + other_hand.comp_hand[-1].__str__())













