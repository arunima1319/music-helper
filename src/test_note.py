import unittest 
from note import Note 


class TestNote(unittest.TestCase): 

    def test_note_transpose_same_octave(self): 
        note = Note("C", 0, 0.25)
        transposed_note = note.transpose(3)
        new_note = Note("D#", 0, 0.25)
        self.assertEqual(transposed_note.__repr__(), new_note.__repr__())


    def test_note_transpose_lower_octave(self):
        note = Note("C", 0, 0.25)
        transposed_note = note.transpose(-13)
        new_note = Note("B", -2, 0.25)
        self.assertEqual(transposed_note.__repr__(), new_note.__repr__())

    def test_note_transpose_higher_octave(self):
        note = Note("A#", 0, 1.0)
        transposed_note = note.transpose(5)
        new_note = Note("D#", 1, 1.0)
        self.assertEqual(transposed_note.__repr__(), new_note.__repr__())
