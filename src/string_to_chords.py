from note import Note
from chord import Chord
from string_to_notes_list


def string_to_chords(chord_string): 
    
    for i in range(len(chord_string)):
        if chord_string[i] == "(":
            j = 1
            while(chord_string[i+j] != ")"): 
                j += 1
            chord_string = 
            