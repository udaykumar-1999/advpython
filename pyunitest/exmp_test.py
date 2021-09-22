# unitest
# integration, api
# pytest, pyunit, robot ... (frameworks)

import unittest


# python -m unitest test_module test_upper
# python -m unittest testmodule.Testclass
# python -m unittest testmodule.Testclass.test_method

class Testexample(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('uday'.upper(), 'UDAY')

    def test_isupper(self):
        self.assertTrue('UDAY'.isupper())
        self.assertFalse('uday'.isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ['hello', 'world'])
        

if __name__ == '__main__':
    unittest.main()
