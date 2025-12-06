#tall på samme index skal sumeres eller ganges sammen avhengig av hva som er siste 

with open("input_5.txt") as f:
    data = f.read().strip()
numbers = []
for line in len(data)-1: # vil ikke ha med siste da det er operatoren og ikke tall 
    numbers.append(line.splitt(" "))


