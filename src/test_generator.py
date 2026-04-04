import unittest
from generator import freq_duration_generator
from constants import *


class TestGenerator(unittest.TestCase):

    def test_freq_duration_generator(self):
        freq, duration = freq_duration_generator("C", 1, 0.5, 120)
        self.assertEqual(freq, 2 * middle_C_freq)
