from constants import MusicType


def music_type(music_string):
    if music_string[0] == "(":
        return MusicType.CHORD
    else:
        return MusicType.MELODY


def file_music_type(music_file):

    if music_file.split(".")[1] == "melody":
        file_path = f"melodies/{music_file}"
        return MusicType.MELODY, file_path

    elif music_file.split(".")[1] == "chord":
        file_path = f"chords/{music_file}"
        return MusicType.CHORD, file_path

    else:
        return None, None
