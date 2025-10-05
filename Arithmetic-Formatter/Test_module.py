import unittest
from arithmetic_arranger import arithmetic_arranger

class TestAF(unittest.TestCase):
    def test1(self):
        prob = ["3801 - 2", "123 + 49"]
        result = arithmetic_arranger(prob)
        expected = "  3801      123\n-    2    +  49\n------    -----"
        self.assertEqual(result, expected)
    
    def test2(self):
        prob = ["1 + 2", "1 - 9380"]
        result = arithmetic_arranger(prob)
        expected = "  1         1\n+ 2    - 9380\n---    ------"
        self.assertEqual(result, expected)
    
    def test3(self):
        prob = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
        result = arithmetic_arranger(prob)
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(result, expected)
    
    def test4(self):
        prob = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
        result = arithmetic_arranger(prob)
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        self.assertEqual(result, expected)
    
    def test5(self):
        prob = ["1 + 2", "3 + 4", "5 + 6", "7 + 8", "9 + 10", "11 + 12"]
        result = arithmetic_arranger(prob)
        self.assertEqual(result, "Error: Too many problems.")
    
    def test6(self):
        prob = ["1 * 2", "3 + 4"]
        result = arithmetic_arranger(prob)
        self.assertEqual(result, "Error: Operator must be '+' or '-'.")
    
    def test7(self):
        prob = ["1a + 2", "3 + 4"]
        result = arithmetic_arranger(prob)
        self.assertEqual(result, "Error: Numbers must only contain digits.")
    
    def test8(self):
        prob = ["12345 + 2", "3 + 4"]
        result = arithmetic_arranger(prob)
        self.assertEqual(result, "Error: Numbers cannot be more than four digits.")
    
    def test9(self):
        prob = ["3 + 855", "988 + 40"]
        result = arithmetic_arranger(prob, True)
        expected = "    3      988\n+ 855    +  40\n-----    -----\n  858     1028"
        self.assertEqual(result, expected)
    
    def test10(self):
        prob = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]
        result = arithmetic_arranger(prob, True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        self.assertEqual(result, expected)

if __name__ == '__main__':
  
    unittest.main()
