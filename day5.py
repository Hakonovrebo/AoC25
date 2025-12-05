"""
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

fresh = set()

f = open("input_5.txt", "r")
l = f.readline()
while l =! "" and l.strip != "":
    start, stop = l.strip().split("-")
    fresh.update(range(start, stop+1)
    l = f.readline()

