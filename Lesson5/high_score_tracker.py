
while True:
	game_score = input("Enter a game score or `stop` to END: ")
	
	if game_score.strip().lower() == 'stop':
		print("Game session ended!")
		break
	else:
		try:
			if not game_score.isdigit():
				raise ValueError
			game_score = int(game_score)
			if game_score > 100:
				print("Wow! That’s a new high score!")
			else:
				print("Good try, keep playing!")
		except ValueError:
			print("Enter a number or `stop` to END")
