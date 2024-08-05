#653380014-1
import unittest
import CountClump as CountClump

class Test(unittest.TestCase):
    def test_TC01(self):
        result = CountClump.CountClump.count_clumps([0])
        self.assertEqual(result, 0)

    def test_TC02(self):
        result = CountClump.CountClump.count_clumps([5,4,3])
        self.assertEqual(result, 0)

    def test_TC03(self):
        result = CountClump.CountClump.count_clumps([4,4,1,5])
        self.assertEqual(result, 1)

    def test_TC04(self):
        result = CountClump.CountClump.count_clumps(None)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
