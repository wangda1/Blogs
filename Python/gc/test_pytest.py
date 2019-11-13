import pytest
import unittest

def test_set_mode(mode):
    assert('hello' == 'hello')
    assert(mode == 'hw')
class dev():
    @staticmethod
    def get_mode():
        return 'sim'
    def __init__(self, mode):
        self.mode = mode
    # def get_mode(self):
    #     return self.mode

class Test(unittest.TestCase):
    # @pytest.mark.skipif(dev.get_mode() =='sim', reason="not support")
    @unittest.skipIf(dev.get_mode() == 'sim', "not support")
    def test_mode(self):
        assert(1 == 1)

