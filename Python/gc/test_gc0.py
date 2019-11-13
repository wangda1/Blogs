import sys
import gc

def print_id_count(obj,name):
    print('\n %s id: %d refer count: %d list: %s' % (name, id(obj), sys.getrefcount(obj),gc.get_referrers(obj)))
 
if __name__ == '__main__':
    print(sys.getrefcount('wow'))
    print_id_count('wow', 'a')
    a = 'wow'
    print('referred by a -- "wow"')
    print_id_count('wow', 'wow')
    print_id_count(a, 'a')
    b = 'wow'
    print('referred by b -- "wow" ')
    print_id_count('wow', 'wow')
    print_id_count(a, 'a')
    print_id_count(b, 'b')