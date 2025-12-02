current_pos = 50
counter = 0

with open("input_1.txt", "r") as f:
    for l in f:
        l = l.strip()
        if not l:
            continue

        direction = l[0]
        amount = int(l[1:])
        step = 1 if direction == "R" else -1

        for _ in range(amount):
            current_pos = (current_pos + step) % 100
            if current_pos == 0:
                counter += 1

print(counter)
