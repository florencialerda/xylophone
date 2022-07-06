from xylophone.client import XyloClient
from xylophone.xylo import XyloNote

def read_score(filename):
    """
    Receives a partiture and selects the notes that the metalophone can support. Then, creates a list in which it creates an object
    of the class Xylonote, where the parameters are the selected notes.
    Parameters
    -------
      filename : str

    Returns
    -------
      notes : list
    """
    with open(filename, 'r') as f:
        lines= f.readlines()
        ultra_info=[]
        for line in lines:
          info=line.split()
          supported_notes = ["C7", "B6", "A6", "G6", "F6", "E6", "D6", "C6", "B5", "A5", "G5", "F5", "E5", "D5", "C5", "B4", "A4", "G4", "C#7", "A#6", "G#6", "F#6", "D#6", "C#6", "A#5", "D#5", "C#5", "A#4", "G#4", "Cb7", "Bb6", "Ab6", "Gb6", "Eb6", "Db6", "Bb5", "Ab5", "Eb5", "Db5", "Bb4", "Ab4"]
          if info[1] in supported_notes:
              ultra_info.append((info[1], float(info[0])))
    notes=[]
    for xilo_note in ultra_info:
        xilo_object = XyloNote(xilo_note[0], xilo_note[1], 90)
        notes.append(xilo_object)
    return notes

def read_xylophone(dispositivo:str):
    """
    Receives an IP and creates a variable with it.

    Parameters
    -------
      dispositivo : str
      
    Returns 
    -------
      dispositivo : str
    """
    return dispositivo

notes=read_score(filename)
host=read_xylophone(dispositivo)

client = XyloClient(host, port=8080)
client.load(notes)
client.play()

