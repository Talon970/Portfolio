# Beispiel-Datei: test_math_functions.py

import sys
sys.path.append('/home/howmanywho/Dokumente/Code/programmieren/freecode')


import unittest
from addieren_001 import add

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
