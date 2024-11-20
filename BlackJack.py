#Procedural Programming Course Project - BlackJack
import random
def main():
   deck = init_deck()
   hand = [[], []] # one is player two is dealer
   
   for start_deal in range(2):
      hand[0].append(deal_a_card(deck))
      hand[1].append(deal_a_card(deck))
      return hand
      
def deal_a_card(deck):
   random_card = random.choice(deck)
   deck.remove(random_card)
   return random_card

def init_deck():
    deck = []
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J"]
    for suit in suits:
        for rank in ranks:
            if rank == "A":
                value = 11
            elif rank in ["K", "Q", "J"]:
                value = 10
            else:
                value = int(rank)
            cards = [[rank], [suit], [value]]
            deck.append(cards)
    return deck
   



   







if __name__ == "__main__":
   main()