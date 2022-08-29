class A:
    def feature1(self):
        print('feature 1 is working')
    
    def feature2(self):
        print('feature 2 is working')



class B:
    def feature3(self):
        print('feature 3 is working')
    
    def feature4(self):
        print('feature 4 is working')


class C(A,B):
    def hello(self):
        print('hello bro')



a1 = A()
b1 = B()

c1 = C()

c1.hello()