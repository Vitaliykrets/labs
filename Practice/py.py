# a = float(input("Number: "))

# if a < 0:
#     print("Number < 0")
    
# elif a > 0:
#     print("Number > 0")

# else:
#     print("Number = 0")
         
# a = float(input("Number: "))

# if a < 12 and a >= 0:
#     print("Number in diapason 0 до 12" )
    
# else:
#     print("Число поза діапазону")
        
# Number_1 = float(input("Number_1: "))            

# if Number_1 % 2 == 0.0:
#     print("Число парне")

# else:
#     print("Число непарне")
           
    
# Number_1 = float(input("Number_1: "))
# Number_2 = float(input("Number_2: "))
# Number_3 = float(input("Number_3: "))

# if Number_1 == Number_2 == Number_3:
#     print("Всі числа рівні")
    
# else: 
#     max_number = max(Number_1, Number_2, Number_3)
#     print(f"Max number: {max_number}")

# year = int(input("Year: "))

# if year % 400 == 0:
#     print("Високосний рік!")

# elif year % 100 == 0:
#     print("Рік не високосний")
    
# elif year % 4 == 0:
#     print("Рік є високосний")    
        
# else:
#     print("Рік не високосний")
     
# x = str(input("Name: "))

# print("HI" + ', ' + x)

# list = [12, 21, -12, "a", "Ben", "Danial", True, False]

# list.append(113)
# list.remove(12)
# list[-1] = True

# print(list.count(True))
# print(list)

# my_tuple = (1, 2, -21, "abs", True, False, "Eshkere")

# tupl = my_tuple

# print(tupl)

# Робота

# Kretsul = {}
# Levonovuy = {}
# Sharshevskiy = {"Name": 'Stepan', "age": '17', "G"}

# list = [1, -21, 0, 32, -1]

# list.pop(0)
# або
# list.remove(-1)
# list.append(0)
# print(list)

# lst_1 = [1, 2, 3, 4, 5, 6]

# for el in lst_1:
#     print(f"el: {el}")
#     if el == 3:
#         print(f"skipping {el} element")
#         continue
#     print(f"el: {el}")
    
#     print("Done")
    
# lst_2 = []
# lst_2.append(1)
# lst_2.append(4)
# lst_2.append(8)
# lst_2.append(21)
# lst_2.append(9)
# lst_2.append(3)

# print(lst_2)

# tpl1 = (1, 2, 3, 4, 5, 6)

# print(tpl1)

# tpl2 = (1, 2, 3, [11, 22, 33], "asd", "qwe")

# len(tpl2)

# tpl2[3][2] = "Test_value"
# tpl2[3].append("new el")

# print(tpl2)

# lst_3 = [1]
# lst_4 = list([1])

# tpl_3 = (123, "asd")

# print(type(tpl_3))

# set_1 = {1, 2, 3, 4, 5, 6, 7}
# for el in set_1:
#     print(el)
#     print("Done")

# lst_5 = [1, 2, 1, 2, "a", "a"]
# print(set(lst_5))


# dict_1 = {1: "qwe", 2: "abs", 3: "czx", "val": 3123}

# def say_hello4(name):
#     print(f"Hello {name}")
   
# say_hello4("Bill")   
# say_hello4("Bella") 
# say_hello4("Ben") 

# tmp_3 = say_hello4
# tmp_3("Andrii")

# def fuc_1(lst):
#     lst[0] = "new"
    
# lst_1 = list(range(10))
    
# print(lst_1)    
# fuc_1(lst_1)
# print(lst_1)
    

# lst_2 = lst_1
# lst_1[1] = "new"
# print(lst_2)

# def fuc_1(lst):
#     lst = lst[:]
#     lst[0] = "new"
    
#     return lst

# lst_1 = list(range(10))
    
# print(lst_1)    
# lst_2 = fuc_1(lst_1)
# print(lst_1)
# print(lst_2)
    

# lst_2 = lst_1
# lst_1[1] = "new"
# print(lst_2)

# for i in range(10):
#     x = i**2
#     print(f"x value from for = {x}") 

# print(f"x value from for outer = {x}")

# globals().get('x', False)

# 'lst_1' in globals ()

# a_globals = 123

# def fnc_2():
#     # a_globals = "qwe"
#     global a_globals
#     a_globals = "new value"
#     print(f"value from {fnc_2.__name__}: = {a_globals}")

