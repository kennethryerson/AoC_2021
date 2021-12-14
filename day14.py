template = None
pairs = {}
elements = {}

pair_count = {}

with open("day14.in", "r") as f:
    for line in f:
        if template is None:
            template = line.strip()
            for e in template:
                if e not in elements:
                    elements[e] = 0
        elif len(line.strip()):
            pair,e = line.strip().split(" -> ")
            pairs[pair] = e
            pair_count[pair] = 0
            if e not in elements:
                elements[e] = 0

for i in range(len(template)-1):
    pair_count[template[i:i+2]] += 1

def count_step():
    add_counts = {}
    for pair,e in pairs.items():
        np1 = "".join((pair[0],e))
        np2 = "".join((e,pair[1]))
        if pair not in add_counts:
            add_counts[pair] = 0
        if np1 not in add_counts:
            add_counts[np1] = 0
        if np2 not in add_counts:
            add_counts[np2] = 0
        add_counts[np1] += pair_count[pair]
        add_counts[np2] += pair_count[pair]
        add_counts[pair] -= pair_count[pair]
    for pair,c in add_counts.items():
        pair_count[pair] += c

for i in range(40):
    count_step()

for pair,c in pair_count.items():
    elements[pair[0]] += c

elements[template[-1]] += 1

most = 0
least = None
for e,cnt in elements.items():
    if cnt > most:
        most = cnt
    if least is None or cnt < least:
        least = cnt
    print("{}: {}".format(e, cnt))

print(most - least)
