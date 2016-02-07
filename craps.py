
from random import randrange
from input_number_between import input_number_between


def play():
    START_MONEY = 100
    MIN_MONEY_TO_WIN = 200
    FACTOR_WIN = 2
    money = START_MONEY
    print "At any time, bet 0 to quit. Quit above %d to win 1/%d of your coins in money" % (MIN_MONEY_TO_WIN, FACTOR_WIN)
    
    while True:
        print "You have %d." % money
        
        bet = input_number_between("  Your bet ?", 0, money)
        
        draw = randrange(1, 7) + randrange(1, 7)

        if draw in [7, 11]:
            money += bet
            print "  %d: Natural... You win!" % draw
            
        elif draw in [2, 3, 12]:
            money -= bet
            print "  %d: Snake eye... You lose!" % draw
        
        elif money == 0: 
            print "You have 0, you lose!"
            return 0
        elif bet == 0:
            if money > FACTOR_WIN * START_MONEY:
                print "You win %d money." % money / FACTOR_WIN
                return money /FACTOR_WIN
            else:
                print "You have under %d coins, sorry." % MIN_MONEY_TO_WIN
                return 0
        else: 
            print "  %d: Try to draw it again... The real fun begins!" % draw
            money += repeat(draw) * bet
        

        

def repeat(objectif):
    print "    Press ENTER to roll the dice..."
    while True:
        if raw_input() == "":
            draw = randrange(1, 7) + randrange(1, 7)
            
            if draw == objectif:
                print "    %d: Your objective... Congrats!" % draw
                return 1
            if draw == 7:
                print "    7: CRAPS... You lose!"
                return -1
            print "    %d: Press ENTER to roll again..." % draw 
            
