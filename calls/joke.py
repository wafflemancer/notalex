# Get random joke from custom dialogue
# Note: due to legacy implementation,
# number of jokes is hardcoded to
# be randomized.                
# NUM_JOKES = 6
        
#from random import randint
import custom_dialogue as cd

def rand_joke():
    NUM_JOKES = 6
    bank = cd.dialogue_bank()
    msg = msg.strip()
    #num = randint(1,NUM_JOKES)
    num = '4'
    #jokeselect = str(num) + 'joke'
    jokeselect = num + 'joke'
    if jokeselect in bank.keys():
        convo = bank[jokeselect]
            if convo[1] is None:
                return convo[0]
            else:
                if convo[1](jokeselect):
                    return convo[0]
                else:
                    return None
    else:
        return None
