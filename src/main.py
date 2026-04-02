import numpy as np
import sounddevice as sd
import sys
from constants import *
from string_to_notes_list import string_to_notes_list
from string_to_chords_list import string_to_chords_list 
from file_to_string import file_to_string
from generator import waveform_generator, freq_duration_generator
from file_edit import file_edit
from record_music_attempt import record_music_attempt
from note import Note
from parse_inputs import parse_inputs
from music_type import music_type, file_music_type
from read_update_files import * 
from playback import playback, playable_string_to_track
from create_processes import create_processes




def main():

    try: 
        
        sd.default.samplerate = fs

        source_music = parse_inputs(sys.argv)
   

        #This code block executes only if parse_inputs returns one or more music sources to play
        if source_music:  

            processes = create_processes(source_music)

            for p in processes:
                p.start()

            user_input = input(
                """
Enjoying the music? 
Press 'q' to interrupt and stop track. 

"""
            )

            if user_input.strip().lower() in ['stop', 'q', 'exit', 'quit', 's', 'enough']:
                print("Stopping music")
                for p in processes:
                    p.terminate()
            
            else:
                for p in processes:
                    p.join()
           

    except KeyboardInterrupt:
        print(" Stopping music...")
            

    except Exception as e:
        print(e)
        return; 


if __name__ == "__main__":
    main()
