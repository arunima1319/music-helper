import unittest
from transpose import transpose_chord, transpose_melody

class TestTranspose(unittest.TestCase):

    def test_transpose_melody(self): 
        original_string = "C-D-E-C---"
        
        transposed_string = transpose_melody(original_string, 1)
        new_string = "C#-D#-F-C#---"
        self.assertEqual(transposed_string, new_string)

    def test_transpose_chord(self):
        original_string = "(CEG)---"
        transposed_string = transpose_chord(original_string, 7)
        new_string = "(GBDh)---"
        self.assertEqual(transposed_string, new_string)
