import datetime
import re

def log_score(score, times_played, largest_number):
    with open("log.txt", "a") as log_file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{current_time}: Game: {times_played}, Score: {score}, Largest Tile: {largest_number}\n")


def read_scores():


    # Initialize variables
    total_games_played = 0
    high_score = 0
    games_2048_and_higher = 0

    # Open the log file
    with open('log.txt', 'r') as log_file:
        for line in log_file:
            # Increment total games played
            total_games_played += 1
            
            # Extract score and largest tile using regular expressions
            match = re.search(r"Score: (\d+), Largest Tile: (\d+)", line)
            if match:
                score = int(match.group(1))
                largest_tile = int(match.group(2))
                
                # Update high score
                if score > high_score:
                    high_score = score
                
                # Check if the largest tile is 2048 or higher
                if largest_tile >= 2048:
                    games_2048_and_higher += 1

    # Print or return the results
    print(f"Total Games Played: {total_games_played}")
    print(f"High Score: {high_score}")
    print(f"Games with 2048 or higher tile: {games_2048_and_higher}")

    scores = []
    return scores, high_score, total_games_played, games_2048_and_higher

