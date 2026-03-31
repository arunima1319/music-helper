import os
from transpose import transpose 

def file_edit(command, file):

    file_path = os.path.join("melodies", file)

    
    
    match(command):
        case("confirm"):
            with open ("record.txt", "r") as f:
                entry = f.read()
                lines = entry.split("\n")
            to_enter = lines[0] + "\n"
            with open(file_path, "a") as f:
                f.write(to_enter)

        case("undo"):
            with open(file_path, "r") as f:
                text = f.read()
            lines = text.split("\n")
            with open (file_path, "w") as f:
                new_text = ("\n").join(lines[:-1])
                f.write(new_text)

        case("delete"):
            with open (file_path, "w") as f:
                f.write("")



    if command[0:9] == "transpose": 
        semitones = int(command[9:])
        with open (file_path, "r") as f: 
            text = f.read()
        lines = text.split("\n")
        new_lines = []
        for line in lines:
            new_line = transpose(line, semitones)
            new_lines.append(new_line)
        new_text = "\n".join(new_lines)
        new_file_name = file.split(".")[0] + "_" + command[9:] + ".txt"
        new_file_path = os.path.join("melodies", new_file_name)
        with open(new_file_path, "w") as f:
            f.write(new_text)