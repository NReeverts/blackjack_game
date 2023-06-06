import random, csv
#You got this
class Games:
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
      if player is not None:
        player.cards.append(random_card)
        player.total += random_card["value"]
        self.deck.remove(random_card)
      else:
        self.cards.append(random_card)
        self.total += random_card["value"]
        self.deck.remove(random_card)
      
      
  def play_roulette(self,player, num, bet=20):
    roulette_nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    random_num = random.choice(roulette_nums)
    print("The Roulette Gods chose a {random_num}")
    if num == random_num:
      print("YOU WIN +${bet*len(roulette_nums)}")
      player.chips += len(roulette_nums) * bet
    else:
      print("Sorry. Not today -${bet}")
      player.chips -= bet


  def play_bj(self, player, bet):
    self.draw_cards(2)
    self.draw_cards(2, player)
    # Main game loop
    while True:
      #Reset from prev hand
      #Show dealers/players cards and totals
      print("dealer is showing:\n" + self.cards[0]["face"])
      print("Total: "+str(self.cards[0]["value"]))
      print("your cards are:")
      for i in player.cards:
        print(i["face"])
      
      print("Total: " + str(player.total))
      #get user input to select action
      choice = input("hit or stand? input 'h' or 's'\n").lower()
      while choice != "h" and choice != "s":
        choice = input("whoops, please enter either 'h' for hit or 's' for stand\n")
      #"hit" logic
      if choice == "h":
        self.draw_cards(1, player)
        if player.total > 21:
          print("your final cards:")
          for i in player.cards:
            print(i["face"])
          print(f"Bust! Better luck next time!: -${bet}")
          player.chips -= bet
          continue
        
      #"stand" logic
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

  def __init__(self, name, chips=100):
    self.name = name
    self.cards = []
    self.chips = chips
    self.total = 0
  
  def __repr__(self):
    return f"{self.name} has ${self.chips} worth of chips"

  def show_hand(self):
    i=1
    for card in self.cards:
      print(f"{i}. The {card['face']} of {card['suit']}, Blackjack value: {card['value']}")
      i += 1

  def add_chips(self, num):
    self.chips += num
    print("New Balance: ${self.chips}")

  def im_done(self):
    print("Im done")




casino1 = Games("Billy Bobs Backwoods Casino")
casino2 = Games("I can't think of a good name")
player1 = Player("Noah")
player2 = Player("Not Noah")
# casino.play_bj(player1, 20)

