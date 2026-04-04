import unittest
from chord import Chord
from note import Note


class TestChord(unittest.TestCase):

    def test_chord_repr(self):
        chord = Chord()
        output = "(C0, E0, G0, 0.25)"
        self.assertEqual(chord.__repr__(), output)

    def test_note_to_notation_string(self):
        chord = Chord(Note("C", 1), Note("D#", 1), Note("G", 1))
        chord.length = 0.5
        notation_string = "(ChD#hGh)-"
        self.assertEqual(chord.chord_to_notation_string(), notation_string)
