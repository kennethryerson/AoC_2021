in_data = []

with open("day2.in", "r") as f:
    for line in f:
        in_data.append(line.strip().split(" "))

pos = 0
depth = 0

for d,u in in_data:
    if d == "forward":
        pos += int(u)
    elif d == "down":
        depth += int(u)
    elif d == "up":
        depth -= int(u)

print("pos: {}, depth: {}".format(pos, depth))
print(pos*depth)

pos = 0
depth = 0
aim = 0

for d,u in in_data:
    if d == "forward":
        pos += int(u)
        depth += aim*int(u)
    elif d == "down":
        aim += int(u)
    elif d == "up":
        aim -= int(u)

print("pos: {}, depth: {}".format(pos, depth))
print(pos*depth)
