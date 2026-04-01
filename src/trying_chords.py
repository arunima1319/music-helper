from generator import waveform_generator, freq_duration_generator 
import numpy as np
import sounddevice as sd
from chord import Chord
from note import Note
from constants import *


chord = Chord(Note("C", 1, 3.0), Note("E", 1, 2.0), Note("G", 1, 4.0))
bpm = 90

transposed  = chord.transpose(-4)
print(transposed)

sd.play(chord.generate_final_waveform(bpm))
sd.wait()

sd.play(transposed.generate_final_waveform(bpm))
sd.wait()