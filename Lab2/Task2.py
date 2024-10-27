import numpy as np 
import math  


def function(x, d):
    sum_value = 0.0 
    k = 1  
    while True:
        term = (-1)**k * math.sin(k * x) / k 
        sum_value += term  
        if abs(term) < d:  
            break
        k += 1  
    return sum_value


def tabulate_series(a, b, h, d):
    x_values = np.arange(a, b + h, h)  
    results = []  
    for x in x_values:
        y = function(x, d)  
        results.append((x, y))  
    return results


a = 3.0  
b = 4.0  
h = 0.1  
d = 0.001  
table = tabulate_series(a, b, h, d)  
for x, y in table:
    print(f"x = {x:.1f}, f(x) = {y}")  
