import numpy 
from constants import *
from note import Note

def string_to_notes_list(music_text): 
    music_text.strip()
    notes_list = []
    i = 0
    

    while (i < len(music_text)):  #String must start with a note, not a - 
        index_of_note = i
        if music_text[i] in notes_dict:
            octave = 0 #By default, we assume the note is middle C
            
            if len(music_text) > i+1 and music_text[i+1] == "#":
               
                
                h = 1
                while(len(music_text) > i + h + 1 and music_text[i+h+1] == "h"):
                    octave += 1
                    h+=1
                i += h-1
                

                l = 1
                while(len(music_text) > i + l + 1 and music_text[i+l+1] == "l"):
                    octave -= 1
                    l += 1
                i += l-1 
                
                
                j = 1

                while(len(music_text) > i + j + 1 and music_text[i + 1 + j]== "-"):
                    j += 1
                
                length = j*0.25
                i += j+1

                note = Note(music_text[index_of_note: index_of_note +2], octave, length)
                notes_list.append(note)
                
               

            else:
                
                
                h = 1
                while(len(music_text) > i + h and music_text[i+h] == "h"):
                    octave += 1
                    h+=1 
                i+= h-1

                l = 1
                while(len(music_text) > i + l and music_text[i+l] == "l"):
                    octave -= 1
                    l += 1
                i += l-1
                
            
                
                j = 1
                while(len(music_text) > i + j and music_text[i+ j]== "-"):
                    j += 1
                
        
                length = j*0.25
                i += j

                note = Note(music_text[index_of_note], octave, length)
                notes_list.append(note)
                
                
              
        else: 
            raise Exception ("Invalid music text.\n")
        

            
    return notes_list
        
            
            
