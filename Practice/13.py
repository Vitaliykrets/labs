# 1
# class A:
#     def __init__(self):
#         print("class A")

# class B(A):
#     def __init__(self):
#         print("class B")
#         super().__init__()
        
# class X:
#     def __init__(self):
#         print("class X")
#         super().__init__()
        
# class Forward(B, X):
#     def __init__(self):
#         print("class Forward")
#         super().__init__() 
        
# class Backward(X, B):
#     def __init__(self):
#         print("class Backward")
#         super().__init__() 
 
# b = B()
# x = X()
# bb = Backward()
# f = Forward()
 
# 2
class Cls_1:
    def m(self):
        print("m from Cls_1")
        

class Cls_2(Cls_1):
    def m(self):
        print("m from Cls_2")
             

class Cls_3(Cls_1):
    def m(self):
        print("m from Cls_3")
        
cls_1 = Cls_1()
cls_2 = Cls_2()
cls_3 = Cls_3()
        
cls_1.m()
cls_2.m()
cls_3.m()


class Cls_4(Cls_2, Cls_1):
    pass
 
cls_4 = Cls_4
cls_4.m()        
# 3


# 4


# 5        

        
        