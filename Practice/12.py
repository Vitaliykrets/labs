# 1 
# lst = [1, 2, 3, 4, 5]

# iterartor = iter(lst)
# print(iterartor)    

# i = 0
# while i < 4:
#     print(next(iterartor))


# 2
# class StudemtGroup():
#     def __init__(self):
#         self.student_list = []
        
#     def add_student(self, student):
#         self.student_list.append(student)    

# grtoup_1 = StudemtGroup()

# for student in grtoup_1:
#     print(student)

# 3
# lst = list(range(13))
# print(lst)

# lst_iter = iter(lst)

# next_ = next(lst_iter)
# print(next_)

# 4
# class StudemtGroup():
#     def __init__(self):
#         self.student_list = []
        
#     def add_student(self, student):
#         self.student_list.append(student)   
        
#     def __str__(self):
#         return ",\n".join(self.student_list)     

# grtoup_1 = StudemtGroup()
# grtoup_1.add("Andrii")
# grtoup_1.add("Petro")
# grtoup_1.add("Yurii")
# grtoup_1.add("Zenovii")

# for student in grtoup_1:
#     print(student)


# 5
# class StudentGroup():
#     def __init__(self):
#         self.student_list = []
        
#     def __iter__(self):
#         self.__idx = 0
#         return self
    
#     def __next__(self):
#         if self.__idx < len(self.student_list):
#             obj = self.student_list[self.__idx]
#             self.__idx += 1
#             return obj
        
#         else:
#             raise IndentationError
             
            
#     def add_student(self, student):
#         self.student_list.append(student)   
        
#     def __str__(self):
#         return ",\n".join(self.student_list)     

# group_1 = StudentGroup()
# group_1.add_student("Andrii")
# group_1.add_student("Petro")
# group_1.add_student("Yurii")
# group_1.add_student("Zenovii")

# print(group_1)



# 6
# def first_gen():
#     print("Hello first time")
#     yield                   # те саме що і return
#     print("Hello second time")
#     yield
#     print("Hello third time")
#     yield

# f_gen = first_gen()
# next(f_gen)
# print("running...")

# next(f_gen)
# print("running...")

# next(f_gen)
# print("running...")



# 7
# lst_a = [el for el in range(5)]
# lst_b = [el for el in range(10,50,10)]\

# print(list(zip(lst_a, lst_b)))

# ipped = list(zip(lst_a, lst_b))

# unzipped = zip(*zipped)
    


# 8
# lst_1 = [1, 2, 3, 4, -12, False]
# any(lst_1)
# all(lst_1)
