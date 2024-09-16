import math

x = 5.168
z = 1.569
y = 3.022

result = (x + 1)**2 + 2 * (y + z) / (x + y - z**2) + 13 * math.log(x * y + z, 5)

print(result)