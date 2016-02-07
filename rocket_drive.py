
def input_direction(message):
    while True:
        direction = input(message)
        if direction in (-1, 0, 1):
            return direction
        print "Please enter -1, 1 or 0."

def play():
    
    MONEY_TO_WIN = 200
    position = -143
    speed = 0
    trials = 0
    print "position | speed | direction"
    while True:
        message = "%8d | %5d | " % (position, speed)
        if position == 0:
            print message, "you won in %d trials!" % trials
            if trials <= 20:
                print "Congratulations, you win %d." % MONEY_TO_WIN * 5
                return MONEY_TO_WIN * 5
            elif 20 < trials < 50:
                print "Great, you win %d." % MONEY_TO_WIN 
                return MONEY_TO_WIN 
        direction = input_direction(message)
        if direction == 0:
            print "Aborted. You win nothing."
            return 0
        if speed * direction > 0:
            speed = 2 * speed
        elif speed * direction < 0:
            speed = int(speed / 2.0) # simulate a truncated division, since / is a floored devision (-1/2 actually yields -1)
        else:
            speed = direction
        trials += 1
        position += speed
