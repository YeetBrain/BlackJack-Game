import random
import time

def aceDecide(cards):
  
  cards1 = cards
    
  while sum(cards1) > 21 and 11 in cards1:
    
    place = cards1.index(11)
    cards1.remove(11)
    cards1.insert(place, 1)
      
  return cards1
      
def getDeck():
  
  used = []
  
  for i in range(2,11):
    for b in range(4):
      used.append(i)
  
  for i in range(4):
    used.append("Jack")
    used.append("Queen")
    used.append("King")
    used.append("Ace")
    
  return used
  
def win(dealer1, player1):
  
  if a > 0:
  
    if sum(player1) > 21:
      print("Here is your hand:")
      print(player)
      print("You busted! :(")
      return False
    
    elif sum(dealer1) > 21:
      print("The dealer busted! :)")
      return False
      
    elif sum(dealer1) < 17:
      return True
    
    else:
      print("The dealer has finalized his hand.")
      
      if sum(dealer1) > sum(player1):
        print("The dealer won. :(")
        return False
        
      elif sum(player1) > sum(dealer1):
        print("You won!:)")
        return False
        
      else:
        print("Tie!")
        return False
        
  else:
      
    return True

############################################################
#print rules and how to play
cardNum = {"Ace": 11, "Jack":10, "Queen":10, "King":10}

start = input("Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! \n\nThe dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!\n\nPress Enter to start playing!")

while start == "":
  
  print("")
#the deck of cards is made
  used = getDeck()
  
#player's deck is made
  player = []
  player1 = []
  card = 0
  
  for i in range(2):

    card = used[random.randint(0,len(used)-1)]
    if isinstance(card, str):
      player1.append(cardNum[card])
    else:
      player1.append(card)
    player.append(card)
    used.remove(card)

    player1 = aceDecide(player1)
#dealer's deck is made
  dealer = []
  dealer1 = []
  
  
  for i in range(2):
  
    card = used[random.randint(0, len(used)-1)]
    if isinstance(card, str):
      dealer1.append(cardNum[card])
    else:
      dealer1.append(card)
    dealer.append(card)
    used.remove(card)

  dealer1 = aceDecide(dealer1)
#Player starts playing

  a = 0

  while win(dealer1, player1):
    
    print("Here is your hand:")
    print(player)
    play = input("Type H to hit or S to stay: ")
  
    if play == "H":
      
      card = used[random.randint(0,len(used)-1)]
      if isinstance(card, str):
        player1.append(cardNum[card])
      else:
        player1.append(card)
      player.append(card)
      used.remove(card)
      player1 = aceDecide(player1)
      
    elif play == "S":
      
      print("")
      print("Dealer's turn!")
      print("")
      print("Here is the dealer's hand")
      print(dealer)
      time.sleep(2)
      
      while sum(dealer1) < 17:
        
        print("The dealer hit. Here is the dealer's new hand: ")
        card = used[random.randint(0,len(used)-1)]
        if isinstance(card, str):
          dealer1.append(cardNum[card])
        else:
          dealer1.append(card)
        dealer.append(card)
        used.remove(card)
        dealer1 = aceDecide(dealer1)
        print(dealer)
        time.sleep(2)
        
    a += 1
     
  print("")   
  start = input("Press Enter to play again!")

      
#Dealer starts playing

#repeat if there isn't a winner
#repeat game if there is a winner and declare winner
