from note import Note
from chord import Chord
from constants import *


def string_to_chords_list(chord_string): 
    
    chords = []

    i = 0
    j = 0
    while i < len(chord_string):
    
        if chord_string[i] == "(":
            
            chord = Chord() 
            j = i+1
    
            while(len(chord_string) > j and chord_string[j] != ")"):
                j += 1
            chord_notes = chord_string[i+1:j]

            list_of_pitches= [chord.note1.pitch, chord.note2.pitch, chord.note3.pitch]
            list_of_octaves = [chord.note1.octave, chord.note2.octave, chord.note3.octave]

            p = 0
            note_number = 0
            while p < len(chord_notes):
                index_of_note = p
                if chord_notes[p] not in notes_dict:
                    raise Exception ("invalid chord string")
                else:
                    if len(chord_notes) > p+1 and chord_notes[p+1] == "#":
                        list_of_pitches[note_number] = chord_notes[index_of_note: index_of_note + 2]
                        p+=2
                    else:
                        list_of_pitches[note_number] = chord_notes[index_of_note]
                        p +=1 
                    

                if len(chord_notes) > p and  (chord_notes[p] == "h" or chord_notes[p] == "l"):
                    if chord_notes[p] == "h":
                        while len(chord_notes) > p and chord_notes[p] == "h":
                            list_of_octaves[note_number] += 1
                            p+=1
                    elif chord_notes[p] == "l":
                        while len(chord_notes) > p and chord_notes[p] == "l":
                            list_of_octaves[note_number] -= 1
                            p+=1
                    
                note_number += 1 


            (chord.note1 , chord.note2, chord.note3 ) = (
                Note(list_of_pitches[0], list_of_octaves[0]), 
                Note(list_of_pitches[1], list_of_octaves[1]),
                Note(list_of_pitches[2], list_of_octaves[2])
            )

            j+=1
            units = 1
            while len(chord_string) > j and chord_string[j] != "(":
                if chord_string[i+j] != "-":
                    raise Exception("Invalid chord string. Ensure all notes are within parentheses.")
                units += 1
                j+=1
            

            chord.length = units*0.25
           
            chords.append(chord)

        else: 
            raise Exception("Invalid chord string. Does your string not start with a '('?")
            

        i = j
          
            
        

    return chords
                    
                

