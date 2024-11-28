#Procedural Programming Course Project - BlackJack
import random
def main():      
 while True:

    deck = init_deck()
    hand = [[], []] # one is player, two is dealer 
    for start_deal in range(2): #initial deal of two cards to player and dealer
            hand[0].append(deal_a_card(deck))
            hand[1].append(deal_a_card(deck))
            
    print("\nDEALERS SHOW CARDs:")
    print(f"{hand[1][0][0]} of {hand[1][0][1]}")
    player_turn(hand,deck) 
    dealers_turn(hand, deck)
    players_hand_score = hand_score(hand[0])
    dealer_hand_score = hand_score(hand[1])
    show_dealer_cards(hand)
    print(f"\nYour points: {players_hand_score}")
    print(f"\nDealers points: {dealer_hand_score}")
    win_game(players_hand_score, dealer_hand_score)
    ###############################################
   
    restart_game = input("Play again? (y/n): ")
    if restart_game.lower() in ["yes", "y"]:
        continue
    elif restart_game.lower() in ["no", "n"]:
        print("\nCome back soon!")
        print("Bye!")
        break
    else:
        print("Please enter 'y' or 'n'")
      

def show_dealer_cards(hand):
      print("\nDEALERS CARDS:")
      print(hand[1])

def show_players_cards(hand):
     print("\nYOUR CARDS:")
     print(hand[0])
       


  
def player_turn(hand, deck):
 while True:
     players_hand_score = hand_score(hand[0])
     show_players_cards(hand)
     print(f"\nYour points: {players_hand_score}")
     if players_hand_score > 21:
         print("BUSTED, Dealer wins!")
         break
        
     player_turn = input("Hit or Stand (H/S: )")
     if player_turn.lower() in ["hit", "h"]:
         hand[0].append(deal_a_card(deck))
         
         
     elif player_turn.lower() in ["stand", "s"]:
         break
     else:
         print("Please choose hit or stand")

   
       

def dealers_turn(hand, deck):
    while True:
        dealers_hand_score = hand_score(hand[1])
        print("\nDEALERS TURN:")
        show_dealer_cards(hand)

        if dealers_hand_score < 17:
            print("DEALER HITS!")
            hand[1].append(deal_a_card(deck))    
        elif dealers_hand_score > 21:
                print("DEALER BUSTED YOU WIN")
                break
        else:
            print("DEALER STANDS.")
            break


#deal a random card
def deal_a_card(deck):
   random_card = random.choice(deck)
   deck.remove(random_card)
   return random_card

#Calculate Total Score Of a Given Hand
def hand_score(hand):
    score = 0
    aces = 0
    for card in hand:
     score += card[2]
     if card[0] in ["A"]:
        aces += 1
    while score > 21 and aces > 0:
        score -=10 
        aces -= 1
    return score 
        

        
#initialize our deck
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
            cards = [rank,suit, value]
            deck.append(cards)
    return deck
   



def win_game(player_hand_score, dealer_hand_score):
    if player_hand_score > 21:
      print("Dealer wins")
    elif dealer_hand_score > 21:
        print("Player wins")
    elif player_hand_score > dealer_hand_score:
        print("Player Wins")
    elif dealer_hand_score > player_hand_score:
        print("Dealer wins")
    else:
        print("You have tied")







if __name__ == "__main__":
   main()