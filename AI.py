from Utils import Utils


class AI:
    @staticmethod
    def alphaBetaSearch(state,level):    
        alpha = -1000;
        beta = 1000;
        maxV = AI.max_value(state,alpha,beta,level);
        
        return maxV; #We need to return the child with this value

    @staticmethod
    def max_value(state,alpha,beta,level):
        v = -10000
        maxChild = state
        
        if(level == 0):
            return Utils.evaluate(state),maxChild
    
        for child in Utils.get_node_children(state,0,False):
            #if(extraTurn(state,child_index)):
                #v = max(v,AI.max_value(child,alpha,beta,level-1)[0])
                
           #else:
            v = max(v,AI.min_value(child,alpha,beta,level-1)[0])
            
            if(v>=beta): #cut off condition
                return v,child
            
            if (v>alpha): #update alpha if the found score is bigger
                alpha = v
                maxChild = child
                
        return v,maxChild;
    @staticmethod
    def min_value(state,alpha,beta,level):
        v = 10000
        minChild = state
        
        if(level == 0):
            return Utils.evaluate(state),minChild
    
        for child in Utils.get_node_children(state,1,False):
            #if(extraTurn(state,child_index)):
                #v = min(v,AI.min_value(child,alpha,beta,level-1)[0])
            #else:
            v = min(v,AI.max_value(child,alpha,beta,level-1)[0])
            
            if(v<alpha): #cut off condition
                return v,child
            
            if (v<beta): #update beta if the found score is smaller
                beta = v
                minChild = child
                
        return v,minChild;













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