# test the deleted order in a instance
import gc
import sys

class G():
    __instance = None

    def __init__(self):
        self.name = 'global variable'
        print(self.name)

    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = G()
            cls.__instance.name = 'global variable single'
            print(cls.__instance.name)
        return cls.__instance
    def __del__(self):
        print('%s was deleted' % self.name)

g = G()



class C():
    def __init__(self):
        self.name = 'little c'
        # self.dev = g.get_instance()
        # print('In C get global instance')
        print(self.name)
    def work(self):
        self.dev = g.get_instance()
    def __del__(self):
        print(id(self.dev))
        print(self.dev is None)
        print('little c was deleted')

if __name__ == '__main__':
    # gc.set_threshold(0)
    # g.get_instance()
    c = C()
    c.work()
    # import objgraph
    # objgraph.show_refs([c],filename='c.png')

