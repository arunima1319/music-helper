from constants import MusicType 

def music_type(music_string):
    if music_string[0] == "(":
        return MusicType.CHORD
    else:
        return MusicType.MELODY
    

