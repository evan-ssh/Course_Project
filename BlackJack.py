#Procedural Programming Course Project - BlackJack
import random
def main():
 deck = []
 suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
 ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J"]
 for suit in suits:
    for rank in ranks:
        if rank in ["A"]:
           value = 11
        elif rank in ["K", "Q", "J"]:
           value = 10
        else:
            value = int(rank)
        cards = (suit, rank, value)
        deck.append(cards)

 dealers_cards = []
 dealer_cards = random.choice(deck)
 dealers_cards.append(dealer_cards)
 deck.remove(dealer_cards)
 dealer_card_value =  sum(card[2] for card in dealers_cards)  
 print(f"Dealers cards: {dealers_cards}")
 print(f"Value: {dealer_card_value}")
 
 players_cards = []
 for _ in range(2):
    player_cards = random.choice(deck)
    players_cards.append(player_cards)
    deck.remove(player_cards)
 player_card_value =  sum(card[2] for card in players_cards)  
 print(f"Your cards: {players_cards}")
 print(f"Value: {player_card_value}")
 player_turn = input("Would u like to 'Hit' or 'Stand'? ")
 if player_turn.lower() == "hit" or "h":
    player_cards = random.choice(deck)
    players_cards.append(player_cards)
    dealer_cards = random.choice(deck)
    dealers_cards.append(dealer_cards)
    if player_card_value > dealer_card_value:
       print("you have won")
    else:
       print("Dealer wins")
 elif player_turn.lower() == "stand" or "s":
    dealer_cards = random.choice(deck)
    dealers_cards.append(dealer_cards)
    if player_card_value < dealer_card_value:
       print("you have won")
    else: 
       print("Dealer wins")
 else:
    pass
 





if __name__ == "__main__":
   main()