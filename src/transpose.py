from note import Note
from string_to_notes_list import string_to_notes_list
from string_to_chords_list import string_to_chords_list


def transpose_melody(music_string, semitones):
    notes = string_to_notes_list(music_string)
    new_notes = []
    for note in notes:
        new_note = note.transpose(semitones)
        new_notes.append(new_note)

    new_string = ""
    for new_note in new_notes:
        new_string += new_note.note_to_notation_string()

    return new_string


def transpose_chord(music_string, semitones):
    chords = string_to_chords_list(music_string)
    new_chords = []

    for chord in chords:
        new_chord = chord.transpose(semitones)
        new_chords.append(new_chord)

    new_string = ""
    for new_chord in new_chords:
        new_string += new_chord.chord_to_notation_string()

    return new_string
