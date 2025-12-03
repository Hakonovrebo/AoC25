def find_higes_diget(line):
  firstD = 0
  lastD = 1
  for x in range(1, len(line)-1): # scip last, sins last diget cant be first
      if int(line[x]) > int(line[firstD]):
          firstD = x 
          lastD = x+1 if lastD <= firstD else lastD
      lastD = x if int(line[x]) > int(line[lastD]) and x > firstD else lastD
      
  
  lastD = len(line)-1 if int(line[len(line)-1]) > int(line[lastD]) else lastD
  print(line, line[firstD] + line[lastD])
  return int(line[firstD] + line[lastD])

def find_tvel_high(line):
  k = 12  # hvor mange sifre vi skal plukke
  pos = 0
  chosen_digits = []

  for picked in range(k):
      remaining = k - picked  # hvor mange vi fortsatt må plukke etter dette
      # vi kan lete til og med denne indeksen
      max_search_index = len(line) - remaining

      best_digit = -1
      best_index = None

      # finn største siffer vi kan velge for denne posisjonen
      for i in range(pos, max_search_index + 1):
          d = int(line[i])
          if d > best_digit:
              best_digit = d
              best_index = i
              if best_digit == 9:  # kan ikke bli bedre, kan break’e tidlig
                  break

      chosen_digits.append(str(best_digit))
      pos = best_index + 1  # neste siffer må komme etter dette

  return int("".join(chosen_digits))

f = open("input_3.txt", "r")
counter = 0
for line in f:
  #counter += find_higes_diget(line.strip())
  counter += find_tvel_high(line.strip())
print(counter)
