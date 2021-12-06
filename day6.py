fish_on_day = [0,0,0,0,0,0,0,0,0,0]

def next_day():
    global fish_on_day
    next = [0,0,0,0,0,0,0,0,0]
    for i in range(8):
        next[i] = fish_on_day[i+1]
    next[6] += fish_on_day[0]
    next[8] = fish_on_day[0]
    fish_on_day = next.copy()

with open("day6.in", "r") as f:
    for line in f:
        for x in line.split(","):
            fish_on_day[int(x)] += 1

print(fish_on_day)

for i in range(256):
    next_day()

print(sum(fish_on_day))
