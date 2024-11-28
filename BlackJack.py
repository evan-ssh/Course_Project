#Procedural Programming Course Project - BlackJack
import random
from db import load_bank, save_bank 



def main():   
    FILENAME = "playermoney.txt"
    player_money = load_bank(FILENAME)  
    if player_money < 5:
     print("\nYour balance is too low. Starting with $100.")
     player_money = 100.0
     save_bank(FILENAME, player_money)



    while True:
        print("\nBLACKJACK!")
        print("\nBlackjack Payout is 3:2")
        print(f"\nPLAYER MONEY: {player_money}")
        
        player_bet = place_bet(player_money)   # get player bet 
       
        
        deck = init_deck() #load cards
        hand = [[], []] # one is player, two is dealer 
     
        for start_deal in range(2): #initial deal of two cards to player and dealer
                    hand[0].append(deal_a_card(deck))
                    hand[1].append(deal_a_card(deck))


        ##########################################
        print("\nDEALERS SHOW CARDs:")
        print(f"{hand[1][0][0]} of {hand[1][0][1]}") # BlackJack logic #
        player_turn(hand,deck) 
        dealers_turn(hand, deck)
        players_hand_score = hand_score(hand[0])
        dealer_hand_score = hand_score(hand[1])
        show_dealer_cards(hand)
        print(f"\nYour points: {players_hand_score}")
        print(f"\nDealers points: {dealer_hand_score}")
        player_money_won = win_game(players_hand_score, dealer_hand_score, player_money, player_bet)
        save_bank(FILENAME, player_money_won)
    ###############################################

        restart_game = input("Play again? (y/n): ") # play again #
        if restart_game.lower() == 'y' or 'yes':
            print(f"Starting next game")
        else:
            print(f"Goodbye! thanks for playing.")
            break
        
    ###############################################
    

def place_bet(player_money):
    while True:
        try:
            player_bet = float(input("BET AMOUNT(5-1000):")) 
            if player_bet == 0: 
               return 0
            if player_bet < 5:
                print("Please enter a higher amount")        
            elif player_bet > 1000:
                print("please enter a lower amount")
            elif player_bet > player_money:
                print("You cant bet more money than you have!")  
            else:
                return player_bet
        except ValueError:
                print("Please enter a number")
def show_dealer_cards(hand):
    print("\nDEALERS CARDS:")
    for card in hand[1]:
     print(f"{card[0]} of {card[1]}\n")

def show_players_cards(hand):
    print("\nYOUR CARDS:")
    for card in hand[0]:
     print(f"{card[0]} of {card[1]}\n")
 




  
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



def deal_a_card(deck): #deal a random card
   card = random.choice(deck)
   deck.remove(card)
   return card


def hand_score(hand): #Calculate Total Score Of a Given Hand
    score = sum(card[2] for card in hand)
    aces = sum(1 for card in hand if card[0] == "A")
    while score > 21 and aces > 0:
        score -=10 
        aces -= 1
    return score 
        

        
 
def init_deck(): #initialize our deck
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
    random.shuffle(deck)
    return deck
   


#determine game winner
def win_game(player_hand_score, dealer_hand_score, player_money, player_bet):
    if player_hand_score == 21: #if player gets blackjack 
     print("BLACKJACK!!")
     player_money += player_bet * 1.5
     return player_money
    elif player_hand_score > 21:
      print("Dealer wins")
      player_money += player_bet 
      return player_money
    elif dealer_hand_score > 21:
        print("Player wins")
        player_money -= player_bet 
        return player_money
    elif player_hand_score > dealer_hand_score:
        print("Player Wins")
        player_money += player_bet 
        return player_money
    elif dealer_hand_score > player_hand_score:
        print("Dealer wins")
        player_money -= player_bet
        return player_money
    else:
        print("You have tied")
    return player_money 






if __name__ == "__main__":
   main()