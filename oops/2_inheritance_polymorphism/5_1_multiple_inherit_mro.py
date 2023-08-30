class A(object):
    def dothis(self):
        print("from class A")

class B(A):
    pass

class C(object):
    def dothis(self):
        print("from class C")

class D(B,C):
    pass

d_inst=D()
d_inst.dothis()

print(D.mro())