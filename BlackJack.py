import random

suits = ('♥(Hearts)', '♦(Diamonds)', '♠(Spades)', '♣(Clubs)')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Player:
    def __init__(self):
        self.balance = 100
        self.hand_cards = []

    def balance_change(self, bet):
        self.balance += bet

    def hand_value(self):
        value = 0
        aces = 0
        for card in self.hand_cards:
            if card.rank == "Ace":
                aces += 1
            value += values[card.rank]
        if aces:
            for i in range(0, aces):
                if value > 21:
                    value -= 10
        return value

    def print_hand_cards(self):
        result = ""
        for card in self.hand_cards:
            result += "\n " + str(card)
        return result

    def add_card(self, card):
        self.hand_cards.append(card)

    def empty_hands(self):
        self.hand_cards = []

    def __str__(self):
        return "Hand Cards: " + self.print_hand_cards() + "\nThe total value is: " + str(self.hand_value())


def show_all_cards(p, d):
    print("Dealer cards and value:\n" + str(d))
    print("\nYour card and value:\n" + str(p))


def busted(p):
    if p.hand_value() > 21:
        return True
    return False


print("Hello and welcome to BlackJack")
player = Player()
dealer = Player()
print("your current total is " + str(player.balance))


while True:
    while True:
        try:
            bet = int(input("How much would you like to bet? "))
        except:
            print("invalid Input.\nThe input should be number")
        else:
            if bet > player.balance:
                print("Sorry not enough money.\nYour total is" + str(player.balance))
            else:
                break
    print("Ok lets begin")

    deck = Deck()
    deck.shuffle()
    player.empty_hands()
    dealer.empty_hands()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())

    show_all_cards(player, dealer)

    playing = True

    print("Player turn")
    while playing:
        player_play = input("Do you want to hit or stand? for hit press h and for stand press s ")

        if player_play == 'h':
            player.add_card(deck.deal())
            show_all_cards(player, dealer)
            if busted(player):
                print("Sorry you have lost")
                player.balance_change(-bet)
                playing = False

        elif player_play == 's':
            playing = False

        else:
            print("Not a valid input try again")

    if busted(player):
        playing = False
    else:
        playing = True

    print("Dealer Playing")
    while dealer.hand_value() < player.hand_value() and playing:
        dealer.add_card(deck.deal())
        show_all_cards(player, dealer)
        if busted(dealer):
            print("WOW the dealer just busted!!!!")
            player.balance_change(bet)
            playing = False
        elif player.hand_value() < dealer.hand_value() < 22:
            print("Dealer won good luck next time")
            player.balance_change(-bet)
        elif player.hand_value() == dealer.hand_value():
            print("It's a Tie")

    print("Your current total is " + str(player.balance))
    game = ""
    while True:
        game = input("Want another game? Please enter y or n ")
        if game == 'y':
            print("Ok and good luck")
            break
        elif game == 'n':
            print("OK coward See you next time")
            break
        else:
            print("Try again!!!")
    if game == 'n':
        break


