
input()
entry = list(map(int,input().split(" ")))
max_1 = max(entry[0], entry[1])
max_2 = min(entry[0], entry[1])
length= len(entry)
i = 2

while i < length:
    if(entry[i] > max_1):
        max_2 = max_1
        max_1 = entry[i]
    else:
        if(entry[i] > max_2):
            max_2 = entry[i]
    i += 1

print( (max_1 * max_2) )
    

