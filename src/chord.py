from note import Note
from generator import waveform_generator, freq_duration_generator
from constants import *
import sounddevice as sd 


C = Note("C", 0, 0.25)
E = Note("E", 0, 0.25)
G = Note("G", 0, 0.25)

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



    def chord_to_notation_string(self):
        notation_string = "("
        list_of_notes = [self.note1, self.note2, self.note3]
        for note in list_of_notes: 
            notation_string += note.pitch
            if note.octave < 0:
                notation_string +=(note.octave*(-1))*"l"
            elif note.octave > 0:
                notation_string +=(note.octave)*"h"
            else:
                pass
        notation_string += ")"
        
        notation_string += "-"*int((self.length/(0.25)) - 1.0)
        return notation_string

    def transpose(self, semitones):

        new_note1 = self.note1.transpose(semitones)
        new_note2 = self.note2.transpose(semitones)
        new_note3 = self.note3.transpose(semitones)

        new_chord = Chord(new_note1, new_note2, new_note3)
        new_chord.length= self.length

        return new_chord
    

    def __repr__(self): 
        return f"({self.note1.pitch}{self.note1.octave}, {self.note2.pitch}{self.note2.octave}, {self.note3.pitch}{self.note3.octave}, {self.length})"