
from file_to_string import file_to_string
from constants import *
from file_edit import file_edit
from read_update_files import *
from record_music_attempt import record_music_attempt
from music_type import music_type, file_music_type



#A module to parse inputs and execute the required functions
#Ensures smoother user experience


def check_file_validity(arg):
    full_file_inputted = False

    if "." in arg:
        ext = arg.split(".")[1]
        full_file_inputted = True

            
    if full_file_inputted:
        if ext == "melody" or ext == "chord":
            if len(arg.split(".")) > 2:
                raise Exception("This is an invalid extension.")
            update_latest_file_used(arg)
        else: 
            raise Exception ("You tried to enter a file but this is not a melody or chord file")

  
    return full_file_inputted


def parse_inputs(input_array):
        

        #Handles the special merge command
        #if len(input_array) >= 2 and input_array[1] == "merge":



        if len(input_array) == 2:   #just a single track is being played or bpm/repeat is being set
            
            arg = input_array[1]
            
            if arg[0:6] == "setbpm":
                update_bpm(arg)
                return None, None
            
            elif arg[0:6] == "repeat":
                update_repeat(arg[6])
                return None, None
                
            #checks if input resembles a valid file or refers to last used file
            elif check_file_validity(arg) or arg == "f":
                music_source = PlayType.FILE
                music_type, path = file_music_type(read_latest_file_used())
                playable = file_to_string(path)

            else:
                music_source = PlayType.CLI
                playable = arg
                record_music_attempt(playable)
    
            print(music_source)
            return music_source, playable
            
        
        elif len(input_array) == 3:

            command, file = input_array[1], input_array[2]

            if check_file_validity(file):
                pass
            elif file == "f":
                pass
            else:
                print(invalid_argument_text)
            
            file = read_latest_file_used()
            
            file_edit(command, file) #file_edit manages the paths on its own

            #will be a different file in case of singing and transpose commands
            music_type, path = file_music_type(read_latest_file_used())
            playable = file_to_string(path)

            return PlayType.FILE, playable

        else:
            print(invalid_argument_text)
            return None, None
    
