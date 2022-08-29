from mimetypes import init


class A:
    def __init__(self) -> None:
        print('in A init')
    def feature1(self):
        print('feature 1 is working')
    
    def feature2(self):
        print('feature 2 is working')



class B:
    def __init__(self) -> None:
        print('in B init')

    def feature3(self):
        print('feature 3 is working')
    
    def feature4(self):
        print('feature 4 is working')

class C(A,B):
    def __init__(self) -> None:
        print('in C init')
        super().__init__()

a1 = C()


