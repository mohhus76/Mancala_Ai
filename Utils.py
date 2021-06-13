class Utils:

    @staticmethod
    def print_frame(vertical, horizontal, character):
        print(character * horizontal)
        for i in range(1, vertical - 1):
            print(character, ' ' * (horizontal - 2), character, sep='')
        print(character * horizontal)

    @staticmethod
    def print_board(state):
        space = " "
        print(space * 12, end=space * 2)
        for i in reversed(range(7, 13)):
            print("[" + str(state[i]) + "]", space * 4, end=space * 2)
        print("\n")
        print(space * 4, end=space * 2)
        print("[" + str(state[13]) + "]", end=space * 2)
        print(space * 59, end=space * 2)
        print("[" + str(state[6]) + "]", end=space * 2)

        print("\n")
        print(space * 12, end=space * 2)
        for i in range(6):
            print("[" + str(state[i]) + "]", space * 4, end=space * 2)

        print("\n\n")

    @staticmethod
    def let_human_play():
        human_play = input("Choose a hole:  ")
        print("\n\n")
        return int(human_play)

    @staticmethod
    def convert_play_to_state(previous_state, hole_index,stealing):
        new_state = previous_state[:]
        num_of_stones_to_propagate = new_state[hole_index]
        new_state[hole_index] = 0
        for i in range(1,num_of_stones_to_propagate+1):
            if (i == num_of_stones_to_propagate and stealing == True):
                if new_state[(hole_index+i)%14] == 0 and ((hole_index+i)%14) != 6 and ((hole_index+i)%14) != 13:  # stealing  # i+j != 6 (human_score_hole)
                    num_of_stolen_stones = new_state[13 -(((hole_index+i)%14)  +1)]
                    new_state[13 -(( (hole_index+i)%14)  +1)] = 0
                    new_state[6] += num_of_stolen_stones + 1  # 1 is the last stone itself
                else:
                    new_state[((hole_index+i)%14)] += 1
            else:
                new_state[((hole_index+i)%14)] += 1

        return new_state

    @staticmethod
    def get_node_children(in_state: list,playerType = 0,stealing=False):#0 for AI , 1 for player
        children = []
        if(playerType == 0):
            for i in range(7,13):
                state = in_state[:]  # by value
                if state[i] == 0:
                    pass
                else:
                    num_of_stones_to_propagate = state[i]
                    state[i] = 0
                    for j in range(1, num_of_stones_to_propagate + 1):
                        if j == num_of_stones_to_propagate and stealing == True:  # last stone condition
                            if state[(i + j) % 14] == 0 and ((i + j) % 14) != 13 and ((i + j) % 14) != 6 :  # stealing  # i+j != 6 (human_score_hole)
                                num_of_stolen_stones = state[13 -( ((i + j) % 14) +1)]
                                state[13 -( ((i + j) % 14) +1)] = 0
                                state[13] += num_of_stolen_stones + 1  # 1 is the last stone itself
                            else:
                                state[(i + j) % 14] += 1
                        else:
                            state[(i + j) % 14] += 1
                    children.append((state,i))
                    
        else:
            for i in range(6):
                state = in_state[:]  # by value
                if state[i] == 0:
                    pass
                else:
                    num_of_stones_to_propagate = state[i]
                    state[i] = 0
                    for j in range(1, num_of_stones_to_propagate + 1):
                        if j == num_of_stones_to_propagate and stealing == True:  # last stone condition
                            if state[(i + j) % 14] == 0 and ((i + j) % 14) != 6 and ((i + j) % 14) != 13 :  # stealing  # i+j != 6 (human_score_hole)
                                num_of_stolen_stones = state[13 -( ((i + j) % 14) +1)]
                                state[13 -( ((i + j) % 14) +1)] = 0
                                state[6] += num_of_stolen_stones + 1  # 1 is the last stone itself
                            else:
                                state[(i + j) % 14] += 1
                        else:
                            state[(i + j) % 14] += 1
                    children.append((state,i))
        return children
# =============================================================================
#     def get_node_children(in_state: list, stealing=False):
#         children = []
#         for i in range(6):
#             state = in_state[:]  # by value
#             if state[i] == 0:
#                 children.append(state)  #  Edited
#             else:
#                 num_of_stones_to_propagate = state[i]
#                 state[i] = 0
#                 for j in range(1, num_of_stones_to_propagate + 1):  # range 1 >> 6
#                     if ((i + num_of_stones_to_propagate) % 14) == 6 and stealing == True:  # last stone condition
#                         if state[(i + j) % 14] == 0 and ((i + j) % 14) != 6:  # stealing  # i+j != 6 (human_score_hole)
#                             num_of_stolen_stones = state[13 - ((i + j) % 14) - 1]
#                             state[13 - ((i + j) % 14) - 1] = 0
#                             state[6] += num_of_stolen_stones + 1  # 1 is the last stone itself
#                     else:
#                         state[(i + j) % 14] += 1
#                 children.append(state)
#         return children
# =============================================================================


    @staticmethod
    def evaluate(state):
        return sum(state[0:6]) - sum(state[7:13])

    @staticmethod
    def possibleMoves(state):
        print("possible moves : \n")
        possiblemoves = []
        for i in range(6):
            if state[i] != 0:
                possiblemoves.append(i+1)
                print("Hole number "+str(i+1)+" \n")
        return possiblemoves

    @staticmethod
    def extra_turn(state,selected_hole): #selected hole is zero based/ AI plays in the upper half/human in the lower half
        num_of_stones_to_propagate = state[selected_hole]
        score_hole_index = 6
        if selected_hole>=7:
            score_hole_index = 13
        if ((selected_hole + num_of_stones_to_propagate) % 14 == score_hole_index):  # last stone condition
            return True

        return False

    @staticmethod
    def is_game_over(state):
        if sum(state[0:6]) == 0:
            state[13] += sum(state[7:13])  # adding remaining holes to score hole
            for i in range(7, 13):
                state[i] = 0  # removing stones from the 6 holes

            return True
        elif sum(state[7:13]) == 0:
            state[6] += sum(state[0:6])
            for i in range(0, 6):
                state[i] = 0
            return True
        return False

    @staticmethod
    def who_wins(state):
        print("Player Score: "+ str(state[6]))
        print("AI Score: "+str(state[13]))

        if state[6] > state[13]:
            print("Player Won The Game!")

        elif state[13] == state[6]:
            print("DRAW!")

        else:
            print("AI Won The Game!")
  