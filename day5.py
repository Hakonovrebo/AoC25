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
def union_fresh(fresh_block):
    # 1) Sorter på startverdien
    fresh_block = sorted(fresh_block, key=lambda x: x[0])

    merged = []

    for start, stop in fresh_block:
        if not merged:
            merged.append([start, stop])
        else:
            last_start, last_stop = merged[-1]

            # Hvis det nye intervallet overlapper eller "toucher" det forrige
            # juster dette etter om intervallene er inklusiv/eksklusiv
            if start <= last_stop + 1:
                # Slå sammen: ta maks sluttverdi
                merged[-1][1] = max(last_stop, stop)
            else:
                # Ingen overlap: nytt intervall
                merged.append([start, stop])

    # 2) Regn ut total lengde
    sum_fres = 0
    for lo, hi in merged:
        # Hvis du bruker inclusive grenser (lo <= val <= hi),
        # er lengden hi - lo + 1
        sum_fres += hi - lo + 1

    print(sum_fres)
    return merged



fresh_ranges = []

with open("input_5.txt") as f:
    data = f.read().split("\n\n")

first_block = data[0].splitlines()
second_block = data[1].splitlines()
for l in first_block:
    start, stop = map(int, l.strip().split("-"))
    fresh_ranges.append((start, stop)) 

"""
fresh = 0

for v in second_block:
    val = int(v)
    #print(v)

    for lo, hi in fresh_ranges:
        if lo <= val <= hi:
            fresh += 1
            print(lo, hi, val)
            break
print(fresh)
"""

union_fresh(fresh_ranges)
