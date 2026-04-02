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
import threading
import multiprocessing

def playback(track, bpm, set_repeat):

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
        print("Track completed, press Enter")         


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

            #stop_flag = threading.Event()  
            #stop_flag.clear()   #making sure it's set to False              
            
            p = multiprocessing.Process(target = playback, name = "Play Music", args = (track, bpm, set_repeat))
            
            p.start()

            
            user_input = input(
                """
Enjoying the music? 
Enter 'stop' to interrupt and stop track. 

"""
            )

            if user_input.strip().lower() in ['stop', 'q', 'exit', 'quit', 's', 'enough']:
                print("Stopping music")
                p.terminate()
            elif "stop" in user_input:
                p.terminate()
            else:
                p.join()
        

    except KeyboardInterrupt:
        print(" Stopping music...")
            

    except Exception as e:
        print(e)
        return; 


if __name__ == "__main__":
    main()
