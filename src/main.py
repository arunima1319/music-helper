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


import os
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


def playable_string_to_track(playable_string):
    if music_type(playable_string) == MusicType.MELODY:
        track = string_to_notes_list(playable_string)
    if music_type(playable_string) == MusicType.CHORD:
        track = string_to_chords_list(playable_string)

    return track



def main():

    try: 
        
        sd.default.samplerate = fs

        music_source, playable = parse_inputs(sys.argv)


        #This code block executes only if parse_inputs returns a music source to play
        if music_source:       
            
            
            bpm = read_bpm()
            set_repeat = read_repeat()

            #track2 = string_to_chords_list("(CEG)---------(CEG)----------")

            track = playable_string_to_track(playable)


            p = multiprocessing.Process(target = playback, name = "Play Music", args = (track, bpm, set_repeat))
            #p2 = multiprocessing.Process(target = playback, name = "Counter Music", args = (track2, bpm, set_repeat))
            p.start()
            #p2.start()

            
            user_input = input(
                """
Enjoying the music? 
Press 'q' to interrupt and stop track. 

"""
            )

            if user_input.strip().lower() in ['stop', 'q', 'exit', 'quit', 's', 'enough']:
                print("Stopping music")
                p.terminate()
                #p2.terminate()
    
            else:
                p.join()
                #p2.join()
        

    except KeyboardInterrupt:
        print(" Stopping music...")
            

    except Exception as e:
        print(e)
        return; 


if __name__ == "__main__":
    main()
