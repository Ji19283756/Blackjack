from random import choice, shuffle, sample


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

    def shuffle(self):
        shuffle(self.cards)
        return self.cards

    def pick_a_card(self, amount, replace=True, taken_cards=[]):
        taken_cards = sample(self.cards, amount)

        return taken_cards

    def permanant_removal_pick_a_card(self, amount):
        drawn_card = sample(self.cards,amount)
        for card in drawn_card:
            self.cards.remove(card)

        return drawn_card

    def make_piles(self, amount):

        if amount > len(self.cards):
            print(f"I can't make {amount} piles")
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
        total_value = sum(map(get_card_value, self.cards))
        # for card in self.cards:
        #     total_value += get_card_value(card)
        self.card_value = total_value
        return total_value

    def is_not_bust(self):
        self.set_card_value()
        return self.card_value < 22

    def won(self):
        self.set_card_value()
        return self.card_value == 21


def play_black_jack():
    def ask_player_for_choice(enemy):
        game_will_be_done = False
        while True:
            try:
                player_decision = int(input(
                    "Do you want to draw another card?\nPrint only numbers\nOptions:"
                    "\n-(1)See total of your own cards\n-(2)See total of your opponent's cards"
                    "\n-(3)draw another card\n-(4)don't draw another card\n-(5)End game, opponent has"
                    " options to draw one more time\n").strip())
                if 1 <= player_decision <= 5:
                    print()
                    if player_decision == 1:
                        print("Your cards are:")
                        for card in player.cards:
                            print(card)
                        print(f"This means that your total is {player.card_value}\n")
                    elif player_decision == 2:
                        print("Your opponent's cards are:")
                        for card in enemy.cards:
                            print(card)
                        print(f"Your opponent's total is {enemy.card_value}\n")
                    elif player_decision == 3:
                        print("The dealer draws another card")
                        player.cards += deck.permanant_removal_pick_a_card(1)
                        print(f"You got {player.cards[-1]}")
                        player.set_card_value()
                        print(f"This gives you a total card value of {player.card_value}")
                    elif player_decision == 4:
                        print("You decide not to draw another card")
                    elif player_decision == 5:
                        print("You decide to end the game")
                        game_will_be_done = True

                    if 3 <= player_decision <= 5:
                        break

            except ValueError:
                print("Please print a valid number")

        return game_will_be_done

    def dealer_ai(real_player, self_dealer):
        dealer_amount = self_dealer.card_value
        dealer_game_will_be_done = False
        if dealer_amount < 19 or (dealer_amount >= 19 and (20 < real_player.card_value < 22)):
            print("The dealer draws another card")
            self_dealer.cards += deck.permanant_removal_pick_a_card(1)
            self_dealer.set_card_value()
            print(f"The dealer got {player.cards[-1]}\nThis gives him a total value of {self_dealer.card_value}")

        elif dealer_amount >= 19:
            print("The dealer decides to end the game")
            dealer_game_will_be_done = True

        return dealer_game_will_be_done

    deck = Deck()
    deck.shuffle()

    print("The dealer draws a card")
    drawn_card = deck.permanant_removal_pick_a_card(1)
    print(f"You got {drawn_card[0]}\n")
    player = Player(drawn_card)

    print("The dealer draws a card")
    drawn_card = deck.permanant_removal_pick_a_card(1)
    print(f"The dealer got {drawn_card[0]}\n")
    dealer = Player(drawn_card)

    player_game_will_be_done = False
    dealer_game_will_be_done = False
    while True:
        if player_game_will_be_done:
            break

        if player.is_not_bust():
            player_game_will_be_done = ask_player_for_choice(dealer)
        else:
            print("You went bust, your cards were:")
            for card in player.cards:
                print(card)
            print("Giving you a total of " + str(player.card_value) + " which means you lose")
            break
        if player.won() or not player.is_not_bust():
            break

        if dealer_game_will_be_done:
            break

        if dealer.is_not_bust():
            dealer_game_will_be_done = dealer_ai(player, dealer)
        else:
            break

        if dealer.won() or not dealer.is_not_bust():
            break

    def evaluate_winner(player1, dealer1):
        if 21 >= player1.card_value > dealer1.card_value:
            print("You win")
        elif 21 >= dealer1.card_value > player1.card_value:
            print("The dealer won")
        elif player1.card_value>21:
            print("You go bust\nYou Lose and the Dealer wins")
        elif dealer1.card_value>21:
            print("The dealer goes bust\nYou Win")
        else:
            print("Its a tie")
    evaluate_winner(player, dealer)


play_black_jack()

