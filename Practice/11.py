# 1
# from abc import ABC, abstractclass

# class AbstractCls(ABC):
    
#     @abstractclass
#     def some_method(self):
#         pass
    
        
# 2
# for i in lst:
#     if i == 0:
#         continue
#     else:
#         number /= 1

      
# 3
# try:
#     1 / 0
# except ZeroDivisionError:
#     print("Exception has been caught")
    
# print("still running...")
    
# 4
# try:
#     1 / 0
# except IndexError:
#     print("Exception has been caught")
    
# print("still running...")
    
# 5
# name = input("Enter name: ")

# if len(name) < 6:
#     raise ValueError(f"Given name {name} should be at least 5 characters long...")

# print("still running...")


#6
# lst = [1, 2, 3, 4, 5]

# while len(lst) > 0:
#     print(lst.pop())

# print("still running...")



#7
# lst = [1, 2, 3, 4, 5]

# while True:
#     print(lst.pop())

# print("still running...")

#8
# lst = [1, 2, 3, 4, 5]

# try: 
#     while True:
#         print(lst.pop())
        
# except IndexError:
#     print("List is empty: {lst}")
    
# print("still running...")


#9
# lst = (1, 2, 3, 4, 5)

# try: 
    
#     while True:
#         print(lst.pop())
        
# except Exception:
#     print("List is empty: {lst} ")
    
# print("still running...")


#10
# lst = (1, 2, 3, 4, 5)

# try: 
    
#     while True:
#         print(lst.pop())

# except ArithmeticError:
#     print(f"Not supported type {type(lst)}")        
# except IndexError:
#     print("List is empty: {lst}")
# except Exception:
#     print("List is empty: {lst} ")
    
# print("still running...")


# 11
# def averge_num(sequence):
#     sum_data = 0
#     count = 0
#     try:
#         for element in sequence:
#             try:
#                 sum_data += element
#                 count += 1
#             except TypeError:
#                 pass
        
#         averge = sum_data / count
#     except ZeroDivisionError:
#         averge = 0
        
#     return averge
    
# sequence = [ "qwe"]
# print(averge_num(sequence))

# # 12
# def averge_num(sequence):
#     sum_data = 0
#     count = 0
    
#     for element in sequence:
#         try:
#             sum_data += element
#             count += 1
#         except TypeError:
#             pass
        
#         averge = sum_data / count
        
#     return averge
    
# sequence = [1, 2, 3, 4, "qwe"]
# print(averge_num(sequence))


# 13
# try:
#     raise ValueError("Some exception text")
# except  ValueError as ex:
#     print(f"handled exception: {ex}")
# finally:
#     print("this is always exception")
    
# print("still running...")
        