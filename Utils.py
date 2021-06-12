@staticmethod
def get_node_children(in_state: list,playerType = 0,stealing=False):#0 for AI , 1 for player
    children = []
    if(playerType == 0):
        for i in range(7,13):
            state = in_state[:]  # by value
            if state[i] == 0:
                children.append(state)
            else:
                num_of_stones_to_propagate = state[i]
                state[i] = 0
                for j in range(1, num_of_stones_to_propagate + 1):
                    if j == num_of_stones_to_propagate and stealing == True:  # last stone condition
                        if state[(i + j) % 14] == 0 and ((i + j) % 14) != 6:  # stealing  # i+j != 6 (human_score_hole)
                            num_of_stolen_stones = state[13 - ((i + j) % 14) - 1]
                            state[13 - ((i + j) % 14) - 1] = 0
                            state[6] += num_of_stolen_stones + 1  # 1 is the last stone itself
                    else:
                        state[(i + j) % 14] += 1
                children.append(state)
        else:
            for i in range(6):
                state = in_state[:]  # by value
                if state[i] == 0:
                    children.append(state)
                else:
                    num_of_stones_to_propagate = state[i]
                    state[i] = 0
                    for j in range(1, num_of_stones_to_propagate + 1):
                        if j == num_of_stones_to_propagate and stealing == True:  # last stone condition
                            if state[(i + j) % 14] == 0 and ((i + j) % 14) != 6:  # stealing  # i+j != 6 (human_score_hole)
                                num_of_stolen_stones = state[13 - ((i + j) % 14) - 1]
                                state[13 - ((i + j) % 14) - 1] = 0
                                state[6] += num_of_stolen_stones + 1  # 1 is the last stone itself
                        else:
                            state[(i + j) % 14] += 1
                    children.append(state)
    return children





