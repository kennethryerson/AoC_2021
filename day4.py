in_data = []

with open("day4.in", "r") as f:
    for line in f:
        in_data.append(line)

call_numbers = [int(x) for x in in_data[0].split(",")]

boards = []

li = 2
while li < len(in_data):
    board = []
    for row in range(5):
        row = [0]*5
        for col in range(5):
            row[col] = int(in_data[li][col*3:col*3+2])
        board.append(row)
        li += 1
    boards.append(board)
    li += 1

row_win = ["X"]*5

def print_board(b):
    print()
    for row in range(5):
        print(b[row])
    print()

def board_sum(b):
    bsum = 0
    for row in range(5):
        for col in range(5):
            if b[row][col] != "X":
                bsum += b[row][col]
    return bsum

winners = []
winner = None
last_called = []
board_sums = []
for n in call_numbers:
    for board in boards:
        for row in range(5):
            for col in range(5):
                if board[row][col] == n:
                    board[row][col] = "X"
    for i in range(len(boards)):
        if i not in winners:
            for row in range(5):
                if boards[i][row] == row_win:
                    winner = i
                    winners.append(winner)
                    last_called.append(n)
                    board_sums.append(board_sum(boards[winner]))
                    break
            for col in range(5):
                count = 0
                for row in range(5):
                    if boards[i][row][col] == "X":
                        count += 1
                if count == 5:
                    winner = i
                    winners.append(winner)
                    last_called.append(n)
                    board_sums.append(board_sum(boards[winner]))
                    break
    if len(winners) == len(boards):
        break

print("winner = {}, call = {}".format(winners[0], last_called[0]))
print("loser = {}, call = {}".format(winners[-1], last_called[-1]))

print(board_sums[0]*last_called[0])
print(board_sums[-1]*last_called[-1])
