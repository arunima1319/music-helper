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
from music_type import music_type 
from read_update_files import * 
 

import os

def main():

    try: 
        
        sd.default.samplerate = fs

        music_source = parse_inputs(sys.argv)

        if music_source:       #This code block executes only if parse_inputs returns a music source to play
            
            
            bpm = read_bpm()
            set_repeat = read_repeat()


            if music_source == PlayType.CLI:
                music_string = sys.argv[1]
                track = string_to_notes_list(music_string) if music_type(music_string) == MusicType.MELODY else string_to_chords_list(music_string)

                if track:       
                    record_music_attempt(music_string)

            elif music_source == PlayType.FILE:
                file = read_latest_file_used()

                if file.split(".")[1] == "melody": 
                    file_path = f"melodies/{file}"
                    music_string = file_to_string(file_path)
                    track = string_to_notes_list(music_string)

                elif file.split(".")[1] == "chord":
                    file_path = f"chords/{file}"
                    music_string = file_to_string(file_path)
                    track = string_to_chords_list(music_string)
                            

            if set_repeat == "Y":
                i = 0
                while i < len(track):
                    track[i].play(bpm)
                    if i == len(track) -1:
                        i = 0
                    else:
                        i += 1
                
                
            elif set_repeat == "N":
                for music in track:
                    music.play(bpm)  


            

    except Exception as e:
        print(e)
        return; 


if __name__ == "__main__":
    main()
