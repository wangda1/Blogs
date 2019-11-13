import sys

class B():
    def __init__(self):
        self.name = 'little b construct'
    def __del__(self):
        print(sys.getrefcount(self))
        print('little b was deleted')

class A():
    def __init__(self):
        print('little a construct')
        self._b = B()

    def __del__(self):
        del self._b   # makes B' reference minus 1
        print('little a was deleted')

if __name__ == '__main__':
    a = A()

