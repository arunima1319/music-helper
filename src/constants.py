from enum import Enum 

class PlayType(Enum):
    CLI = "cli_string"
    FILE = "textfile"


twelfth_root_of_two = 1.059463

invalid_argument_text = """


Invalid argument.
To play a melody, please enter the name of a single melody file or a single melody string.
For example: 
"uv run src/main.py happy_birthday.txt"
OR
uv run src/main.py EEF#-E-A-G#---
          
To update a melody file, please enter your command followed by the file.
For example: 
"uv run src/main.py confirm happy_birthday.txt"

"""

notes_dict = {
        "C": 1,
        "C#" : 2,
        "D": 3,
        "D#": 4,
        "E": 5,
        "F" : 6,
        "F#" : 7, 
        "G" : 8, 
        "G#": 9, 
        "A": 10,
        "A#": 11,
        "B" : 12

}

middle_C_freq = 261.3

