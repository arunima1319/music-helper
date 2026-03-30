import numpy as np
import sounddevice as sd
import sys
from constants import *
from string_to_notes_list import string_to_notes_list
from generator import waveform_generator, freq_duration_generator


def main():

    fs = 44100
    sd.default.samplerate = fs

    if len(sys.argv) == 2: 
        music_string = sys.argv[1]

    elif len(sys.argv) == 1:
        music_string = "CDEEEEEEE--EEDEF--"
 
    else:
        print("Your melody should not have spaces in between")
        return;
        

    try: 
        music = string_to_notes_list(music_string)
    except Exception as e:
        print(e)
        return; 

    

    #music = [("C", 0.5)] + [("D", 0.5)] + [("E", 0.5)]*6 + [("E", 1)] + [("E", 0.5)]*2 + [("D", 0.5)] + [("E", 0.5)] + [("F", 1)]
    tones= []

    for note in music:  
        tones.append(freq_duration_generator(note[0], note[1], 100))


    list_of_waveforms = []
    for i in range(0, len(tones)):
        freq, duration = tones[i][0], tones[i][1]
        list_of_waveforms.append(waveform_generator(freq, duration, fs))


    for waveform in list_of_waveforms:
        sd.play(waveform)
        sd.wait()

if __name__ == "__main__":
    main()
