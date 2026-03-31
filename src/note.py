class Note: 

    def __init__(self, pitch, octave, length):
        self.pitch = pitch
        self.octave = octave
        self.length = length
        
    
    def __repr__(self):
        return f"note = {self.pitch}, octave = {self.octave}, length = {self.length})"
    
