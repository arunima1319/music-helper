import os
from transpose import transpose 
from constants import MusicType
from music_type import music_type 

def confirm_file(file_path, music_type_of_file):
    with open ("record.txt", "r") as f:
        record = f.read()
    lines = record.split("\n")
    latest_entry = lines[0].strip()

    if music_type(latest_entry) != music_type_of_file:
        raise Exception("You cannot add chords to a melody file or vice versa.")

    print("1 - alright till here")
    if not os.path.exists(file_path):
        try:
            dir_name = "/".join(file_path.split("/")[:-1])
            os.makedirs(dir_name)
            print(f"This is your first {music_type_of_file.value} file! You should see a new {dir_name} folder in your music helper.")
        except:
            print("Thanks for adding a new Chord file!")

        with open(file_path, "w") as f:
            f.write(latest_entry)


        

    else:
        with open(file_path, "r") as f: 
            original_contents = f.read()
        original_lines = [line for line in original_contents.split("\n") if line]
        original_lines.append(latest_entry)
        
        new_content = ("\n").join(original_lines)
        with open(file_path, "w") as f:
            f.write(new_content)

        



def undo_file(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    lines = text.split("\n")
    with open (file_path, "w") as f:
        new_text = ("\n").join(lines[:-1])
        f.write(new_text) 

def delete_file(file_path):
    with open (file_path, "w") as f:
        f.write("")


def create_singing_practice_file(file_path, filename):
    with open (file_path, "r") as f:
        melody = f.read()
    melody_lines = [melody for melody in melody.split("\n") if melody]
    new_melody_lines = []
    for i in range (-12, 12, 1):
        for melody_line in melody_lines: 
            new_melody_line = transpose(melody_line, i)
            new_melody_lines.append(new_melody_line)

    new_contents = ("\n").join(new_melody_lines)

    new_filename = "sing" + "_" + filename.split(".")[0] + ".melody"
    new_file_path = os.path.join("melodies", "sing", new_filename)

        
    try:
        os.makedirs("melodies/sing")
        print("You just created your first singing practice file! You should see a new 'sing' folder within 'melodies' ") 
    except Exception:
        print("Thanks for adding a new singing practice file!")

    with open(new_file_path, "w") as f:
        f.write(new_contents)
    

def transpose_file(command, file_path, filename):
    semitones = int(command[9:])
    with open (file_path, "r") as f: 
            text = f.read()
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        new_line = transpose(line, semitones)
        new_lines.append(new_line)
    new_text = "\n".join(new_lines)
    new_file_name = filename.split(".")[0] + "_" + command[9:] + ".melody"
    new_file_path = os.path.join("melodies", new_file_name)
    with open(new_file_path, "w") as f:
        f.write(new_text)



def file_edit(command, file):      #We have ensured its a valid melody or chord file

    if file.split(".")[1] == "chord":
        music_type_of_file = MusicType.CHORD
        file_path = os.path.join("chords", file) 


    if file.split(".")[1] == "melody":
        music_type_of_file = MusicType.MELODY
        file_path = os.path.join("melodies", file)

    if command == "confirm": 
        confirm_file(file_path, music_type_of_file)
            

    elif command == "undo":
        undo_file(file_path)


    elif command == "delete":
        delete_file(file_path)
            

    elif command == "singing":
        if music_type_of_file == MusicType.CHORD:
            raise Exception("you cannot create scale exercises from a chord progression")
        create_singing_practice_file(file_path, file)    

    elif command[0:9] == "transpose": 
        transpose_file(command, file_path, file)

    else:
        raise Exception("invalid command")