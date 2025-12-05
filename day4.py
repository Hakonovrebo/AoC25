#parse input
#lese inn 2d array
#finne størrelse på array for å sette begrensinger
#ittterere gjennom og sjekke alle naboer. 
def has_nabors(x, y):
    """
    -1,-1 0,-1 +1,-1
    -1,0   x   +1,0
    +1,-1 +1,0 +1,+1 
    """
    naburs = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len_x and 0 <= ny < len_y:
                if paperstorage[ny][nx]:
                    naburs += 1

    return True if naburs < 4 else False 

paperstorage = []

f = open("input_4.txt", "r")

for line in f:
    line = line.strip()
    arr = []
    for symbol in line:
        arr.append(True if symbol.strip() == "@" else False)
    paperstorage.append(arr)

len_x = len(paperstorage[0])
len_y = len(paperstorage)

moveble_stacks = 0 
for y in range(0, len_x):
    for x in range(0, len_y):
        print(len_x, len_y, x, y)
        if paperstorage[y][x]:
            moveble_stacks += 1 if has_nabors(x, y) else 0 

print(moveble_stacks)