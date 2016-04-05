import unittest
from ambrosio import CommandList

class TestCommandList(unittest.TestCase):

    def test_000_newqueue_length(self):
        cl = commandlist.CommandList()
        self.assertEqual(c1.length(),0)

    def test_001_newqueue_cantpop(self):
        cl = commandlist.CommandList()
        self.assertEqual(IndexError,c1.next)


    def test_002_push_then_pop(self):
        cl = commandlist.CommandList()
        c1.append("Test")
        c=c1.next()
        self.assertEqual(c, "Test")

if __name__=="__main__":
    import sys
    sys.exit(unittest.main())
