input = "987654321111111
811111111111119
234234234234278
818181911112111"

def find_higes_diget(line):
  firstD = 0
  lastD = 1
  for x in range(1, len(line)-1): # scip last, sins last diget cant be first
      if int(line[x]) > int(line[firstD]):
        firstD = x 
        lastD = x+1 if lastD <= firstD else lastD
      lastD = x if int(line[x]) > int(line[lastD]) and x > firstD else lastD
      
    
  lastD = len(line)-1 if int(line[len(line)-1]) > int(line[lastD]) else lastD

  return int(line[firstD] + line[lastD])
      
  
