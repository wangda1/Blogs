# test the deleted order in a instance
import gc
import sys

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance 

class G(Singleton):

    def __init__(self):
        self.name = 'global variable'
        print(self.name)

    def __del__(self):
        print(id(self))
        print(sys.getrefcount(self))
        print('%s was deleted' % self.name)   
# class G():
#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         print('Creating Instance')
#         instance = super(G, cls).__new__(cls, *args, **kwargs)
#         return instance

#     def __init__(self):
#         self.name = 'global variable'
#         print(self.name)

#     @classmethod
#     def get_instance(cls):
#         if not cls.__instance:
#             cls.__instance = G()
#             cls.__instance.name = 'global variable single'
#             print(cls.__instance.name)
#         return cls.__instance
#     def __del__(self):
#         print(id(self))
#         print(sys.getrefcount(self))
#         print('%s was deleted' % self.name)


class A():
    def __init__(self):
        self.name = 'little a'
        self.dev = G()
        # print('In A get Global instance')
        print(self.name)
        self._c = C()
    
    def __del__(self):
        print('little a begins to delete')
        # print(id(self.dev))
        print('little a\'s refer count: %d' % sys.getrefcount(self))
        print(sys.getrefcount(self.dev))
        # del self.dev
        # del self._c
        print('little a was deleted')

class B():
    def __init__(self):
        self.name = 'little b'
        self.dev = G()
        # print(id(self.dev))
        # print('In B get global instance')
        print(self.name)
    
    def __del__(self):
        print(sys.getrefcount(self.dev))
        # del self.dev
        print('little b was deleted')

class C():
    def __init__(self):
        self.name = 'little c'
        self.dev = G()
        # print('In C get global instance')
        print(self.name)
    
    def __del__(self):
        # print(id(self.dev))
        # print(self.dev.name)
        print(sys.getrefcount(self.dev))
        # del self.dev
        print('little c was deleted')

class ABC():
    def __init__(self):
        self.name = 'little abc'
        print(self.name)
    def get_ABC(self):
        self._a = A()
        self._b = B()
    def __del__(self):
        print('little abc begins to delete')
        #del self._a                     ## 除非直接作为形参，否则不会将 refer count +1
        print(sys.getrefcount(self._a))
        # del self._a
        print('little abc was deleted')

if __name__ == '__main__':
    # gc.set_threshold(0)
    abc = ABC()
    abc.get_ABC()
    # print('go to objgraph')
    print(sys.getrefcount(abc._a))
    print(sys.getrefcount(abc._b))
    # print(sys.getrefcount(abc._a.dev))
    # import objgraph
    # objgraph.show_backrefs([g.get_instance()], filename='ref.png')
