import csv, random


class BlackJack:
    deck = []
    with open("deck.csv") as deck_csv:
        deck_dict = csv.DictReader(deck_csv)
        for i in deck_dict:
            i["value"] = int(i["value"])
            deck.append(i)

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.total = 0

    def __repr__(self):
        return f"Hello and welcome to {self.name}!"

    def reset(self):
        self.cards, self.total = [], 0

    def draw_cards(self, num=1, player=None):
        for i in range(num):
            random_card = random.choice(self.deck)
            if type(player) is Player:
                player.cards.append(random_card)
                player.total += random_card["value"]
                self.deck.remove(random_card)
            elif player is None:
                self.cards.append(random_card)
                self.total += random_card["value"]
                self.deck.remove(random_card)

    def play(self, player, bet):
        self.draw_cards(2)
        self.draw_cards(2, player)
        # Main game loop
        if player.total == 21:
            print(f"BlackJack! +${3*bet}")
            player.chips += 3 * bet
            return
        while True:
            # Show dealers/players cards and totals
            print("dealer is showing:\n" + self.cards[0]["face"])
            print("Total: " + str(self.cards[0]["value"]))
            print("your cards are:")
            for i in player.cards:
                print(i["face"])
            print("Total: " + str(player.total))
            # get user input to select action
            choice = input("hit or stand? input 'h' or 's'\n").lower()
            while choice != "h" and choice != "s":
                choice = input(
                    "whoops, please enter either 'h' for hit or 's' for stand\n"
                )
            # "hit" logic
            if choice == "h":
                self.draw_cards(1, player)
                if player.total > 21:
                    print("your final cards:")
                    for i in player.cards:
                        print(i["face"])
                    print(f"Your Total: {player.total}")
                    print(f"Bust! Better luck next time!: -${bet}")
                    player.chips -= bet
                    return
                continue

            # "stand" logic
            if choice == "s":
                while self.total < 17:
                    self.draw_cards()

                print("dealers cards:")
                for i in self.cards:
                    print(i["face"])

                if (self.total > 21) or (self.total < 21 and self.total < player.total):
                    print(f"You win +${bet}")
                    print(f"Dealer Total: {self.total}\nYour Total: {player.total}")
                    player.chips += bet

                elif (self.total < 21) and (self.total > player.total):
                    print(f"Dealer wins -${bet}")
                    print(f"Dealer Total: {self.total}\nYour Total: {player.total}")
                    player.chips -= bet

                elif self.total == player.total:
                    print("Tie")

                else:
                    print("Error")

                return


class Player:
    def __init__(self, chips=100):
        self.cards = []
        self.chips = chips
        self.total = 0
        self.has_chips = self.chips > 0

    def __repr__(self):
        return f"you have ${self.chips} worth of chips"

    def reset(self):
        self.cards, self.total = [], 0


welcome_message = """
 /$$             /$$                              /$$                    
| $$            | $$                             | $$                    
| $$  /$$$$$$  /$$$$$$   /$$$$$$$        /$$$$$$ | $$  /$$$$$$  /$$   /$$
| $$ /$$__  $$|_  $$_/  /$$_____/       /$$__  $$| $$ |____  $$| $$  | $$
| $$| $$$$$$$$  | $$   |  $$$$$$       | $$  \ $$| $$  /$$$$$$$| $$  | $$
| $$| $$_____/  | $$ /$$\____  $$      | $$  | $$| $$ /$$__  $$| $$  | $$
| $$|  $$$$$$$  |  $$$$//$$$$$$$/      | $$$$$$$/| $$|  $$$$$$$|  $$$$$$$
|__/ \_______/   \___/ |_______/       | $$____/ |__/ \_______/ \____  $$
                                       | $$                     /$$  | $$
                                       | $$                    |  $$$$$$/
                                       |__/                     \______/ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'
  """
blackjack1 = BlackJack("Lets play: Blackjack")
print(welcome_message)
print("welcome to Lets play Blackjack!")
starting_chips = int(input("how many chips would you like to start with?\n"))

while type(starting_chips) != int:
    starting_chips = int(
        input(
            "How many chips would you like to start with? Please enter a round number.\n"
        )
    )

player1 = Player(starting_chips)
bet_size = int(
    input(
        "How much would you like to bet?\n",
    )
)

while type(bet_size) != int:
    bet_size = int(
        input("How much would you like to bet? Please enter a round number.")
    )

blackjack1.play(player1, bet_size)

play_again = input("Play again? y/n\n").lower()

while play_again == "y":
    blackjack1.reset()
    player1.reset()

    if player1.has_chips == False:
        print("Sorry, looks like youre out of chips. Better luck next time")
        break

    print(f"Your chips: {player1.chips}")
    bet_size = int(input("How much would you like to bet?\n"))

    while type(bet_size) != int:
        bet_size = int(
            input("How much would you like to bet? Please enter a round number.")
        )
    blackjack1.play(player1, bet_size)
    play_again = input("Play again? y/n\n").lower()


print("Thanks for playing!")
print(f"Starting chips: {starting_chips}")
print(f"Final chips: {player1.chips}")

if player1.chips >= starting_chips:
    print(f"Amount won:{player1.chips - starting_chips}")
else:
    print(f"Amount lost:{player1.chips - starting_chips}")
