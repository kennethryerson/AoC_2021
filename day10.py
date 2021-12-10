in_data = []

with open("day10.in", "r") as f:
    for line in f:
        in_data.append(line.strip())

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

match = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

def check(line):
    stack = []
    for i in range(len(line)):
        if line[i] in ["(", "[", "{", "<"]:
            stack.append(match[line[i]])
        elif line[i] in [")", "]", "}", ">"]:
            if stack.pop() != line[i]:
                return i,line[i]
    return None,None

corrupt_lines = []
total_points = 0
for line in in_data:
    error,delim = check(line)
    if error:
        total_points += points[delim]
    else:
        corrupt_lines.append(line)

print(total_points)


points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def fix_line(line):
    stack = []
    for i in range(len(line)):
        if line[i] in ["(", "[", "{", "<"]:
            stack.append(match[line[i]])
        elif line[i] in [")", "]", "}", ">"]:
            stack.pop()
    score = 0
    while len(stack):
        c = stack.pop()
        score *= 5
        score += points[c]
    return score

scores = []
for line in corrupt_lines:
    scores.append(fix_line(line))

print(sorted(scores)[len(scores)//2])
