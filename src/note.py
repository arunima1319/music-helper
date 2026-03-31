from constants import notes_dict, number_to_notes_dict 

class Note: 

    def __init__(self, pitch, octave, length):
        self.pitch = pitch
        self.octave = octave
        self.length = length
        
    def transpose(self, semitones): 

        pos_in_octave = notes_dict[self.pitch] 
        new_octave = self.octave + (pos_in_octave + semitones)//12 
        new_pitch_number = (pos_in_octave + semitones)%12
        print(new_pitch_number)
        new_pitch = number_to_notes_dict[new_pitch_number] 
        

        new_note = Note(new_pitch, new_octave, self.length)
        return new_note

    def __repr__(self):
        return f"pitch = {self.pitch}, octave = {self.octave}, length = {self.length})"
    
