in_data = []

with open("day5.in", "r") as f:
    for line in f:
        in_data.append(line.strip())

lines = []

for x in in_data:
    s,e = x.split(" -> ")
    s = [int(x) for x in s.split(",")]
    e = [int(x) for x in e.split(",")]
    lines.append((s,e))

xmax = 0
ymax = 0

for line in lines:
    if line[0][0] > xmax:
        xmax = line[0][0]
    if line[1][0] > xmax:
        xmax = line[1][0]
    if line[0][1] > ymax:
        ymax = line[0][1]
    if line[1][1] > ymax:
        ymax = line[1][1]

gline = ["." for i in range(xmax+1)]
grid = []
for i in range(ymax+1):
    grid.append(gline.copy())

for line in lines:
    if line[0][0] == line[1][0]:
        p0 = line[0][1]
        p1 = line[1][1]
        if p0 > p1:
            p0 = line[1][1]
            p1 = line[0][1]
        for y in range(p0,p1+1):
            if grid[y][line[0][0]] == ".":
                grid[y][line[0][0]] = 1
            else:
                grid[y][line[0][0]] += 1
    elif line[0][1] == line[1][1]:
        p0 = line[0][0]
        p1 = line[1][0]
        if p0 > p1:
            p0 = line[1][0]
            p1 = line[0][0]
        for x in range(p0,p1+1):
            if grid[line[0][1]][x] == ".":
                grid[line[0][1]][x] = 1
            else:
                grid[line[0][1]][x] += 1
    else: # diagonals
        x0 = line[0][0]
        x1 = line[1][0]
        y0 = line[0][1]
        y1 = line[1][1]
        x = x0
        y = y0
        while x != x1 and y != y1:
            if grid[y][x] == ".":
                grid[y][x] = 1
            else:
                grid[y][x] += 1
            if x0 < x1:
                x += 1
            else:
                x -= 1
            if y0 < y1:
                y += 1
            else:
                y -= 1
        if grid[y][x] == ".":
            grid[y][x] = 1
        else:
            grid[y][x] += 1

count = 0
for line in grid:
    for e in line:
        if e != "." and e > 1:
            count += 1

print(count)
