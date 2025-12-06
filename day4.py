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
input_lines = open("input_4.txt", "r")
for line in input_lines:
    line = line.strip()
    if not line:
        continue
    row = [ch for ch in line]   # beholder '.' og '@' som er
    paperstorage.append(row)

len_y = len(paperstorage)        # antall rader
len_x = len(paperstorage[0])     # antall kolonner


def has_nabors(warehouse, y, x):
    """
    Sjekker om cellen (y, x) har færre enn 4 naboer som er '@'.
    y = rad, x = kolonne

    Naboer:
    (-1,-1) (0,-1) (+1,-1)
    (-1, 0)   X    (+1, 0)
    (-1,+1) (0,+1) (+1,+1)
    """
    neighbors = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue  # hopp over seg selv
            ny = y + dy
            nx = x + dx
            if 0 <= ny < len_y and 0 <= nx < len_x:
                if warehouse[ny][nx] == '@':
                    neighbors += 1
    return neighbors < 4


def has_nabors_and_rm(warehouse, y, x):
    """
    Samme som has_nabors, men dersom cellen er en tilgjengelig '@',
    merkes den som fjernet (for eksempel med '.')
    og funksjonen returnerer True.
    """
    neighbors = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            ny = y + dy
            nx = x + dx
            if 0 <= ny < len_y and 0 <= nx < len_x:
                if warehouse[ny][nx] == '@':
                    neighbors += 1

    if neighbors < 4 and warehouse[y][x] == '@':
        warehouse[y][x] = '.'   # eller 'X' hvis du vil se fjernede
        return True
    return False


def one_pase(warehouse):
    """
    Én passering over hele lageret:
    - finn alle '@' som er tilgjengelige
    - fjern dem
    - tell hvor mange som ble fjernet
    Vi muterer warehouse in-place og returnerer antall fjernet.
    """
    removed_this_pass = 0
    for y in range(len_y):
        for x in range(len_x):
            # bare interessant om det faktisk er en rull her
            if warehouse[y][x] == '@':
                if has_nabors_and_rm(warehouse, y, x):
                    removed_this_pass += 1
    return removed_this_pass


# Del 2: kjør repeterte pass til ingenting mer fjernes
total_removed = 0
while True:
    removed = one_pase(paperstorage)
    if removed == 0:
        break
    total_removed += removed

print(total_removed)
