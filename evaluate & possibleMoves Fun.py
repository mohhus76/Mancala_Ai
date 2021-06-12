def evaluate(state):
    return sum(state[0:6])-sum(state[7:13])
    
    
    
def possibleMoves(state):
    possiblemoves=[]
    for i in range(7,13):
        if(state[i] != 0):
            possiblemoves.append(i-6)
    return possiblemoves


def extra_turn(state, selected_hole, player_type):
        num_of_stones_to_propagate = state[selected_hole - 1]
        score_hole_index = 6
        if player_type == "human":
            score_hole_index = 13

        if (((selected_hole - 1) + num_of_stones_to_propagate) % 14) == score_hole_index:  # last stone condition
            return True

        return False
