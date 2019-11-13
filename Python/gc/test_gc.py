import sys
import gc


def print_id_count(obj,name):
    print('\n %s id: %d refer count: %d list: %s' % (name, id(obj), sys.getrefcount(obj),gc.get_referrers(obj)))
    
class testGC():
    def __init__(self, name, age):
        self.name = name
        print(sys.getrefcount(self.name))
        # print(gc.get_referrers(self.name))
        print_id_count(self.name, 'name')
        print('\n %s id: %d refer count: %d list: %s' % (name, id(self.name), sys.getrefcount(self.name),gc.get_referrers(self.name)))
        # print(gc.get_referrers(self))
        # print('\n %s id: %d refer count: %d' % ('self', id(self), sys.getrefcount(self)))
        # print('self.name id: %d refer count: %d' % id(self.name),sys.getrefcount(self.name))
        # self.age = 20
        # print('self id: %d refer count: %d' % id(self),sys.getrefcount(self))
        # print('self.name id: %d refer count: %d' % id(self.name),sys.getrefcount(self.name))
    def __del__(self):
        print('Object was deleted...')
        # print_id_count(self,'self')
        print_id_count((self.name), 'name')


if __name__ == '__main__':
    a = 'wow'
    print(sys.getrefcount(a))
    print(gc.get_referrers(a))
    t = testGC(a, 20)
    # print(sys.getrefcount(a))
    # print(sys.getrefcount(a))
    # print_id_count(a, 'name')
    del t
    print(sys.getrefcount(a))
    # del a
    # a = testGC('wow', 22)
