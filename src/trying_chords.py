from generator import waveform_generator, freq_duration_generator 
import numpy as np
import sounddevice as sd
from chord import Chord
from note import Note
from constants import *


chord = Chord(Note("C", 1, 4.0), Note("E", 1, 4.0), Note("G", 1, 4.0))
bpm = 90
sd.play(chord.generate_final_waveform(bpm))
sd.wait()