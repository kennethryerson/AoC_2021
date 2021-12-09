in_data = []

with open("day9.in", "r") as f:
    for line in f:
        in_data.append(line.strip())

row_len = len(in_data[0])

def low_point(x,y):
    p = int(in_data[y][x])
    if y > 0 and int(in_data[y-1][x]) <= p:
        return False
    if x > 0 and int(in_data[y][x-1]) <= p:
        return False
    if x < (row_len - 1) and int(in_data[y][x+1]) <= p:
        return False
    if y < (len(in_data) - 1) and int(in_data[y+1][x]) <= p:
        return False
    return True

low_points = []

risk = 0
for y in range(len(in_data)):
    for x in range(row_len):
        if low_point(x,y):
            risk += int(in_data[y][x]) + 1
            low_points.append((x,y))

print(risk)

def get_basin(points):
    new_points = points.copy()
    point_added = False
    for x,y in points:
        for xx,yy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if xx >= 0 and xx < row_len and yy >= 0 and yy < len(in_data):
                if (xx,yy) not in new_points and int(in_data[yy][xx]) != 9:
                    new_points.append((xx,yy))
                    point_added = True
    if point_added:
        return get_basin(new_points)
    return new_points

basin_sizes = []
for p in low_points:
    basin_sizes.append(len(get_basin([p])))

#print(basin_sizes)
top_3 = sorted(basin_sizes)[-3:]
print(top_3)
print(top_3[0]*top_3[1]*top_3[2])