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
from parse_inputs import parse_inputs
from read_update_files import * 
 

import os

def main():

    try: 
        
        sd.default.samplerate = fs

        music_source = parse_inputs(sys.argv)

        if music_source:       #This code block executes only if parse_inputs returns a music source to play
            
            
            bpm = read_bpm()


            if music_source == PlayType.CLI:
                music_string = sys.argv[1]
                notes = string_to_notes_list(music_string)

                if notes:       #ensuring that the melody_string was valid, and string_to_notes returned a list of notes
                    record_melody_attempt(music_string)

            elif music_source == PlayType.FILE:
                file = read_latest_file_used()
                music_string = file_to_string(file)
                notes = string_to_notes_list(music_string)
            

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
