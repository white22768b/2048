import stats
import mov
import game


def main_menu():
    while True:
        game.clear_screen()
        print("1. Enter the game")
        print("2. Check stats")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            main()
        elif choice == '2':
            scores, high_score, total_games_played, games_2048_or_higher = stats.read_scores()
            print("Stats:")
            print()
            print(f"High Score: {high_score}")
            # print("Last 5 games:")
            # for timestamp, score in scores[-5:]:  # Adjusted to show last 5 games
                # print(f"{timestamp}: Score: {score}")
            print(f"Number of times 2048 or higher was achieved: {games_2048_or_higher}")
            print(f"Total Games Played: {total_games_played}")
            input("Press Enter to return to the main menu...")
        elif choice == '3':
            break


def main():
    reached_2048 = False
    # Load times_played from log.txt
    try:
        with open('log.txt', 'r') as file:
            times_played = sum(1 for line in file)
    except FileNotFoundError:
        times_played = 0

    while True:
        grid = game.initialize_grid()
        score = 0
        moves = 0  # Initialize move counter
        largest_number = 0 # Initialize largest number
        game.print_grid(grid)
        while True:
            print(f"Score: {score} | Moves: {moves}")  # Display move counter
            move = mov.get_move()
            if move == 'K':  # Check if the player pressed 'K' to end the game
                print("Game Over!")
                print(f"Final Score: {score}")
                times_played += 1  # Increment times played
                stats.log_score(score, times_played, largest_number)  # Assume modification to log_score to include largest_number
                break  # End the current game
            if move in ['W', 'A', 'S', 'D']:
                moves += 1  # Increment move counter
                # Update grid based on the move (Assuming this happens inside a function not shown here)
                # After updating the grid, find the largest number
                current_largest = max(map(max, grid))  # Find the largest number in the grid
                if current_largest > largest_number:  # Update the largest number if a new one is found
                    largest_number = current_largest
            if move == 'W':
                grid, gained_score = mov.move_up(grid)
            elif move == 'A':
                grid, gained_score = mov.move_left(grid)
            elif move == 'S':
                grid, gained_score = mov.move_down(grid)
            elif move == 'D':
                grid, gained_score = mov.move_right(grid)
            else:
                print("Invalid move. Please enter W, A, S, or D. Press K to end game.")
                continue
            score += gained_score
            game.add_new_tile(grid)  # Add a new tile to the grid after a successful move
            game.clear_screen()
            game.print_grid(grid)
            if not reached_2048 and game.contains_2048_tile(grid):
                user_choice = input("You've reached 2048! Do you want to continue? (Y/N): ")
                if user_choice.lower() != 'y':
                    print("Game Over!")
                    print(f"Final Score: {score}")
                    times_played += 1  # Increment times played
                    stats.log_score(score, times_played, largest_number)  # Assume modification to log_score to include largest_number
                    break  # End the current game
                reached_2048 = True  # Set the flag to True to avoid asking again
            if not mov.can_move(grid):
                print("No more moves available. Game over!")
                print(f"Final Score: {score}")
                times_played += 1  # Increment times played
                stats.log_score(score, times_played, largest_number)  # Assume modification to log_score to include largest_number
                break  # End the current game

        # Ask the user if they want to play again
        play_again = input("Play again? (Y/N): ")
        if play_again.lower() != 'y':
            break  # Exit the while loop and end the game
        else:
            # Reset game variables for a new game
            grid = game.initialize_grid()
            grid = game.print_grid(grid)
            score = 0
            reached_2048 = False
            # No need to increment times_played here as it's done at game over


if __name__ == "__main__":
    main_menu()