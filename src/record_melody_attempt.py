
import os 

"""
Records the latest melody tried at the top of a file "record.txt"
Keeps a record of only the last 20 melodies tried 
If user is happy with their try and want to note it down in the final file,
They can "confirm" the latest entry to that file
"""

def record_melody_attempt(music_tried): 


    if os.path.exists("record.txt"):
        with open ("record.txt", "r") as f:
            text = f.read()
            lines = text.split()
            if len(lines) > 19:
                text = ("\n").join(lines[0:19])
                
    else: 
        text = ""

    with open ("record.txt", "w") as f:
        new_text = music_tried + "\n" + text
        f.write(new_text) 
    
