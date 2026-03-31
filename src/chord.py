from note import Note
from generator import waveform_generator, freq_duration_generator
from constants import *


class Chord():
    def __init__(self, note1, note2, note3):
        self.note1 = note1
        self.note2 = note2
        self.note3 = note3 


    def generate_final_waveform(self, bpm):

        note1 = self.note1 
        note2 = self.note2
        note3 = self.note3 

        freq1, duration1 = freq_duration_generator(note1.pitch, note1.octave, note1.length, bpm)
        freq2, duration2 = freq_duration_generator(note2.pitch, note2.octave, note2.length, bpm)
        freq3, duration3 = freq_duration_generator(note3.pitch, note3.octave, note3.length, bpm)

        waveform1= waveform_generator(freq1, duration1, fs)
        waveform2 = waveform_generator(freq2, duration2, fs)
        waveform3 = waveform_generator(freq3, duration3, fs)

        waveform_final = waveform1 + waveform2 + waveform3 

        return waveform_final