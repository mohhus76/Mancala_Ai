def evaluate(state):
    return sum(state[0:6])-sum(state[7:13])
    
    
    
def possibleMoves(state):
    possiblemoves=[]
    for i in range(7,13):
        if(state[i] != 0):
            possiblemoves.append(i-6)
    return possiblemoves
