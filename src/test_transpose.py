import unittest
from transpose import transpose

class TestTranspose(unittest.TestCase):

    def test_transpose(self): 
        original_string = "C-D-E-C---"
        
        transposed_string = transpose(original_string, 1)
        new_string = "C#-D#-F-C#---"
        self.assertEqual(transposed_string, new_string)