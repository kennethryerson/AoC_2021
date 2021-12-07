in_data = []

with open("day7.in", "r") as f:
    for line in f:
        in_data.extend([int(x) for x in line.split(",")])

c_at_h = [0]*(max(in_data)+1)
for h in in_data:
    c_at_h[h] += 1

print(c_at_h)

def fuel_cost(h):
    cost = 0
    for i in range(len(c_at_h)):
        cost += abs(i - h)*c_at_h[i]
    return cost

def find_h(cfunc):
    h = 0
    cost = cfunc(0)
    for i in range(1, len(c_at_h)):
        c = cfunc(i)
        if c < cost:
            h = i
            cost = c
    return h

h = find_h(fuel_cost)
print(h)
print(fuel_cost(h))

ccosts = [0]*len(c_at_h)
for i in range(1,len(ccosts)):
    ccosts[i] = ccosts[i-1]+i

def fuel_cost2(h):
    cost = 0
    for i in range(len(c_at_h)):
        cost += ccosts[abs(i - h)]*c_at_h[i]
    return cost

h = find_h(fuel_cost2)
print(h)
print(fuel_cost2(h))
