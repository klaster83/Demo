array2D = []

filename = "output.txt"

with open(filename, 'r') as f:
    for line in f.readlines():
        array2D.append(line.split(','))

counter = 1
for row in array2D:
    if len(row) == 13:
        print(f"{counter}) OK")
    else:
        print(f"{counter}) FAIL!")
    counter +=1


# print(array2D)
# print(array2D[1][0:2])
