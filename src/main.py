import numpy as np
import sounddevice as sd
import sys
from constants import *
from string_to_notes_list import string_to_notes_list
from file_to_string import file_to_string
from generator import waveform_generator, freq_duration_generator
from file_edit import file_edit
from record_melody_attempt import record_melody_attempt
from note import Note
from parse_inputs import parse_inputs, read_bpm
 

import os

def main():

    try: 
        
        sd.default.samplerate = fs

        melody_string, melody_source = parse_inputs(sys.argv)

        if melody_string:       #This code block executes only if parse_inputs returns a melody string
            
            

            bpm = read_bpm()

            notes = string_to_notes_list(melody_string)

            if melody_source == PlayType.CLI:
                if notes:       #ensuring that the melody_string was valid, and string_to_notes returned a list of notes
                    record_melody_attempt(melody_string)
            
            waveform_list = []
            for note in notes:  
                waveform_list.append(note.generate_final_waveform(bpm))


            for waveform in waveform_list:
                sd.play(waveform)
                sd.wait()

    except Exception as e:
        print(e)
        return; 


if __name__ == "__main__":
    main()
