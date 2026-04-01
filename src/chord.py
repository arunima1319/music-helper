from note import Note
from generator import waveform_generator, freq_duration_generator
from constants import *
import sounddevice as sd 


C = Note("C", 0, 1.0)
E = Note("E", 0, 1.0)
G = Note("G", 0, 1.0)

class Chord():
    def __init__(self, note1 = C, note2 = E, note3 = G):
        self.note1 = note1
        self.note2 = note2
        self.note3 = note3 
        self.length = max(note1.length, note2.length, note3.length)

    def generate_final_waveform(self, bpm):

        note1 = self.note1 
        note2 = self.note2
        note3 = self.note3 

        length = self.length

        freq1, duration1 = freq_duration_generator(note1.pitch, note1.octave, length, bpm)
        freq2, duration2 = freq_duration_generator(note2.pitch, note2.octave, length, bpm)
        freq3, duration3 = freq_duration_generator(note3.pitch, note3.octave, length, bpm)

        waveform1= waveform_generator(freq1, duration1, fs)
        waveform2 = waveform_generator(freq2, duration2, fs)
        waveform3 = waveform_generator(freq3, duration3, fs)

        waveform_final = waveform1 + waveform2 + waveform3 

        return waveform_final
    
    def play(self, bpm):
        waveform_final = self.generate_final_waveform(bpm)
        sd.play(waveform_final)
        sd.wait()





    def transpose(self, semitones):

        new_note1 = self.note1.transpose(semitones)
        new_note2 = self.note2.transpose(semitones)
        new_note3 = self.note3.transpose(semitones)

        new_chord = Chord(new_note1, new_note2, new_note3)

        return new_chord
    

    def __repr__(self): 
        return f"{self.note1.pitch}{self.note1.octave}, {self.note2.pitch}{self.note2.octave}, {self.note3.pitch}{self.note3.octave}, length = {self.length}"