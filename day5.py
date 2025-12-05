input_5 = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

fresh_ranges = []

with open("input.txt") as f:
    data = f.read().split("\n\n")

first_block = data[0].splitlines()
second_block = data[1].splitlines()

for l in first_block:
    start, stop = map(int, l.strip().split("-"))
    fresh_ranges.append((start, stop)) 
fresh_counter = []

fresh = 0

for v in second_block:
    val = int(v)
    for lo, hi in fresh_counter:
        if lo <= val <= hi:
            fresh += 1
            break

print(fresh)
        
