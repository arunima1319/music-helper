import os

def file_to_string(file):
    filepath = os.path.join("melodies", file) 

    if os.path.exists(filepath): 
        with open (filepath) as f: 
            text = f.read()
    else: 
        raise Exception("No such file")
    
    text = text.strip()

    music_string = ""

    lines = text.split("\n")

    for line in lines:
        line = line.strip()
        music_string += line
            
            
    return music_string

