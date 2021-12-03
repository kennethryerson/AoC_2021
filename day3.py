in_data = []

with open("day3.in", "r") as f:
    for line in f:
        in_data.append(line.strip())

n = len(in_data)
width = len(in_data[0])

gamma = 0
epsilon = 0

for bit in range(width):
    bit_count = 0
    for x in in_data:
        if x[bit] == "1":
            bit_count += 1
    gamma <<= 1
    epsilon <<= 1
    if bit_count > n//2:
        gamma |= 1
    else:
        epsilon += 1

power = gamma*epsilon

print("gamma: {}".format(gamma))
print("epsilon: {}".format(epsilon))
print("power consumption: {}".format(power))

in_data.sort()
o2_data = in_data.copy()
co2_data = in_data.copy()

for bit in range(width):
    bit_count = 0
    for x in o2_data:
        if x[bit] == "1":
            bit_count += 1
    idx = 0
    while idx < n and o2_data[idx][bit] != "1":
        idx += 1
    if bit_count >= (len(o2_data) + 1)//2:
        o2_data = o2_data[idx:]
    else:
        o2_data = o2_data[0:idx]
    if len(o2_data) == 1:
        break

o2_consumption = int(o2_data[0], base=2)
print("O2 consumption: {}".format(o2_consumption))

for bit in range(width):
    bit_count = 0
    for x in co2_data:
        if x[bit] == "1":
            bit_count += 1
    idx = 0
    while idx < n and co2_data[idx][bit] != "1":
        idx += 1
    if bit_count >= (len(co2_data) + 1)//2:
        co2_data = co2_data[0:idx]
    else:
        co2_data = co2_data[idx:]
    if len(co2_data) == 1:
        break

co2_rating = int(co2_data[0], base=2)
print("CO2 rating: {}".format(co2_rating))

life = o2_consumption*co2_rating
print("life support: {}".format(life))
