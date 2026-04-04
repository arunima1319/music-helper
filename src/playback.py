from music_type import music_type, file_music_type
from read_update_files import read_latest_file_used
from file_to_string import file_to_string
from record_music_attempt import record_music_attempt
from constants import *
from string_to_chords_list import string_to_chords_list
from string_to_notes_list import string_to_notes_list
from parse_inputs import check_file_validity


def playback(track, bpm, set_repeat):

    if set_repeat == "Y":
        i = 0
        while i < len(track):
            track[i].play(bpm)
            if i == len(track) - 1:
                i = 0
            else:
                i += 1

    elif set_repeat == "N":
        for music in track:
            music.play(bpm)
        print("Track completed, press Enter")


def source_to_playable_string(source):
    # Convert each source to a playable string

    # checks if input resembles a valid file or refers to last used file
    if check_file_validity(source) or source == "f":
        music_source = PlayType.FILE
        path = file_music_type(read_latest_file_used())[1]
        playable = file_to_string(path)

    else:
        music_source = PlayType.CLI
        playable = source
        print(music_source)

    return music_source, playable


def playable_string_to_track(playable_string):
    if music_type(playable_string) == MusicType.MELODY:
        track = string_to_notes_list(playable_string)
    if music_type(playable_string) == MusicType.CHORD:
        track = string_to_chords_list(playable_string)

    return track