# print(f"a_globals value = {a_globals}")
# fnc_2()
# print(f"a_globals value = {a_globals}")

# def outer():
#     a = "hello"
#     def inner():
        
#         a = "python"
#         print(f"inner fnc: {a}")
        
#     inner()
#     print(f"outer fnc: {a}")

# outer()

# def outer():
#     a = "hello"
#     print(f"outer fnc: {a}")
#     def inner():
#         nonlocal a
#         a = "python"
#         print(f"inner fnc: {a}")
        
#     inner()
#     print(f"outer fnc: {a}")

# outer()

# def add_(a, b):
#     return a + b

# def say_hello(name):
#     return f"Hello: {name}"
    

# def outer():
#     x = "hello"
#     print(f"x = {x}") 
    
#     def inner():
#         print(f"inner fnc x = {x}")
        
#     return inner    
 
# fnc_23 = outer()
# print(fnc_23())

# def outer(a, b):
#     def inner(c):
#         return c**2
    
#     print(f"a = {a}, b = {b}")
#     return inner

# fnc_3 = outer(2,9)
# print(fnc_3(11))
# print(fnc_3(4))

# def power(n):
#     def inner(x):
#         return x**n
#     return inner

# cube = power(3)
# # cube.__closure__
# # cube.__code__.co_freevars
# square = cube(2)

# print(cube(5))
# print(square)


# def add_(*args):
#     sum_ = 0
#     for el in args:
#         sum_ += el
#         return sum_
    
# def executor(fnc_name):
#     def inner(*args, **kwargs):
#         result = fnc_name(*args, **kwargs)
#         return result
#     return inner    

# add_executor = executor(add_)

# print(add_(1, 3))
# print(add_executor(4, 6, 11))

# def mul_(*args):
#     prod = 1
#     for el in args:
#         prod *= el
#     return prod

# mul_executor = executor(mul_)
# print(mul_(1, 3, 4, 7))    
# print((add_executor(1, 1, 2, 3, 4, 1)))



# def count_fnc_calls(fnc):
#     count = 0
    
#     def inner(*args, **kwargs):
#         nonlocal count
#         count = count + 1
#         result = fnc(*args, **kwargs)
#         print(f"Fuction is called {count} times")
#         return result
#     return inner

# @count_fnc_calls
# def fnc_5():
#     print("Hello")
    
# print(fnc_5())

# 25.10.2024

# class Circle:
#     pass

# c1 = Circle()

# # print(type(c1))

# c2 = object.__new__(Circle)
# print(c2)


# class Point:
#     def __new__(cls, x, y):
#         print(f"Hello from the __new__ method")
#         obj = object.__new__(cls)
#         return obj
    
#     def __init__(self, x, y):
#         print(f"Hello from the __init__ method")
#         self.x = x
#         self.y = y
        
# p4 = Point(22, 23)

# print(p4.__dict__)

# class Point2:
#     def __new__(cls, x, y):
#         print(f"Hello from the __new__ method")
#         obj = object.__new__(cls)
#         obj.x = x
#         obj.y = y
#         return obj
    
# p5 = Point2(33, 44)
# print(p5.__dict__)   

# class Point3:
#     cls_var = 0
    
#     def __new__(cls, x, y):
#         print(f"Hello from the __new__ method")
#         obj = object.__new__(cls)
#         return obj
    
#     def __init__(self, x, y):
#         print(f"Hello from the __init__ method")
#         self.x = x
#         self.y = y
        
#     @staticmethod
#     def say_hello():
#         print(f"Hello say_Hello method")
       
# p10 = Point3(55, 66)                  
# p10.say_hello()

# Point3.say_hello()

# class Student:
#     def __init__(self, name, rating):
#         self.__name = name
#         self.__rating = rating
        
#     @property  
#     def rating(self):
#         return self.__rating
        
#     def __eq__(self, other):
#         return self.__rating == other.__rating
        
#     def __nq__(self, other):
#         return not self.__eq__(other)
                
# stud_1 = Student("Andrii", 76)
# stud_2 = Student("Mykola", 99)        
# stud_3 = Student("Pavlo", 50)

# stud_1 != stud_2

# > __gt__
# < __lt__
# <= __le__
# == __eq__
# != __ne__
# >= __ge__



























































