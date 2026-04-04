from constants import *
import numpy as np


def waveform_generator(freq, duration, sample_rate):
    t = np.arange(sample_rate * duration) / sample_rate
    waveform = 0.5 * np.sin(2.0 * np.pi * freq * t)
    return waveform


def freq_duration_generator(note, octave, length, bpm):
    """
    dict= {
        "C": 1,
        "C#" : 2,
        "D": 3,
        "D#": 4,
        "E": 5,
        "F" : 6,
        "F#" : 7,
        "G" : 8,
        "G#": 9,
        "A": 10,
        "A#": 11,
        "B" : 12

    }
    """

    try:
        freq = (
            (2 ** (octave))
            * middle_C_freq
            * ((twelfth_root_of_two) ** (notes_dict[note]))
        )
    except Exception as e:
        print("error: not a valid note")

    duration = (length / bpm) * 60

    return freq, duration
