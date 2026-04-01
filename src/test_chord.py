import unittest
from chord import Chord
from note import Note

class TestChord(unittest.TestCase):

    def test_chord_repr(self): 
        chord = Chord()
        output = "(C0, E0, G0, 0.25)"
        self.assertEqual(chord.__repr__(), output)


