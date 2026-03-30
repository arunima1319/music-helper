import numpy 
from constants import *

def string_to_notes_list(music_text): 
    music_text.strip()
    notes_list = []
    i = 0
    

    while (i < len(music_text)):  #String must start with a note, not a - 
        if music_text[i] in notes_dict:
            if len(music_text) > i+1 and music_text[i+1] == "#": 
                j = 1
                while(len(music_text) > i + j + 1 and music_text[i + 1 + j]== "-"):
                    j += 1
                length = j*0.25
                notes_list.append((music_text[i:i+2], length))
                i += j+1
               

            else: 
                j = 1
                while(len(music_text) > i + j and music_text[i+ j]== "-"):
                    j += 1
                length = j*0.25
                notes_list.append((music_text[i], length))
                i += j
              
        else: 
            raise Exception ("invalid music text")
        

            
    return notes_list
        
            
            

