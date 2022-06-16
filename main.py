from datetime import datetime

array2D = []

filename = "output.txt"

with open(filename, 'r') as f:
    for line in f.readlines():
        array2D.append(line.split(','))

# counter = 1
# for row in array2D:
#     if len(row) == 13:
#         print(f"{counter}) OK")
#     else:
#         print(f"{counter}) FAIL!")
#     counter +=1

time_now = datetime.now()
month_now = time_now.month
hour_now = time_now.hour

print(month_now, hour_now)
print(type(month_now), type(hour_now))

string_to_print = f"{array2D[hour_now][0]}, {round(int(array2D[hour_now][month_now]) / 85, 2)}kWh"
print(string_to_print)


# print(array2D)
# print(array2D[1][0:2])
