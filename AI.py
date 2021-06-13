from Utils import Utils


class AI:
    @staticmethod
    def alphaBetaSearch(state,level,stealing):    
        alpha = -1000;
        beta = 1000;
        maxV = AI.max_value(state,alpha,beta,level,stealing);
        
        return maxV; #We need to return the child with this value

    @staticmethod
    def max_value(state,alpha,beta,level,stealing):
        v = -10000
        maxChild = state
        hole = 0
        if(level == 0 or Utils.is_game_over(state)) :
            return Utils.evaluate(state),maxChild
    
        for child in Utils.get_node_children(state,0,stealing):
            if(Utils.extra_turn(state,child[1])):
                v = max(v,AI.max_value(child[0],alpha,beta,level-1,stealing)[0])
                
            else:
                v = max(v,AI.min_value(child[0],alpha,beta,level-1,stealing)[0])
            
            if(v>=beta): #cut off condition
                return v,child[0],child[1]
            
            if (v>alpha): #update alpha if the found score is bigger
                alpha = v
                maxChild = child[0]
                hole = child[1]
                
        return v,maxChild,hole;
    @staticmethod
    def min_value(state,alpha,beta,level,stealing):
        v = 10000
        minChild = state
        hole = 0
        if(level == 0 or Utils.is_game_over(state)):
            return Utils.evaluate(state),minChild
    
        for child in Utils.get_node_children(state,1,stealing):
            if(Utils.extra_turn(state,child[1])):
                v = min(v,AI.min_value(child[0],alpha,beta,level-1,stealing)[0])
            else:
                v = min(v,AI.max_value(child[0],alpha,beta,level-1,stealing)[0])
            
            if(v<alpha): #cut off condition
                return v,child[0],child[1]
            
            if (v<beta): #update beta if the found score is smaller
                beta = v
                minChild = child[0]
                hole = child[1]
                
        return v,minChild,hole;













###################################################################################################################
def minMaxSearch(state,level):
    maxV = max_value_minMax(state,level);
    return maxV; 


def max_value_minMax(state,level):
    v = -10000
    maxChild = state
    
    if(level == 0):
        return evaluate(state),maxChild

    for child in get_node_children(state):      
        if(v<min_value(child,level-1)[0]):
            v=min_value(child,level-1)[0]
            maxChild=child
            
    return v,maxChild;

def min_value_minMax(state,level):
    v = 10000
    minChild = state
    
    if(level == 0):
        return evaluate(state),minChild

    for child in get_node_children(state):        
       if(v>max_value(child,level-1)[0]):
            v=max_value(child,level-1)[0]
            minChild=child
            
    return v,minChild;