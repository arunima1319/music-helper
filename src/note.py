from constants import notes_dict, number_to_notes_dict, fs 
from generator import freq_duration_generator, waveform_generator
import sounddevice as sd

class Note: 

    def __init__(self, pitch = "C", octave = 0, length = 1.0):
        self.pitch = pitch
        self.octave = octave
        self.length = length
        
    def transpose(self, semitones): 

        pos_in_octave = notes_dict[self.pitch] 
        new_octave = self.octave + (pos_in_octave + semitones)//12 
        new_pitch_number = (pos_in_octave + semitones)%12
        new_pitch = number_to_notes_dict[new_pitch_number] 
        

        new_note = Note(new_pitch, new_octave, self.length)
        return new_note

    def note_to_notation_string(self):
        notation_string = self.pitch
        if self.octave < 0:
            notation_string +=(self.octave*(-1))*"l"
        if self.octave > 0:
            notation_string +=(self.octave)*"h"
        
        notation_string += "-"*int((self.length/(0.25)) - 1.0)
        return notation_string
    
    def generate_final_waveform(self, bpm):
        freq, duration = freq_duration_generator(self.pitch, self.octave, self.length, bpm)
        waveform = waveform_generator(freq, duration, fs)
        return waveform
    
    def play(self, bpm):
        sd.play(self.generate_final_waveform(bpm))
        sd.wait()

    def __repr__(self):
        return f"pitch = {self.pitch}, octave = {self.octave}, length = {self.length})"
    
