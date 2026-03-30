import os

def file_edit(command, file):

    file_path = os.path.join("melodies", file)

    
    
    match(command):
        case("confirm"):
            with open ("record.txt", "r") as f:
                entry = f.read()
                lines = entry.split("\n")
            with open(file_path, "a") as f:
                f.write(lines[0])

        case("delete"):
            with open (file_path, "w") as f:
                f.write("")

   