import os

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

   