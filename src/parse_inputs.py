
from file_to_string import file_to_string
from constants import *
from file_edit import file_edit
from read_update_files import *


#A module to parse inputs and execute the required functions
#Ensures smoother user experience

def parse_inputs(input_array):
        

        if len(input_array) == 2:   #just a melody is being played or bpm is being set
            
            arg = input_array[1]
            
            if arg[0:6] == "setbpm":
                update_bpm(arg)
                return None
                
            full_file_inputted = False
            if "." in arg:
                ext = arg.split(".")[1]
                full_file_inputted = True
                music_source = PlayType.FILE 

            
            if full_file_inputted:
                if ext == "melody" or ext == "chord":
                    update_latest_file_used(arg)
                else: 
                    print(music_source)
                    raise Exception ("This is not a melody or chord file")                
                                
            elif arg == "f":
                music_source = PlayType.FILE

            else:
                music_source = PlayType.CLI
    
            print(music_source)
            return music_source
            
        
        elif len(input_array) == 3:

            command, file = input_array[1], input_array[2]


            if "." in file:
                ext = file.split(".")[1]
                if ext =="melody" or ext == "chord":
                    if len(file.split(".")) > 2:
                        raise Exception("This is an invalid extension.")
                    update_latest_file_used(file)
                else: 
                    raise Exception ("This is not a melody or chord file")
            
            elif file == "f":
                pass
            else:
                print(invalid_argument_text )
            
            file = read_latest_file_used()
            
            file_edit(command, file)

            return None

        else:
            print(invalid_argument_text)
            return None
    
