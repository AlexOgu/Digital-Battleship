import random


def create_board(board, enemy_board=None, size=10, hidden_ships=True):
    if board is None:
        board = [[' ' for _ in range(size)] for _ in range(size)]

    header = "   " + " ".join([f"{i:2}" for i in range(size)])
    if enemy_board is None:
        print(header)
        for i in range(size):
            print(f"{i:3}" + "|".join([f"{block:2}" for block in board[i]]) + "|")
    else:
        print(header + "      |   " + header)
        for i in range(size):
            enemy_row = [
                'M' if enemy_board[i][j] == 'M' else
                (board[i][j] if enemy_board[i][j] == 'HH' or (not hidden_ships and board[i][j] != ' ') else ' ')
                for j in range(size)
            ]
            print(f"{i:3}" + "|".join([f"{cell:2}" for cell in board[i]]) + "|" +
                  "     |" + f"{i:3}" + "|".join([f"{cell:2}" for cell in enemy_row]) + "|")


def place_ships(board, ship_count, ship_names, ship_names_inv):
    size = len(board)
    for ship_id in range(1, ship_count + 1):
        ship_name, ship_abbreviation, ship_length = ship_names[ship_id]
        ship_placed = False

        while not ship_placed:
            try:
                coords = input(f"Enter x y coordinates to place the {ship_name} (or 'q' to quit): ").strip()
                if coords.lower() == 'q':
                    print("Exiting the game...")
                    exit()

                coords = coords.split()
                ship_row, ship_col = map(int, coords)

                if not (0 <= ship_row < size and 0 <= ship_col < size):
                    print("Coordinates out of bounds.")
                    continue

                direction = input("Enter direction (r for Right, d for Down, or 'q' to quit): ").lower()
                if direction == 'q':
                    print("Exiting the game...")
                    exit()
                if direction not in ['r', 'd']:
                    print("Invalid direction. Please enter 'r' or 'd'.")
                    continue

                if direction == 'r':
                    if ship_col + ship_length > size:
                        print("Ship doesn't fit. Try again.")
                        continue
                    if any(board[ship_row][ship_col + i] != ' ' for i in range(ship_length)):
                        print("Ship overlaps with another ship. Try again.")
                        continue
                    for i in range(ship_length):
                        board[ship_row][ship_col + i] = ship_abbreviation
                elif direction == 'd':
                    if ship_row + ship_length > size:
                        print("Ship doesn't fit. Try again.")
                        continue
                    if any(board[ship_row + i][ship_col] != ' ' for i in range(ship_length)):
                        print("Ship overlaps with another ship. Try again.")
                        continue
                    for i in range(ship_length):
                        board[ship_row + i][ship_col] = ship_abbreviation

                ship_placed = True
            except ValueError:
                print("Invalid input. Please enter numerical coordinates.")

        create_board(board)


def check_guess(board, row, col, ship_names_inv):
    hit_ship = board[row][col]
    if hit_ship in ship_names_inv:
        board[row][col] = 'HH'
        if all(cell != hit_ship for row_cells in board for cell in row_cells):
            print(f"You sunk the {ship_names_inv[hit_ship]}!")
        return hit_ship
    else:
        board[row][col] = 'M'
        print("Missed!")
    return None


def play_battleship(size, num_ships, ship_names):
    ship_names_inv = {abbr: name for _, (name, abbr, _) in ship_names.items()}

    print("Player 1, prepare to place your fleet.")
    board1 = [[' ' for _ in range(size)] for _ in range(size)]
    place_ships(board1, num_ships, ship_names, ship_names_inv)

    print("Player 2, prepare to place your fleet.")
    board2 = [[' ' for _ in range(size)] for _ in range(size)]
    place_ships(board2, num_ships, ship_names, ship_names_inv)

    boards = [board1, board2]
    players = ['Player 1', 'Player 2']
    current_player = 0

    while True:
        print(f"{players[current_player]}'s turn.")
        opponent_board = boards[1 - current_player]
        create_board(boards[current_player], opponent_board, size)

        try:
            guess = input("Enter x y coordinate to fire (or 'q' to quit): ").strip()
            if guess.lower() == 'q':
                print("Exiting the game...")
                exit()

            guess = guess.split()
            guess_row, guess_col = map(int, guess)

            if not (0 <= guess_row < size and 0 <= guess_col < size):
                print("Coordinates out of bounds.")
                continue

            if opponent_board[guess_row][guess_col] in ['HH', 'M']:
                print("Already guessed this coordinate.")
                continue

            hit_ship = check_guess(opponent_board, guess_row, guess_col, ship_names_inv)
            if hit_ship:
                print(f"You hit {players[1 - current_player]}'s {ship_names_inv[hit_ship]}!")
                if all(cell not in ship_names_inv for row in opponent_board for cell in row):
                    print(f"{players[current_player]} wins!")
                    break

            current_player = 1 - current_player
        except ValueError:
            print("Invalid input. Please enter numerical coordinates.")


if __name__ == '__main__':
    ship_names = {
        1: ("Carrier", "Ca", 5),
        2: ("Battleship", "Ba", 4),
        3: ("Cruiser", "Cr", 3),
        4: ("Submarine", "Su", 3),
        5: ("Destroyer", "De", 2)
    }
    play_battleship(10, 5, ship_names)
