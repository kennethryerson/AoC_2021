in_data = []

with open("day11.in", "r") as f:
    for line in f:
        in_data.append([int(x) for x in line.strip()])

flashed = []
for i in range(10):
    flashed.append([False]*10)

nflashes = 0

def clear():
    for i in range(10):
        for j in range(10):
            if in_data[i][j] > 9:
                in_data[i][j] = 0
            flashed[i][j] = False

def flash(i,j):
    global nflashes
    if in_data[i][j] > 9 and not flashed[i][j]:
        nflashes += 1
        flashed[i][j] = True
        for ii in range(i-1,i+2):
            for jj in range(j-1,j+2):
                if ii >= 0 and ii < 10 and jj >= 0 and jj < 10 and not (ii == i and jj == j):
                    in_data[ii][jj] += 1
                    flash(ii,jj)

def step():
    for i in range(10):
        for j in range(10):
            in_data[i][j] += 1
    for i in range(10):
        for j in range(10):
            flash(i,j)

def all():
    for i in range(10):
        for j in range(10):
            if not flashed[i][j]:
                return False
    return True

for i in range(1000):
    step()
    if all():
        print("sync: {}".format(i+1))
    clear()

print(nflashes)
