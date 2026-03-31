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


import os

def main():

    try: 
        fs = 44100
        sd.default.samplerate = fs
        

        if len(sys.argv) == 2:   #just a melody is being played
            if sys.argv[1][-4:] == ".txt" or sys.argv[1] == "f":
                melody_source = PlayType.FILE

                if sys.argv[1][-4:] == ".txt":
                    with open ("latest_file_used.txt", "w") as f:
                        f.write(sys.argv[1])

                with open("latest_file_used.txt", "r") as f:
                    file = f.read()
                
                music_string = file_to_string(file)
                
    
            else:
                melody_source = PlayType.CLI
                music_string = sys.argv[1]
                record_melody_attempt(sys.argv[1])
                

            print(melody_source)
            
        elif len(sys.argv) == 3:
            if sys.argv[2][-4:] ==".txt":
                with open("latest_file_used.txt", "w") as f:
                    f.write(sys.argv[2])
            with open("latest_file_used.txt", "r") as f:
                file = f.read()
            
            file_edit(sys.argv[1], file)
            

            return;


        else:
            print(invalid_argument_text)
            return;
        
        music = string_to_notes_list(music_string)
        tones= []

        for note in music:  
            tones.append(freq_duration_generator(note.pitch, note.octave, note.length, 90))


        list_of_waveforms = []
        for i in range(0, len(tones)):
            freq, duration  = tones[i]
            list_of_waveforms.append(waveform_generator(freq, duration, fs))


        for waveform in list_of_waveforms:
            sd.play(waveform)
            sd.wait()

    except Exception as e:
        print(e)
        return; 


if __name__ == "__main__":
    main()
