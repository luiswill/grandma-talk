from random import randrange

def talk():
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
    money = 0
    
    games = ["mexican_fork", "craps", "rocket_drive"]
    help_me = ["games", "text", "money"]
    
    
    RANGE_RANDOM = 20
    
    while True:
        say = raw_input("> ")
        if say.startswith("BYE"):
            print "BYE, SONNY !"
            return
    
        if "play" in say:
            ask_game_and_play(list_games)
            print "You have %d money." % money
            
        elif say == "help":
            print "Type money to see your money, games to see games, text to see my answers possible.."
            
        elif say.endswith("!!"):
            print "Calm down boy!"
        elif say.upper() != say:
            print "HUH ?! SPEAK UP, SONNY !"
        else:
            rand_text = randrange(len(text))
            if rand_text < len(text[0]):
                rand_number = randrange(RANGE_RANDOM)
                print text[0][rand_text] % rand_number
            else:
                print text[rand_text]
                
                

def ask_game_and_play(games):
    
    while True:
        game = raw_input("What do you want to play little boy? Type list to show games.")
        
        if game == "list":
            print games
            
        elif game in games:
            import importlib
            return importlib.import_module(game, package=None).play()
        
        else:
            print "Sorry boy, I am too old to remember this game."
            return
talk()
