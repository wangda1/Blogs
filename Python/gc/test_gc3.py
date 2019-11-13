import sys
import gc

class O():
    def __init__(self):
        self.name = 'I am a O'
    def __del__(self):
        print('Oops, O is deleted')

if __name__ == '__main__':
    o = O()
    c = o
    print(id(o))
    o.__del__()
    print(c.name)
    print(id(c))
