from AI import AI
from Utils import Utils

play = "y"

while play == "y":
	initial_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
	state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
	number_levels=4
	hole_number = 0
	level = input("Select level (E/M/H) \n")
	if(level == 'M'):
		number_levels=8
	elif(level == 'H'):
		number_levels=12        
	mode = input("stealing mode ?  (y / n) \n")
	turn = input("play first turn? (y/n)\n")
	if(mode == 'y'):
		stealing = True
	else:
		stealing = False
	while(True):
		new_turn_human = 1
		new_turn_ai = 1
		
		if(turn == 'y'):
			
			while(new_turn_human or Utils.extra_turn(initial_state , hole_number-1)):
				print("Human turn : \n")
				initial_state = state[:]
				Utils.print_board(state)
				Utils.possibleMoves(state)
				hole_number = Utils.let_human_play() #return hole number one based
				state = Utils.convert_play_to_state(state, hole_number-1,stealing)
				Utils.print_board(state)
				if(Utils.is_game_over(state)):
					break
				new_turn_human = 0
				print("----------------------------------------------------------------------\n")
			
			if(Utils.is_game_over(state)):
				break
			
			while(new_turn_ai or Utils.extra_turn(initial_state , hole_number)):
				print("Computer turn : \n")
				initial_state = state[:]
				v,state,hole_number = AI.alphaBetaSearch(state,number_levels,stealing)
				print("Computer played hole "+str((hole_number+1)-7))
				Utils.print_board(state)            
				if(Utils.is_game_over(state)):
					break
				new_turn_ai = 0
				print("----------------------------------------------------------------------\n")
				
			if(Utils.is_game_over(state)):
				break
				
		else:
			while(new_turn_ai or Utils.extra_turn(initial_state , hole_number)):
				print("Computer turn : \n")
				initial_state = state[:]
				v,state,hole_number = AI.alphaBetaSearch(state,number_levels,stealing)
				print("Computer played hole "+str((hole_number+1)-7))
				Utils.print_board(state)            
				if(Utils.is_game_over(state)):
					break
				new_turn_ai = 0
				print("----------------------------------------------------------------------\n")
				
			if(Utils.is_game_over(state)):
				break
			
			while(new_turn_human or Utils.extra_turn(initial_state , hole_number-1)):
				print("Human turn : \n")
				initial_state = state[:]
				Utils.possibleMoves(state)
				hole_number = Utils.let_human_play() #return hole number one based
				state = Utils.convert_play_to_state(state, hole_number-1,stealing)
				Utils.print_board(state)
				if(Utils.is_game_over(state)):
					break
				new_turn_human = 0
				print("----------------------------------------------------------------------\n")
			
			if(Utils.is_game_over(state)):
				break
		
	Utils.who_wins(state)
	play = input("Play again y/n: ")