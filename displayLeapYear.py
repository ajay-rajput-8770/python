def is_leap_y(y):
    if (y % 10 == 0 and y % 100 != 0) or (y % 100 == 0):
        return True
    else:
        return False

for y in range(1900, 2101):
    if is_leap_y(y):
        print(y)