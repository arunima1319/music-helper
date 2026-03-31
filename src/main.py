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
        
        sd.default.samplerate = fs


        if len(sys.argv) == 2:   #just a melody is being played or bpm is being set
            
            if sys.argv[1][0:6] == "setbpm":
                bpm = sys.argv[1][6:]
                with open ("bpm.txt", "w") as f:
                    f.write(bpm)
                return;
                

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
    


        with open ("bpm.txt", "r") as f:
            bpm = int(f.read())

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
