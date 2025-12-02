def is_double_repeat(num): 
    if len(num)%2 != 0: #111 isn't a palindrom 
        return False
    return num[:len(num)//2] == num[len(num)//2:]
        
       
def is_eny_part_repeting(num):
    length = len(num)
    divisorer = [d for d in range(2, length+1) if length % d == 0]
    #print(divisorer)
    for p in divisorer:
        l2 = int(length/p)
        
        part = num[:l2]
        p2 = ""
        for _ in range(p):
            p2 += part
        if num == p2:
            return True
    return False

is_eny_part_repeting("121212")

f = open("input2.csv", "r") 
input_data = f.read() 
input = input_data.split(",") 
counter = 0 
counter2 = 0

for x in input: 
    start, stop = x.strip().split("-") 
    for y in range(int(start), int(stop)+1): 
        if is_double_repeat(str(y)): 
            #print(y)
            counter += y
        if is_eny_part_repeting(str(y)):
            counter2 += y

print("part 1", counter)
print("part 2 =", counter2)
