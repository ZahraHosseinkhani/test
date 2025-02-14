# کد بازی تیک تاک تو با پایتون

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # چک کردن ردیف‌ها
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # چک کردن ستون‌ها
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # چک کردن قطرها
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"بازیکن {current_player}، شماره ردیف (0-2) را وارد کنید: "))
        col = int(input(f"بازیکن {current_player}، شماره ستون (0-2) را وارد کنید: "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("حرکت نامعتبر است. لطفاً دوباره تلاش کنید.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"winner0{winner}")
            break

        if is_full(board):
            print_board(board)
            print("dron")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()