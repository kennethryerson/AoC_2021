in_data = []

with open("day1.in", "r") as f:
    for line in f:
        in_data.append(int(line.strip()))

increased_counts = 0

for d1,d2 in zip(in_data[0:-1], in_data[1:]):
    if d2 > d1:
        increased_counts += 1

print("increased {} times".format(increased_counts))

windowed = []
for d in zip(in_data[0:-2], in_data[1:-1], in_data[2:]):
    windowed.append(sum(d))

increased_counts = 0

for w1,w2 in zip(windowed[0:-1], windowed[1:]):
    if w2 > w1:
        increased_counts += 1

print("windowed data increased {} times".format(increased_counts))
