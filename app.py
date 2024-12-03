import random 

snakes = {17: 7, 54: 34, 62: 19, 64: 60, 87: 36, 93: 73, 95: 75, 98: 79}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99}
final_position = 100

def roll_dice():
    return random.randint(1, 6)

def get_position(player_position, roll):
    new_position = player_position + roll
    if new_position > final_position:
        return player_position  
    return new_position


def snake_or_ladder(position):
    if position in snakes:
        print(f"Oops! Bitten by a snake at {position}. Slide down to {snakes[position]}!")
        return snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder at {position}. Go up to {ladders[position]}!")
        return ladders[position]
    return position 

def playGame():
    print("Welcome to Snakes and Ladders Game!")
    print("Version: 1.0.0  *Feel Free to use anything*\n")
    print("Rules:")
    print("1. Initially all the players are at starting position i.e. 0.")
    print("2. If you land at the bottom of a ladder, you can move up to the top of the ladder.")
    print("3. If you land on the head of a snake, you must slide down to the bottom of the snake.")
    print("4. The first player to get to the FINAL position is the winner.\n")
    print("Game starts now!\n")
    
    player1 = input("Enter your name: ")
    players = [player1, "Player 2"]
    positions = {player: 0 for player in players}

    winner = None
    round_num = 1

    while not winner:
        print(f"--- Round {round_num} ---")
        
        print(f"{player1}'s turn:")
        input("Press Enter to roll the dice...")  # Wait for the player to press Enter
        roll = roll_dice()
        print(f"{player1} rolled a {roll}!")
        new_position = get_position(positions[player1], roll)
        print(f"{player1} moves from {positions[player1]} to {new_position}.")
        new_position = snake_or_ladder(new_position)
        positions[player1] = new_position
        print(f"{player1} is now at position {positions[player1]}.\n")
        
        if positions[player1] == final_position:
            winner = player1
            break

        print("Player 2's turn:")
        roll = roll_dice()
        print(f"Player 2 rolled a {roll}!")
        new_position = get_position(positions["Player 2"], roll)
        print(f"Player 2 moves from {positions['Player 2']} to {new_position}.")
        new_position = snake_or_ladder(new_position)
        positions["Player 2"] = new_position
        print(f"Player 2 is now at position {positions['Player 2']}.\n")

        if positions["Player 2"] == final_position:
            winner = "Player 2"
            break
        
        round_num += 1

    print(f"Congratulations {winner}! You have won the game by reaching position {final_position}!")
    print("Game Over.")



playGame()
