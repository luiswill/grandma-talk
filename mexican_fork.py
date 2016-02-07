
from random import randrange
from input_number_between import input_number_between



        
def play():
    MIN_MONEY_TO_WIN = 200
    FACTOR_WIN = 3
    money = 100
    print "At any time, bet 0 to quit. Quit above %d coins to earn 1/%d money." % (MIN_MONEY_TO_WIN, FACTOR_WIN)
    
    
    while money != 0:
        print "You have %d." % money
        draw1 = randrange(1, 7)
        draw2 = randrange(1, 7)
        
        aux = draw1
        draw1 = min(draw1, draw2)
        draw2 = max(aux, draw2)
        
      
  
        bet = input_number_between("Your bet that the next draw is between %d %d ?" % (draw1, draw2), 0, money)
        if bet == 0: 
            if money >= MIN_MONEY_TO_WIN:
                print "You quit and win %d." % (money / FACTOR_WIN)
                return money / FACTOR_WIN
            else: 
                print "You quit without money!"
                return 0
        
        draw = randrange(1, 7)
        print "I draw %d." % draw
        
        if draw1 <= draw <= draw2:
            money += bet    
        else:
            money -= bet
        

