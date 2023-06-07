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
                    break
                elif (self.total < 21) and (self.total > player.total):
                    print(f"Dealer wins -${bet}")
                    print(f"Dealer Total: {self.total}\nYour Total: {player.total}")
                    player.chips -= bet
                    break

                elif self.total == player.total:
                    print("Tie")

            # choice1 = input("Want to play again? y/n\n")
            # while choice1 != "y" and choice1 != "n":
            #   choice1 = input("Want to play again? Please enter 'y or n\n'")
            # if choice1 == "y":
            #   self.cards, player.cards = [], []
            #   self.total, player.total = 0, 0
            #   continue
            # elif choice1 == "n":
            #   print("Thanks for playing :)")
            #   break


class Player:
    def __init__(self, chips=100):
        self.cards = []
        self.chips = chips
        self.total = 0

    def __repr__(self):
        return f"you have ${self.chips} worth of chips"


blackjack1 = BlackJack("Lets play: Blackjack")
welcome_message = '''
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
  '''

print(welcome_message)
print("welcome to Lets play Blackjack!")
starting_chips = input("how many chips would you like to start with?")
player1 = Player(starting_chips) 

