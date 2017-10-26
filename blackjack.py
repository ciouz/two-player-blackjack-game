### BLACKJACK TABLE BY SHAWN MISAR
#Neat things about this program:
#---Bets can be wagered
#---Drinks can be had
#---The game is two player with a computer dealer
#---All 52 cards and suits are present
#---Aces count as 11 unless the hand is over 21, then it becomes 1 until bust.
#---Each player can draw up to 4 cards (2 initially upon start of game).
#---No hangovers the next day
#---This is my very first python program, took me 24 hours. I'm proud of it. Enjoy!
import random

player1balance = 20
player2balance = 20
anothergame = "Y"
while anothergame == "Y" and (player1balance and player2balance > 0):

    deck =       {1: {"card": "Ace",
                      "suit": "Hearts",
                      "value": 11},
                  2: {"card": "Two",
                      "suit": "Hearts",
                      "value": 2},
                  3: {"card": "Three",
                      "suit": "Hearts",
                      "value": 3},
                  4: {"card": "Four",
                      "suit": "Hearts",
                      "value": 4},
                  5:  {"card": "Five",
                       "suit": "Hearts",
                       "value": 5},
                  6: {"card": "Six",
                      "suit": "Hearts",
                      "value": 6},
                  7: {"card": "Seven",
                      "suit": "Hearts",
                      "value": 7},
                  8: {"card": "Eight",
                      "suit": "Hearts",
                      "value": 8},
                  9: {"card": "Nine",
                      "suit": "Hearts",
                      "value": 9},
                  10: {"card": "Ten",
                       "suit": "Hearts",
                       "value": 10},
                  11: {"card": "Jack",
                       "suit": "Hearts",
                       "value": 10},
                  12: {"card": "Queen",
                       "suit": "Hearts",
                       "value": 10},
                  13: {"card": "King",
                       "suit": "Hearts",
                       "value": 10},
                  14: {"card": "Ace",
                       "suit": "Diamonds",
                       "value": 11},
                  15: {"card": "Two",
                       "suit": "Diamonds",
                       "value": 2},
                  16: {"card": "Three",
                       "suit": "Diamonds",
                       "value": 3},
                  17: {"card": "Four",
                       "suit": "Diamonds",
                       "value": 4},
                  18:  {"card": "Five",
                        "suit": "Diamonds",
                        "value": 5},
                  19: {"card": "Six",
                       "suit": "Diamonds",
                       "value": 6},
                  20: {"card": "Seven",
                       "suit": "Diamonds",
                       "value": 7},
                  21: {"card": "Eight",
                       "suit": "Diamonds",
                       "value": 8},
                  22: {"card": "Nine",
                       "suit": "Diamonds",
                       "value": 9},
                  23: {"card": "Ten",
                       "suit": "Diamonds",
                       "value": 10},
                  24: {"card": "Jack",
                       "suit": "Diamonds",
                       "value": 10},
                  25: {"card": "Queen",
                       "suit": "Diamonds",
                       "value": 10},
                  26: {"card": "King",
                       "suit": "Diamonds",
                       "value": 10},
                  27: {"card": "Ace",
                       "suit": "Spades",
                       "value": 11},
                  28: {"card": "Two",
                       "suit": "Spades",
                       "value": 2},
                  29: {"card": "Three",
                       "suit": "Spades",
                       "value": 3},
                  30: {"card": "Four",
                       "suit": "Spades",
                       "value": 4},
                  31:  {"card": "Five",
                        "suit": "Spades",
                        "value": 5},
                  32: {"card": "Six",
                       "suit": "Spades",
                       "value": 6},
                  33: {"card": "Seven",
                       "suit": "Spades",
                       "value": 7},
                  34: {"card": "Eight",
                       "suit": "Spades",
                       "value": 8},
                  35: {"card": "Nine",
                       "suit": "Spades",
                       "value": 9},
                  36: {"card": "Ten",
                       "suit": "Spades",
                       "value": 10},
                  37: {"card": "Jack",
                       "suit": "Spades",
                       "value": 10},
                  38: {"card": "Queen",
                       "suit": "Spades",
                       "value": 10},
                  39: {"card": "King",
                       "suit": "Spades",
                       "value": 10},
                  40: {"card": "Ace",
                       "suit": "Clubs",
                       "value": 11},
                  41: {"card": "Two",
                       "suit": "Clubs",
                       "value": 2},
                  42: {"card": "Three",
                       "suit": "Clubs",
                       "value": 3},
                  43: {"card": "Four",
                       "suit": "Clubs",
                       "value": 4},
                  44:  {"card": "Five",
                        "suit": "Clubs",
                        "value": 5},
                  45: {"card": "Six",
                       "suit": "Clubs",
                       "value": 6},
                  46: {"card": "Seven",
                       "suit": "Clubs",
                       "value": 7},
                  47: {"card": "Eight",
                       "suit": "Clubs",
                       "value": 8},
                  48: {"card": "Nine",
                       "suit": "Clubs",
                       "value": 9},
                  49: {"card": "Ten",
                       "suit": "Clubs",
                       "value": 10},
                  50: {"card": "Jack",
                       "suit": "Clubs",
                       "value": 10},
                  51: {"card": "Queen",
                       "suit": "Clubs",
                       "value": 10},
                  52: {"card": "King",
                       "suit": "Clubs",
                       "value": 10}}


    card1key = ''
    card2key = ''
    card3key = ''
    card4key = ''
    card5key = ''
    card6key = ''
    card7key = ''
    card8key = ''
    card9key = ''
    card10key = ''
    card11key = ''
    card12key = ''
    totalround2 = ''
    totalround3 = ''
    totalround4 = ''
    totalround5 = ''
    totalround6 = ''
    totalround7 = ''
    totalround8 = ''
    totalround9 = ''
    totalround10 = ''
    totalround11 = ''

    player1 = input("What is your name, superstar? ")
    print("Welcome {}! Now find a friend and bring him or her to join the table!".format(player1))
    player2 = input("Hello! Welcome to the blackjack table. What is your name? ")
    print("Welcome {}! Let's play!".format(player2))
    print("-"*40)
    print("WELCOME TO THE BLACKJACK TABLE")
    print("-"*40)
    drink = input("Would you like a drink? (Y/N) ")
    if drink == "Y":
        print(
              "``````````````````````````````````\n"
              " ```                 `  `      ```\n"
              "   ```              `  `    ```\n" 
              "     ```                  ```\n"
              "        ```              ```\n"
              "          ```          ```\n"
              "             ||||||||||\n"
              "             ||||||||||\n"
              "             ||||||||||\n"
              "             ||||||||||\n"
              "             ||||||||||\n"
              "             ||||||||||\n"
              "             ||||||||||\n"
              "             ||||||||||\n"
              "           000000000000000\n"
                        
              "There you are! Enjoy your beautiful martini!\n"
              "The bartenders are efficient around here.")
    print("-"*40)
    rules = input("Do you know how to play? (Y/N) ")
    if rules == "N":
        print("Okay! The rules are simple. You'll receive two cards in your hand, as will {}, and the dealer. \n"
              "Your goal is to beat the dealer by getting closer to 21. If you and the dealer have the same number \n"
              "Cards 2 - 10 counts as it's own number; jacks, queens, and kings counts as 10 each, and aces can count\n"
              " as either 1 or 11. Each user can draw up to four cards at this table. House wins on a tie or push.".format(player2))
        print("-"*40)
        print("Let's begin blackjack!")
        print("-"*40)
    else:
        print("Let's begin blackjack!")
        print("-"*40)
    firstseat = input("Who's up first? {} or {}? ".format(player1, player2))
    if firstseat == player1:
        secondseat = player2
    else:
        secondseat = player1

    #PLAYER1 TURN
    wager = int(input("Would you like to bet 5 or 10 dollars? Your balance is {} dollars. (5/10) ".format(player1balance)))
    print("Good luck, {}. You place {} dollars on the table. You have a {} dollar remaining balance.\n"
          "Here are your two cards: ".format(firstseat, wager, player1balance - wager))
    card1key = random.choice(deck)
    for k,v in deck.items():
        if card1key == k:
            del deck[k]
    card2key = random.choice(deck)
    for k,v in deck.items():
        if card2key == k:
            del deck[k]
    totalround2 = (card1key["value"]) + (card2key["value"])
    # DOUBLE ACE CHECK
    if totalround2 == 22:
        totalround2 = 12

    print("{} of {} and a {} of {}. \n"
          "You're at: {}".format(card1key["card"], card1key["suit"], card2key["card"], card2key["suit"], totalround2))
    print("-"*40)
    hitorstay = input("Hit or Stay? (H/S)")
    if hitorstay == "H":
        card3key = random.choice(deck)
        for k,v in deck.items():
            if card3key == k:
                del deck[k]
        totalround3 = (card1key["value"]) + (card2key["value"]) + (card3key["value"])
        #Over 21 because of a 11 Ace? Let's make that ace into a 1 and update the total.
        if int(totalround3) > 21 and card1key["card"] == "Ace":
            int(totalround3) - 10
        if int(totalround3) > 21 and card2key["card"] == "Ace":
            int(totalround3) - 10
        if int(totalround3) > 21 and card3key["card"] == "Ace":
            int(totalround3) - 10

        print("{} of {}, {} of {}, and {} of {}.\n"
              "Total: {}".format(card1key["card"], card1key["suit"], card2key["card"], card2key["suit"], card3key["card"], card3key["suit"], totalround3))
        if totalround3 > 21:
            print("BUST! Please wait for the next game.")
        if totalround3 < 21:
            hitorstay = input("Hit or Stay? (H/S)")
            if hitorstay == "H":
                card4key = random.choice(deck)
                for k,v in deck.items():
                    if card4key == k:
                        del deck[k]
                totalround4 = (card1key["value"]) + (card2key["value"]) + (card3key["value"]) + (card4key["value"])
                #Over 21 because of a 11 Ace? Let's make that ace into a 1 and update the total.
                if int(totalround4) > 21 and card1key["card"] == "Ace":
                    int(totalround4) - 10
                if int(totalround4) > 21 and card2key["card"] == "Ace":
                    int(totalround4) - 10
                if int(totalround4) > 21 and card3key["card"] == "Ace":
                    int(totalround4) - 10
                if int(totalround4) > 21 and card4key["card"] == "Ace":
                    int(totalround4) - 10
                print("{} of {}, {} of {}, {} of {} and {} of {}.\n"
                  "Total: {}".format(card1key["card"], card1key["suit"], card2key["card"], card2key["suit"], card3key["card"], card3key["suit"], card4key["card"], card4key["suit"], totalround4))
                if totalround4 > 21:
                    print("BUST! Please wait for the next game.")
            else:
                print("-"*40)
                print("It is now {}'s turn.\n"
                      "Good luck {}! Here we go...".format(secondseat, secondseat))
                print("-"*40)
        else:
            print("It is now {}'s turn.\n"
              "Good luck {}! Here we go...".format(secondseat, secondseat))
            print("-"*40)
    else:
        print("It is now {}'s turn.\n"
              "Good luck {}! Here we go...".format(secondseat, secondseat))
        print("-"*40)



    #PLAYER2 TURN
    wager2 = int(input("Would you like to bet 5 or 10 dollars, {}? Your balance is {} dollars. (5/10) ".format(secondseat, player2balance)))
    print("Good luck, {}. You place {} dollars on the table. You have a {} dollar remaining balance.\n"
          "Here are your two cards: ".format(secondseat, wager2, player2balance - wager2))
    card5key = random.choice(deck)
    for k,v in deck.items():
        if card5key == k:
            del deck[k]
    card6key = random.choice(deck)
    for k,v in deck.items():
        if card6key == k:
            del deck[k]


    totalround5 = (card5key["value"]) + (card6key["value"])
    #Double Ace Check
    if totalround5 == 22:
        totalround5 = 12

    print("{} of {} and a {} of {}. \n"
          "You're at: {}".format(card5key["card"], card5key["suit"], card6key["card"], card6key["suit"], totalround5))
    print("-"*40)
    hitorstay = input("Hit or Stay? (H/S)")

    if hitorstay == "H":
        card7key = random.choice(deck)
        for k,v in deck.items():
            if card7key == k:
                del deck[k]
        totalround6 = (card5key["value"]) + (card6key["value"]) + (card7key["value"])
        #Over 21 because of a 11 Ace? Let's make that ace into a 1 and update the total.
        if int(totalround6) > 21 and card5key["card"] == "Ace":
            int(totalround6) - 10
        if int(totalround6) > 21 and card6key["card"] == "Ace":
            int(totalround6) - 10
        if int(totalround6) > 21 and card7key["card"] == "Ace":
            int(totalround6) - 10
        print("{} of {}, {} of {}, and {} of {}.\n"
              "Total: {}".format(card5key["card"], card5key["suit"], card6key["card"], card6key["suit"], card7key["card"], card7key["suit"], totalround6))
        if totalround6 > 21:
            print("BUST! Please wait for the next game.")
        if totalround6 < 21:
            hitorstay = input("Hit or Stay? (H/S)")

            if hitorstay == "H":
                card8key = random.choice(deck)
                for k,v in deck.items():
                    if card8key == k:
                        del deck[k]
                totalround7 = (card5key["value"]) + (card6key["value"]) + (card7key["value"]) + (card8key["value"])
            #Over 21 because of a 11 Ace? Let's make that ace into a 1 and update the total.
                if int(totalround7) > 21 and card5key["card"] == "Ace":
                    int(totalround7) - 10
                if int(totalround7) > 21 and card6key["card"] == "Ace":
                    int(totalround7) - 10
                if int(totalround7) > 21 and card7key["card"] == "Ace":
                    int(totalround7) - 10
                if int(totalround7) > 21 and card8key["card"] == "Ace":
                    int(totalround7) - 10
            print("{} of {}, {} of {}, {} of {} and {} of {}.\n"
                  "Total: {}".format(card5key["card"], card5key["suit"], card6key["card"], card6key["suit"], card7key["card"], card7key["suit"], card8key["card"], card8key["suit"], int(totalround7)))
            if totalround7 > 21:
                print("BUST! Please wait for the next game.")
            else:
                print("-"*40)
                print("It is now the dealer's turn. Good luck everyone! Here we go...")
                print("-"*40)
        else:
            print("It is now the dealer's turn. Good luck everyone! Here we go...")
            print("-"*40)
    else:
        print("It is now the dealer's turn. Good luck everyone! Here we go...")
        print("-"*40)




    #DEALER DRAWS TWO CARDS
    card9key = random.choice(deck)
    for k,v in deck.items():
        if card9key == k:
            del deck[k]
    card10key = random.choice(deck)
    for k,v in deck.items():
        if card10key == k:
            del deck[k]
    totalround8 = (card9key["value"]) + (card10key["value"])
    #DOUBLE ACE CHECK
    if totalround8 == 22:
        totalround8 = 12
    print("{} of {} and a {} of {}.\n"
          "Total: {}".format(card9key["card"], card9key["suit"], card10key["card"], card10key["suit"], totalround8))

    if totalround8 < 16: #and another card if less than 16
        card11key = random.choice(deck)
        for k,v in deck.items():
            if card11key == k:
                del deck[k]
        totalround9 = (card9key["value"]) + (card10key["value"]) + (card11key["value"])
        #Over 21 because of a 11 Ace? Let's make that ace into a 1 and update the total.
        if int(totalround9) > 21:
            if card9key["card"] == "Ace":
                int(totalround9) - 10
            if card10key["card"] == "Ace":
                int(totalround9) - 10
            if card11key["card"] == "Ace":
                int(totalround9) - 10
        print("{} of {}, {} of {}, and {} of {}.\n"
        "Total: {}".format(card9key["card"], card9key["suit"], card10key["card"], card10key["suit"], card11key["card"], card11key["suit"], totalround9))

        if totalround9 < 16: #and another card if less than 16
            card12key = random.choice(deck)
            for k,v in deck.items():
                if card12key == k:
                    del deck[k]
            totalround10 = (card9key["value"]) + (card10key["value"]) + (card11key["value"] + (card12key["value"]))
            #Over 21 because of a 11 Ace? Let's make that ace into a 1 and update the total.
            if int(totalround10) > 21:
                if card9key["card"] == "Ace":
                    int(totalround10) - 10
                if card10key["card"] == "Ace":
                    int(totalround10) - 10
                if card11key["card"] == "Ace":
                    int(totalround10) - 10
                if card12key["card"] == "Ace":
                    int(totalround10) - 10
            print("{} of {}, {} of {}, {} of {}, and {} of {}.\n"
              "Total: {}".format(card9key["card"], card9key["suit"], card10key["card"], card10key["suit"], card11key["card"], card11key["suit"], card12key["card"], card12key["suit"], totalround10))

            if totalround10 > 21: #BUST
                 print("Dealer BUST!")
            if totalround10 < 21:
                print("The dealer stays at {}.".format(totalround10))

        if totalround9 > 21: #BUST
            print("Dealer BUST!")

        else:
            print("The dealer stays at {}.".format(totalround9))
            print("-"*40)

    else:
        print("The dealer stays at {}.".format(totalround8))
        print("-"*40)




    #RESULTS OF ROUND
    print("-"*40)
    print("----------RESULTS----------")


    #player1 results
    if int(totalround2 or totalround3 or totalround4) > 21:#BUST
        print("The dealer wins against {}! BUST! Sorry, you lost your bet.".format(firstseat))
        player1balance -= wager
    if int(totalround8 or totalround9 or totalround10) >= int(totalround4 or totalround3 or totalround2): #Player1 loses against dealer
        print("The dealer wins against {}! Sorry, you lost your bet.".format(firstseat))
        player1balance -= wager
    else: #Player1 wins against the dealer
        print("{} won against the dealer, and won {} dollars!".format(firstseat, wager * 2 ))
        player1balance += wager*2


    #player2 results
    if int(totalround5 or totalround6 or totalround7) > 21:#BUST
        print("The dealer wins against {}! BUST! Sorry, you lost your bet.".format(secondseat))
        player2balance -= wager2
    if int(totalround8 or totalround9 or totalround10) >= int(totalround7 or totalround6 or totalround5): #Player2 loses against dealer
        print("The dealer wins against {}! Sorry, you lost your bet.".format(secondseat))
        player2balance -= wager2
    else: #Player2 wins against the dealer
        print("{} won against the dealer, and won {} dollars!".format(secondseat, wager2 * 2 ))
        player2balance += wager2*2

    print("-"*40)
    anothergame = input("Want to try another round? {}'s remaining balance is {} and {}'s remaning balance is {}. (Y/N) ".format(firstseat, player1balance, secondseat, player2balance))
    if anothergame == "N":
        print("Thanks for playing! Come back for free martinis anytime!")


