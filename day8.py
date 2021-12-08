first_in = []
second_in = []

with open("day8.in", "r") as f:
    for line in f:
        a,b = line.strip().split("|")
        a = a.strip()
        b = b.strip()
        first_in.append(a.split(" "))
        second_in.append(b.split(" "))

count = 0
for line in second_in:
    for seg in line:
        if len(seg) in [2,4,3,7]:
            count += 1

print(count)

def match_letters(a,b):
    count = 0
    for c in a:
        if c in b:
            count += 1
    return count

def decode_line(line):
    letters_by_digit = ["","","","","","","","","",""]
    for seg in line:
        if len(seg) == 2:
            letters_by_digit[1] = "".join(sorted(seg))
        elif len(seg) == 3:
            letters_by_digit[7] = "".join(sorted(seg))
        elif len(seg) == 4:
            letters_by_digit[4] = "".join(sorted(seg))
        elif len(seg) == 7:
            letters_by_digit[8] = "".join(sorted(seg))

    for seg in line:
        if len(seg) == 6:
            if match_letters(seg, letters_by_digit[4]) == 4:
                n = 9
            elif match_letters(seg, letters_by_digit[7]) == 3:
                n = 0
            else:
                n = 6
            letters_by_digit[n] = "".join(sorted(seg))
        elif len(seg) == 5:
            if match_letters(seg, letters_by_digit[1]) == 2:
                n = 3
            else:
                if match_letters(seg, letters_by_digit[4]) == 3:
                    n = 5
                else:
                    n = 2
            letters_by_digit[n] = "".join(sorted(seg))
    return letters_by_digit

def decode_digits(segs, digits):
    out = 0
    for seg in segs:
        for i in range(10):
            if "".join(sorted(seg)) == digits[i]:
                out = out*10 + i
    return out

total = 0
for first,second in zip(first_in, second_in):
    digits = decode_line(first)
    x = decode_digits(second, digits)
    print(x)
    total += x

print(total)
