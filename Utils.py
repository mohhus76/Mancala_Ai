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


    @staticmethod
    def evaluate(state):
        return sum(state[0:6]) - sum(state[7:13])


    @staticmethod
    def extra_turn(state,selected_hole): #selected hole is zero based/ AI plays in the upper half/human in the lower half
        num_of_stones_to_propagate = state[selected_hole]
        score_hole_index = 6
        if selected_hole>=7:
            score_hole_index = 13
        if (((selected_hole) + num_of_stones_to_propagate) % 14 == score_hole_index):  # last stone condition
            return True

        return False

    @staticmethod
    def is_game_over(state):
        if sum(state[0:5]) == 0:
            state[13] += sum(state[7:12])  # adding remaining holes to score hole
            for i in range(7, 13):
                state[i] = 0  # removing stones from the 6 holes

            return True
        elif sum(state[7:12]) == 0:
            state[6] += sum(state[0:5])
            for i in range(0, 6):
                state[i] = 0
            return True
        return False

    @staticmethod
    def who_wins(state):
        print("Player Score: {}", state[13])
        print("AI Score: {}", state[6])

        if state[13] > state[6]:
            print("Player Won The Game!")

        elif state[13] == state[6]:
            print("DRAW!")

        else:
            print("AI Won The Game!")



