#parse input
#lese inn 2d array
#finne størrelse på array for å sette begrensinger
#ittterere gjennom og sjekke alle naboer. 
paperstorage = []

for line in input:
    arr = []
    for symbol in line:
        arr.append(True if symol.strip() == "@" else False)
    paperstorage.append(arr)

len_x = len(paperstorage[0])
len_y = len(paperstorage)

def has_nabors(x, y):
    """
    -1,-1 0,-1 +1,-1
    -1,0   x   +1,0
    +1,-1 +1,0 +1,+1 
    """
    naburs = 0 
    for nx in range(-1, 2):
        for ny in range(-1,2):
            if nx == 0 and ny == 0:
                continue # skipper og sjekke seg selv. 
            nx = x + nx 
            ny = y + ny 
            if 0 <= nx < len_x and 0 <= ny < len_y #sjekker vi ikke prøver og slå opp indexer utenfor array grenser. 
                if paperstorage[nx][ny]:
                    naburs += 1 

    return True if naburs < 4 else False 
moveble_stacks = 0 
for x in range(0, len_x):
    for y in range(0, len_y):
        if paperstorage[x][y]:
            moveble_stacks += 1 if has_nabors(x, y) else 0 
