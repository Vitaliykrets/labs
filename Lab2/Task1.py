import numpy as np  
import math 

def function1(x):
    if x < 0.3:
        
        return -math.log(x**2) + math.exp(x)
    elif 0.3 <= x < 0.4:
       
        return 1 / math.tan(x**2 + 4)
    else:
        
        return math.tan(x**2 + 1)


def function2(a, b, h):
    x_values = np.arange(a, b + h, h)  
    results = []  
    for x in x_values:
        try:
            y = function1(x)  
            results.append((x, y))  
        except ValueError:  
            results.append((x, 'undefined'))
    return results


a = 0.2  
b = 0.5  
h = 0.01  
table = function2(a, b, h)  
for x, y in table:
    print(f"x = {x:.2f}, f(x) = {y}")  
