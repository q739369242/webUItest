import unittest
'''
1）.assertEqual(self, first, second,msg=None)
–判断两个参数相等：first == second
2）.assertNotEqual(self, first, second,msg=None)
–判断两个参数不相等：first ！= second
3）.assertIn(self, member, container,msg=None)
–判断是字符串是否包含：member in container
4）.assertNotIn(self, member,container, msg=None)
–判断是字符串是否不包含：member not in container
5）.assertTrue(self, expr, msg=None)
–判断是否为真：expr is True
6）.assertFalse(self, expr, msg=None)
–判断是否为假：expr is False
7）.assertIsNone(self, obj, msg=None)
–判断是否为None：objis None
8）.assertIsNotNone(self, obj,msg=None)
–判断是否不为None：obj is not None
'''
class Test(unittest.TestCase):

    def testA(self):
        '''判断a == b'''
        a = 1
        b = 1
        self.assertEqual(a, b)

    def testB(self):
        '''判断a in b'''
        a = "hi!"
        b = "hi! leihao"
        self.assertIn(a, b)

    def testC(self):
        '''判断a is True'''
        a = True
        self.assertTrue(a)

    def testD(self):
        '''失败案例'''
        a = "aaa"
        b = "bbb"
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()
