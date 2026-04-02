# Music Helper 

Music Helper is a tool to quickly play, store, and transpose music (chords and melodies) from the terminal. Great for songwriters, singers, and musicians, especially when access to a musical instrument is limited!


## Installation 

### 1. Prerequisites 

This project requires:
- Python3   [install](https://www.python.org/downloads/)
- Numpy [install](https://numpy.org/install/)
- Sounddevice [install](https://pypi.org/project/sounddevice/)

To run this project using uv (recommended) follow these steps:

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

2. Clone the github repository and navigate to the root of the project 
```
git clone https://github.com/arunima1319/music-helper
cd musichelper
```
3. Install dependencies 

```
uv sync
```


## Usage 

### Format for entering music
Enter notes in the form of a string, no spaces. Possible notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B. 

To indicate that the note must be played at a higher or lower octave, add an 'h' or an 'l' for every octave you want to go higher or lower (from the middle octave) respectively. Example: ```Chh```, ```Bl```, etc. 

The relative length of the note can be coded using '-'. Example: ```F#l---``` will play for 4 beats, while `F#l` will play for only one. You cannot start a string with a '-'. 

Example melody: ```C-E-G-Ch-G-E-C------``` 

To play chords, enclose the notes (exactly 3) in parentheses, and enter the duration of the entire chord as explained above. 

Example chord progression: ```(CEG)-------(DFA)-------(AlCE)---------------```

An input string or file can either be a harmony(chords) or melody string/file. 

### Playing music 

For ease of use, set an alias for ```python3 src/main.py``` in the root of the repository as follows:

``` alias music="python3 src/main.py"```

To play music from an input string, run:

```music <input string>```

Example: ```music C-E-G-Ch-G-E-C--------```

This should play the melody. 

For chords, you may have to enclose the string in quotes to avoid misinterpretations of the `(` character. 

Exampel: ```music (CEG)------(DFA)------```

You can also play music from files. Melody files have a .melody extension, and harmony(chord) files have a .chord extension. Melody files are stored in musichelper/melodies and chord files are in musichelper/chords. You do not need to worry about the directory structure, just enter the name of the file you want to play. 

Examples: ```music april.chord``` or 

```music amazing_grace.melody```

If there are no melody/chord files, you can easily create one by using the command ```confirm``` which will create a new file (or update an existing one) with the most recent music string you have played in the shell. Read more in the [Commands](Commands) section below

### Merge

You can play multiple (any number of) files or input strings at the same time using the merge command. 

```music merge april.chord amazing_grace.melody E------ Chh------``` 

This can be useful to check how different chord progressions sound with a certain melody, or how counter melodies sound together, etc. 



### Commands 

These are some commands to update or create file. The new or updated file will play automatically after these commands are run.

1. confirm


Add the latest played music input string to the file you enter (it must be a .chord or .melody file). If the latest string is a chord string and you try to add it to a melody file (or vice versa), you will receive a prompt telling you that you cannot.
```
music confirm amazing_grace.melody
```
2. undo

Undo the latest addition to a file 

```
music undo amazing_grace.melody
```

3. delete


Clear the contents of the file, but not remove the file itself

```
music delete amazing_grace.melody 
```

4. read

Print the contents of the file to a terminal

```
music read april.chord
```

5. transpose

Transpose the melody/harmony up or down a certain number of semitones. It creates a new file with the new notation strings, example: ```amazing_grace_-2.melody``` , ```april_5.chord```. 

```
#transposes it DOWN two semitones
music transpose-2 amazing_grace.melody

#transposes it UP five semitones
music transpose5 april_5.chord
```

2. singing

Make scale exercises out of a melody file
It will create a file called ```sing_<melody name>.melody```.  It can only be used on melody files.
Very useful for singing practice! 

```
#creates file sing_high_and_low.melody

music singing high_and_low_.melody
```

### Setting BPM, looping tracks, and using shortcuts for filename

To set BPM:
``` music setbpm120 ``` ,  ```music setbpm90``` , etc. 

You can loop tracks (forever) by setting: 
```music repeatY``` (to loop) OR ```music repeatN``` (to play once)

To exit a loop, or interrupt and stop the music, press 'q' - you will be prompted for this. After a track has finished playing on its own, press enter (or any key) once to be able to run your next command.

To avoid having to write the file name repeatedly, you can use the character `f` as an alias for the latest used file. This alias is valid in all cases, and will work as long as the file it points to exists. Enter the full file name first and use 'f' for subsequent uses until you play or update a different file. 

You can see the latest used file in the file ```latest_file_used.txt```  You can see the current BPM in ```bpm.txt```, and whether repeat is on or off in ```repeat.txt```. 





