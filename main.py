from datetime import datetime

INSTALL_DATE = "31.03.2022"
REDUCTION_COEFFICIENT = 85


def panel_degradation(install_date):
    """Take system install date, calculate timedelta between install date and today
    and return system theoretical performance after panel degradation"""

    install_date_obj = datetime.strptime(install_date, "%d.%m.%Y")
    days = (time_now - install_date_obj).days
    if days < 365:
        performance = days / 365 * -0.02 + 1
    else:
        performance = days / 365 * -0.0055 + 0.9855
    return round(performance, 4)


array2D = []
filename = "output.txt"

with open(filename, 'r') as f:
    for line in f.readlines():
        array2D.append(line.split(','))

time_now = datetime.now()
month_now = time_now.month
hour_now = time_now.hour

print(month_now, hour_now)
print(type(month_now), type(hour_now))

string_to_print = f"{array2D[hour_now][0]}, {round(int(array2D[hour_now][month_now]) / REDUCTION_COEFFICIENT, 2)}kWh"
print(string_to_print)


print(panel_degradation(INSTALL_DATE))


