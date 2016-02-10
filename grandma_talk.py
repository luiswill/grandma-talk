#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from random import randrange, choice


GAMES = ["mexican_fork", "craps", "rocket_drive"]
FAMILY = [("Steve", 50), ("Bill", 55), ("Bob", 14)]
MONEY = 0


def talk():
    text_exclam = ["Boy I hear you", 
                    "I hear you don't shout", 
                    "I AM NOT AS OLD AS YOU THINK!", 
                    "I AM JUST IN FRONT OF YOU MAN!", "BOY I UNDERSTAND YOU!",
                    "STOP SHOUTING SO LOUD!!" 
        ]
    
    while True:
        say = raw_input("> ")
        
        if say.startswith("BYE"):
            bye(say)
            print "BYE BYE SONNY!"
            return 
        if except_words(say): #"procédure" to find special words in sentence
            break
            
        elif say.endswith("?"):
            print "What's your problem ? Do you need some MONEY son?"
            
        elif say.endswith("!"):
            if say.count("!") <= len(text_exclam):
                print text_exclam[say.count("!") - 1] #-1 because we have minimum 1 "!" so start at 0
            else: 
                print "CALM DOWN BOY!"
        elif say.upper() != say:
            print "HUH ?! SPEAK UP, SONNY !"
        else:
            print grandma_answer(say)
     
    
def bye(say):
    print "Help me to find one word for scrabble and I let you go."
    words = ["informatique", "", "tortue", "coccinelle", "cristaline"]
    
    if choice((True, True)): #change to (True, False) after correcting shuffling 
        word = choice(words)
        while True:
            if raw_input("My word : %s." % word[::-1]).lower() == word:
                return
            
    else: 
        word = choice(words)
        from random import shuffle
        while True: #doesn't work, I don't know why
            word = word
            shuffle(list(word))
            word_ = ''.join(word)
            if raw_input("My word : %s." % word_) == word:
                return
            

def except_words(say):
    words = [("GRANDMA", "God I am not your mom"), ("GAMES", "I am young enough to play : %s" % GAMES), 
             ("MONEY", "Your money : %d " % MONEY), ("HELP", 
             "Type MONEY to see your money, GAMES to see which games you can play."),
             ("MARIJUANA", "I have some in my garden")
            ]
    if "PLAY" in say: 
        print ask_game_and_play(GAMES)
    elif "FAMILY" in say:
        family()
    else: 
        for word in say.split(" "):
            for i in range(len(words)):
                if words[i][0] == word:
                    print words[i][1]

    

def grandma_answer(say):
    text = [
        [
            "NO, NOT SINCE %d HOURS",
            "Mh yes I slept around %d hours today",
            "Exactly, I lost %d teeths", 
            "I will come to you in %d days",
            "Probably %d times"
        ],
        "You are ugly!",
        "Boy, do you really think I don't hear you?",
        "What the fuck?", "Do you love me?", "What ? You vomite?",
        "Do you want some schweppes with me?", 
        "You're the big boss!", "Aristide is the best.", 
        "L1 Info 4ever", "You mean today?", "Now?", "Oh I ate chicken today", 
        "Boy, you're completely right!", "Python or PHP?"
    ]
    
    RANGE_RANDOM = 20
    MIN_LENGTH_FOR_DEFORM = 10
    if choice((True, False)): #if choice is True
        return "Did you say : %s?" % say.replace(choice(say.replace(" ", "")), unichr(randrange(65, 91)))
         
    rand_text = randrange(len(text))
    to_say = ""
    if rand_text < len(text[0]):
        rand_number = randrange(RANGE_RANDOM)
        to_say = text[0][rand_text] % rand_number
    else:
        to_say = text[rand_text]
        
    if len(say) > MIN_LENGTH_FOR_DEFORM:
        return to_say[::1]
    else: 
        return to_say
        
                
def family():
    
    
    
    choice = raw_input("Our family?")
    if choice.lower() == "all":
        for i in range(len(FAMILY)):
            print "%s is %d years old." % (FAMILY[i][0], FAMILY[i][1])
    if choice.lower().startswith("add"):
        from input_number_between import input_number_between
        FAMILY.append((raw_input("Do you have a name for your person?"), 
                    input_number_between("Since how many years is this person on earth ?", 0, 150)))
        print "Oh a new family member! "

def ask_game_and_play(GAMES):
    
    while True:
        game = raw_input("What do you want to play little boy? We have %s." % GAMES)
        
        if game in GAMES:
            import importlib
            return importlib.import_module(game, package=None).play()
        
        else:
            return "Sorry boy, I am too old to remember this game."

talk()
