def alphaBetaSearch(state,level):
    
    alpha = -1000;
    beta = 1000;
    maxV = max_value(state,alpha,beta,level);
    return maxV; #We need to return the child with this value


def max_value(state,alpha,beta,level):
    v = -10000
    maxChild = state
    
    if(level == 0):
        return evaluate(state),maxChild

    for child in get_node_children(state):
        v = max(v,min_value(child,alpha,beta,level-1)[0])
        
        if(v>=beta): #cut off condition
            return v,child;
        
        if (v>alpha): #update alpha if the found score is bigger
            alpha = v
            maxChild = child
            
    return v,maxChild;

def min_value(state,alpha,beta,level):
    v = 10000
    minChild = state
    
    if(level == 0):
        return evaluate(state),minChild

    for child in get_node_children(state):
        v = min(v,max_value(child,alpha,beta,level-1)[0])
        
        if(v<alpha): #cut off condition
            return v,child;
        
        if (v<beta): #update beta if the found score is smaller
            beta = v
            minChild = child
            
    return v,minChild;
