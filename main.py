# class A:
#     def do_somethink(selfself):
#         print('AA')
# class B(A):
#     def do_somethink(self):
#         print('BB')
# obj = B()
# obj.do_somethink()
#
#
# class A:
#     def do_somethink(selfself):
#         print('AA')
# class B(A):
#     def do_somethink(self):
#         super().do_somethink()
#         print('BB')
# obj = B()
# obj.do_somethink()
#
# class A:
#     def __init__(self, a):
#         self.a = a
# class B:
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b

#
# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def summ(self):
#       print(self.a + self.b)
#
#     def otn(self):
#         print(self.a - self.b)
#     def delenie(self):
#         print(self.a / self.b)
#     def umn(self):
#         print(self.a * self.b)
# obj = Calculator(10, 5)
# obj.summ()
# obj.otn()
# obj.delenie()
# obj.umn()

# class Calc:
#     def sum(self, a, b):
#         print(a+b)
#     def minus(self, a, b):
#         print(a-b)
# c = Calc()
# # c.sum(1, 5)
# print(dir(Calc))

class SomeClass:
    var = 'text'
    def __init__(self, new_var):
        self.new_var = new_var
a = SomeClass(1)
b = SomeClass(2)
print(a.new_var, a.var)
print(b.new_var, b.var)

