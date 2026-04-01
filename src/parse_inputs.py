
from file_to_string import file_to_string
from constants import *
from record_melody_attempt import record_melody_attempt
from file_edit import file_edit

def update_latest_file_used(arg):
    with open ("latest_file_used.txt", "w") as f:
        f.write(arg)


def read_latest_file_used():
    with open("latest_file_used.txt", "r") as f:
        file = f.read()
    return file 

def update_bpm(arg): 
    bpm = arg[6:]
    with open ("bpm.txt", "w") as f:
        f.write(bpm)

def read_bpm(): 
    with open ("bpm.txt", "r") as f:
        return (int(f.read()))

def parse_inputs(input_array):
        

        if len(input_array) == 2:   #just a melody is being played or bpm is being set
            
            arg = input_array[1]
            
            if arg[0:6] == "setbpm":
                update_bpm(arg)
                return None, None
                
            if "." in arg:
                ext = arg.split(".")[1]

            if arg == "f" or ext == "melody" or ext == "chord":
                melody_source = PlayType.FILE

                if arg[-4:] == ".melody" or arg[-4:] == ".chord":
                    update_latest_file_used(arg)
                    
                file = read_latest_file_used()
                
                
                melody_string = file_to_string(file)
                
    
            else:
                melody_source = PlayType.CLI
                melody_string = arg
                
                

            print(melody_source)
            return melody_string, melody_source
            
        
        elif len(input_array) == 3:

            command, file = input_array[1], input_array[2]


            if "." in file:
                ext = file.split(".")[1]
                if ext =="melody" or ext == "chord":
                    update_latest_file_used(file)
            elif file == "f":
                pass
            else:
                print(invalid_argument_text )
            
            file = read_latest_file_used()
            
            file_edit(command, file)

            return None, None

        else:
            print(invalid_argument_text)
            return None, None
    
