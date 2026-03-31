from note import Note
from string_to_notes_list import string_to_notes_list

def transpose(music_string, semitones): 
    notes = string_to_notes_list(music_string)
    new_notes = []
    for note in notes:
        new_note = note.transpose(semitones)
        new_notes.append(new_note)

    new_string = ""
    for new_note in new_notes:
        new_string += new_note.note_to_notation_string()


    return new_string



