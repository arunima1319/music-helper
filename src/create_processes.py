
from read_update_files import read_bpm, read_repeat
from playback import playback, playable_string_to_track, source_to_playable_string
from record_music_attempt import record_music_attempt
from constants import *
import multiprocessing

def create_processes(sources): 

    processes = []
     

    for element in sources:

        source_type, playable = source_to_playable_string(element)

        if playable:

            bpm = read_bpm()
            set_repeat = read_repeat()
            track = playable_string_to_track(playable)

            if source_type == PlayType.CLI:
                record_music_attempt(playable)
            else:
                pass

            p = multiprocessing.Process(target = playback, args = (track, bpm, set_repeat))
            processes.append(p)

        
    return processes
