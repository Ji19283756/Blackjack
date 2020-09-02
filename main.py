import random


class Deck:
    def __init__(self, joker=False):
        self.cards = \
            ['The Ace Of Hearts', 'The Ace Of Spades', 'The Ace Of Clubs', 'The Ace Of Diamonds',
             'The Two Of Hearts', 'The Two Of Spades', 'The Two Of Clubs', 'The Two Of Diamonds',
             'The Three Of Hearts', 'The Three Of Spades', 'The Three Of Clubs', 'The Three Of Diamonds',
             'The Four Of Hearts', 'The Four Of Spades', 'The Four Of Clubs', 'The Four Of Diamonds',
             'The Five Of Hearts', 'The Five Of Spades', 'The Five Of Clubs', 'The Five Of Diamonds',
             'The Six Of Hearts', 'The Six Of Spades', 'The Six Of Clubs', 'The Six Of Diamonds',
             'The Seven Of Hearts', 'The Seven Of Spades', 'The Seven Of Clubs', 'The Seven Of Diamonds',
             'The Eight Of Hearts', 'The Eight Of Spades', 'The Eight Of Clubs', 'The Eight Of Diamonds',
             'The Nine Of Hearts', 'The Nine Of Spades', 'The Nine Of Clubs', 'The Nine Of Diamonds',
             'The Ten Of Hearts', 'The Ten Of Spades', 'The Ten Of Clubs', 'The Ten Of Diamonds',
             'The Jack Of Hearts', 'The Jack Of Spades', 'The Jack Of Clubs', 'The Jack Of Diamonds',
             'The Queen Of Hearts', 'The Queen Of Spades', 'The Queen Of Clubs', 'The Queen Of Diamonds',
             'The King Of Hearts', 'The King Of Spades', 'The King Of Clubs', 'The King Of Diamonds']

        if joker:
            self.cards += ["Joker", "Joker"]

    def shuffle(self, new_order=[]):

        for x in range(len(self.cards)):
            rng = random.randint(0, len(self.cards) - 1)
            new_order += [self.cards[rng]]
            self.cards.remove(self.cards[rng])

        self.cards = new_order

        return self.cards

    def pick_a_card(self, amount, replace=True, taken_cards=[]):

        while len(taken_cards) < amount:
            random_card_position = random.randint(0, len(self.cards) - 1)
            drawn_card = self.cards[random_card_position]

            if not replace and drawn_card in taken_cards:
                continue

            taken_cards += [drawn_card]

        return taken_cards

    def permanant_removal_pick_a_card(self, amount):
        drawn_card = []
        for x in range(amount):
            random_card_position = random.randint(0, len(self.cards) - 1)
            drawn_card += [self.cards[random_card_position]]
            self.cards.pop(random_card_position)

        return drawn_card

    def make_piles(self, amount):

        if amount > len(self.cards):
            print("I can't make " + str(amount) + " piles")
            return

        all_piles = []
        current_pile = []

        # VVVV calculates the amount of cards in each pile
        pile_amount = (len(self.cards) / amount)
        pile_amount -= pile_amount % 1
        pile_amount = round(pile_amount)

        deck = self.shuffle()

        for x in range(amount):
            for y in range(pile_amount):
                current_pile += [deck[0]]
                deck.pop(0)
            all_piles += [current_pile]
            current_pile = []

        return all_piles


def get_card_value(name):
    value_dict = {'Ac': 14, 'Tw': 2, 'Th': 3, 'Fo': 4, 'Fi': 5, 'Si': 6, 'Se': 7, 'Ei': 8,
                  'Ni': 9, 'Te': 10, 'Ja': 11, 'Qu': 12, 'Ki': 13}
    two_first_letters = name[4:6]
    value = value_dict[two_first_letters]

    return value


class Player:
    def __init__(self, cards):
        self.cards = cards
        self.card_value = self.set_card_value()

    def set_card_value(self):
        total_value = 0
        # print("set_card_value")
        for card in self.cards:
            #    print(card)
            total_value += get_card_value(card)
        #    print(get_card_value(card))
        self.card_value = total_value
        # print("total"+str(total_value))
        return total_value

    def is_not_bust(self):
        self.set_card_value()
        if self.card_value < 22:
            return True
        return False

    def won(self):
        self.set_card_value()
        if self.card_value == 21:
            return True
        return False


def play_black_jack():
    def ask_player_for_choice(enemy):
        game_will_be_done = False
        while True:
            try:
                player_decision = int(input(
                    "Do you want to draw another card?\nPrint only numbers\nOptions:"
                    "\n-(1)See total of your own cards\n-(2)See total of your opponent's cards"
                    "\n-(3)draw another card\n-(4)don't draw another card\n-(5)End game, opponent has"
                    " options to draw one more time\n"))
                if 1 <= player_decision <= 5:
                    while True:
                        print()
                        if player_decision == 1:
                            print("Your cards are:")
                            for card in player.cards:
                                print(card)
                            print("This means that your total is " + str(player.card_value) + "\n")
                        elif player_decision == 2:
                            print("Your opponent's cards are:")
                            for card in enemy.cards:
                                print(card)
                            print("Your opponent's total is " + str(enemy.card_value) + "\n")
                        elif player_decision == 3:
                            print("The dealer draws another card")
                            player.cards += deck.permanant_removal_pick_a_card(1)
                            print("You got " + str(player.cards[-1]))
                            player.set_card_value()
                        elif player_decision == 4:
                            print("You decide not to draw another card")
                        elif player_decision == 5:
                            print("You decide to end the game")
                            game_will_be_done = True
                        break
                    #if player_decision == 3 or player_decision == 4 or player_decision == 5:
                    if 3 <= player_decision <= 5:
                        break

            except ValueError:
                print("Please print a valid number")
        return game_will_be_done

    deck = Deck()
    deck.shuffle()

    print("The dealer draws a card")
    drawn_card = deck.permanant_removal_pick_a_card(1)
    print("You got " + str(drawn_card[0]) + "\n")
    player = Player(drawn_card)

    print("The dealer draws a card")
    drawn_card = deck.permanant_removal_pick_a_card(1)
    print("The dealer got " + str(drawn_card[0]) + "\n")
    dealer = Player(drawn_card)
    game_will_be_done = False
    while True:
        if game_will_be_done:
            break

        if player.is_not_bust():
            game_will_be_done = ask_player_for_choice(dealer)
        else:
            print("You went bust, your cards were:")
            for card in player.cards:
                print(card)
            print("Giving you a total of " + str(player.card_value) + " which means you lose")
            break
        if player.won():
            print("You win")
            break

        # if dealer.is_not_bust():
        #    pass
        # else:
        #    break


play_black_jack()

# for pile in piles:
#    print(pile)
#    print(len(pile))
