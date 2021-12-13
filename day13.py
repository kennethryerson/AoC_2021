paper = []
instructions = []

with open("day13.in", "r") as f:
    inst_break = False
    for line in f:
        if not inst_break:
            if line.strip():
                paper.append([int(x) for x in line.strip().split(",")])
            else:
                inst_break = True
        else:
            instructions.append(line.split(" ")[-1].split("="))

def fold_left(crease):
    folded = []
    for dot in paper:
        if dot[0] < crease:
            dot[0] = crease - dot[0] - 1
        else:
            dot[0] = dot[0] - crease - 1
        if dot not in folded:
            folded.append(dot)
    return folded

def fold_up(crease):
    folded = []
    for dot in paper:
        if dot[1] > crease:
            dot[1] = 2*crease - dot[1]
        if dot not in folded:
            folded.append(dot)
    return folded

if instructions[0][0] == "x":
    print(len(fold_left(int(instructions[0][1]))))
elif instructions[0][0] == "y":
    print(len(fold_up(int(instructions[0][1]))))

for inst in instructions:
    if inst[0] == "x":
        paper = fold_left(int(inst[1]))
    elif inst[0] == "y":
        paper = fold_up(int(inst[1]))

def print_paper():
    width = 0
    height = 0
    for p in paper:
        if p[0] >= width:
            width = p[0] + 1
        if p[1] >= height:
            height = p[1] + 1
    grid = []
    for i in range(height):
        grid.append([" " for j in range(width)])
    for p in paper:
        grid[p[1]][p[0]] = "#"
    for row in range(height):
        for col in range(width-1,-1,-1):
            print(grid[row][col],end="")
        print()

print_paper()
