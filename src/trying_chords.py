from generator import waveform_generator, freq_duration_generator
import numpy as np
import sounddevice as sd
from chord import Chord
from note import Note
from constants import *
from string_to_chords_list import string_to_chords_list

chord_string = "(D#F#A)---(BD#hF#h)"
chords = string_to_chords_list(chord_string)

"""
default_chord = Chord()


chord = Chord(Note("C", 1, 3.0), Note("E", 1, 2.0), Note("G", 1, 4.0))
bpm = 90

default_chord.play(bpm)

transposed  = chord.transpose(-4)
print(transposed)

"""
