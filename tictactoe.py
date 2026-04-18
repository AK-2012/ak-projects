from os import system
from random import choice

# tic tac toe board
board = [" "] * 10
result = None
count = 0


def main():
    global result, board, count
    while True:
        try:
            print("This is tic tac toe (also known as naughts and crosses). ")
            mode = (
                v_input(
                    "Would you like to play against the computer or another player? (C) (P) ",
                    ["c", "p", "computer", "player"],
                )
            )
            difficulty = False
            if mode in ["c", "computer"]:
                difficulty = v_input("Would you like to play easy or hard/impossible difficulty? (E) (H) ",
                                     ["easy", "e", "hard", "h"]
                                     )
                difficulty = False if difficulty in ["easy", "e"] else True
            print("\nYou will be X. The computer will automatically fill in spaces. ")
            while result is None:
                count += 1
                take_turn("X")
                system("clear")
                if result is not None:
                    break
                count += 1
                take_turn("O", mode, difficulty)
                system("clear")
            system("clear")
            if result is not None:
                print(result)
            draw_board()
            again = v_input("\nWould you like to play again? (Y) (N) ", ["y", "n", "yes", "no"])
            if again in ["y", "yes"]:
                board = [" "] * 10
                result = None
                count = 0
                system("clear")
                continue
            else:
                break
        except (EOFError, KeyboardInterrupt):
            break
    print("Thank you for playing and goodbye!")


def show_index():
    print(
        "\nEnter an index for a spot on the board:\n\n1|2|3\n-----\n4|5|6\n------\n7|8|9"
    )


def v_input(string, entries):
    valid_entry = input(string).strip().lower()
    while valid_entry not in entries:
        valid_entry = input(string).strip().lower()
    return valid_entry


def win():
    global result
    # all possible winning positions as tuples
    wins = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]
    # loop through the winning combos and check if any have all x's or o's (going through each tuple combination and checking if they all have the same value)
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            result = f"{board[a]} wins\n\n"
            return
    if " " not in board[1:]:
        result = "It's a draw!"


def take_turn(player, type="player", difficulty=False):
    global board
    show_index()
    # heading
    print(f"\n------{player} Goes------\n\n")
    # drawing current state of board
    draw_board()
    # loop to do stuff and for errors
    while True:
        if type == "player" or type == "p":
            try:
                spot = int(input(""))
                # if the spot is taken
                if spot < 1 or spot > 9 or board[spot] != " ":
                    raise ValueError
                board[spot] = player
                break
            # if the user has entered a value greater than 9 or an invalid value or an already taken spot
            except (ValueError, IndexError):
                print("Enter a valid index")
                continue

        # playing against the computer, which is o
        elif type == "c" or type == "computer":
            if difficulty == True: # impossible difficulty
                spot = None
                winning_combos = [
                (1, 2, 3),
                (4, 5, 6),
                (7, 8, 9),
                (1, 4, 7),
                (2, 5, 8),
                (3, 6, 9),
                (1, 5, 9),
                (3, 5, 7),
                         ]
                for x, y, z in winning_combos:
                    # priority 1 - comp win
                    line = [board[x], board[y], board[z]]
                    if line.count("O") == 2 and line.count(" ") == 1:
                        i = line.index(" ")
                        match i:
                            case 0:
                                spot = x
                            case 1:
                                spot = y
                            case 2:
                                spot = z
                        break

                if not spot:
                    for x, y, z in winning_combos:
                        # priority 2 - blocking player
                        line = [board[x], board[y], board[z]]
                        if line.count("X") == 2 and line.count(" ") == 1:
                            i = line.index(" ")
                            match i:
                                case 0:
                                    spot = x
                                case 1:
                                    spot = y
                                case 2:
                                    spot = z
                            break

                # priority 3 - middle
                if not spot and board[5] == " ":
                    spot = 5

                # priority 4 - edges
                if not spot:
                    edges = [number for number in [2, 4, 6, 8] if board[number] == " "]
                    if edges:
                        spot = choice(edges)

                # priority 5 - corners
                if not spot:
                    corners = [number for number in [1, 3, 7, 9] if board[number] == " "]
                    if corners:
                        spot = choice(corners)

            elif difficulty == False:
                possible = [index for index, value in enumerate(board) if value == " " and index != 0]
                if possible:
                    spot = choice(possible)

            if spot:
                board[spot] = "O"
                break

    print("\n")
    system("clear")
    win()


def draw_board():
    print(
        f"Current state of board:\n\n{board[1]}|{board[2]}|{board[3]}\n-----\n{board[4]}|{board[5]}|{board[6]}\n------\n{board[7]}|{board[8]}|{board[9]}"
    )


if __name__ == "__main__":
    main()
