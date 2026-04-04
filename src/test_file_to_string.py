import unittest
from file_to_string import file_to_string


class TestFileToString(unittest.TestCase):

    def test_file_to_string(self):

        file = "melodies/test_file.melody"
        music_string = "C--------"
        self.assertEqual(file_to_string(file), music_string)

    def test_file_to_string_invalid(self):

        file = "unhappy_birthday.txt"
        self.assertRaises(Exception, file_to_string, file)
