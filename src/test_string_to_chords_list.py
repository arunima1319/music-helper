import unittest
from string_to_chords_list import string_to_chords_list 



class TestStringToChordsList(unittest.TestCase): 

    def test_string_to_chords_list(self):

        string = "(D#F#A)---"
        chords = string_to_chords_list(string)
        for chord in chords:
            output = chord.__repr__() + " + "

        check = "(D#0, F#0, A0, 1.0) + "
        self.assertEqual(output, check)
        

    def test_string_to_chords_list_multiple(self):

        string = "(D#F#A)---(BD#hF#h)"
        chords = string_to_chords_list(string)

        output = ""
        for chord in chords:
            output += chord.__repr__() + " + "

        check = "(D#0, F#0, A0, 1.0) + (B0, D#1, F#1, 0.25) + "
        self.assertEqual(output, check)
        
