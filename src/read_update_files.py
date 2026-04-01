def update_latest_file_used(arg):
    with open ("latest_file_used.txt", "w") as f:
        f.write(arg)


def read_latest_file_used():
    with open("latest_file_used.txt", "r") as f:
        file = f.read()
    return file 

def update_bpm(arg): 
    bpm = arg[6:]
    with open ("bpm.txt", "w") as f:
        f.write(bpm)

def read_bpm(): 
    with open ("bpm.txt", "r") as f:
        return (int(f.read()))
