import unittest
from src.string_to_notes_list import string_to_notes_list

class TestStringToNotesList(unittest.TestCase):

    def test_string_to_notes_list(self):
        string = "C-E-D---"
        notes_list = [("C", 0, 0.5), ("E", 0, 0.5), ("D", 0, 1.0)]
        self.assertEqual(string_to_notes_list(string), notes_list)


    def test_string_to_notes_list_sharp(self):
        string = "C#----B#"
        notes_list = [("C#", 0, 1.25), ("B#", 0, 0.25)]
        self.assertEqual(string_to_notes_list(string), notes_list)


    def test_string_to_notes_list_mixed(self):
        string = "C-C#--D-"
        notes_list = [("C", 0, 0.5), ("C#", 0, 0.75), ("D", 0, 0.5)]
        self.assertEqual(string_to_notes_list(string), notes_list)

    def test_string_to_notes_list_octaves_high_low(self):
        string = "ChB#--Al-"
        notes_list = [("C", 1, 0.25), ("B#", 0, 0.75), ("A", -1, 0.5)]
        self.assertEqual(string_to_notes_list(string), notes_list)

    def test_string_to_notes_list_2(self):
        string = "C---Ch---"
        notes_list = [("C", 0, 1.0), ("C", 1, 1.0)]
        self.assertEqual(string_to_notes_list(string), notes_list)

    def test_string_to_notes_list_invalid(self):
        string = "Ci-D-"

        self.assertRaises(Exception, string_to_notes_list, string)



