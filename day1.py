curent_pos = int
"""
input =
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
curent_pos = 50
counter = 0
for l in input:
  if l[0] == "L":
    curent_pos= (curent_pos - int(l[1:]))%100 
  else 
    curent_pos= (curent_pos + int(l[1:]))%100 
  if curent_pos == 0, counter += 1 
print counter
