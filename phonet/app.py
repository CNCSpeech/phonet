import os
import pandas as pd
from phonet import Phonet

def main(file_name):

    # create a path to a temporary file
    tmp_file = os.path.join(os.getcwd(), "tmp.csv")
    phon=Phonet(['vocalic', 'consonantal', 'back', 'anterior', 'open', 'close', 'nasal', 'stop', 
                 'target_vowels', 'target_plosives', 'non_target_plosives', 'continuant', 'lateral', 
                 'flap', 'trill', 'voice', 'strident', 'labial', 'dental', 'velar', 'pause'])
    phon.get_phon_wav(file_name, tmp_file)

    data = pd.read_csv(tmp_file)
    os.remove(tmp_file)
    return data

# example usage
if __name__=="__main__":
    cwd = os.getcwd()
    audio_path = os.path.join(cwd, "phonet", "audios", "control_pataka_fondecyt.wav")
    result_path = os.path.join(cwd, "phonet", "audios", "pataka.csv")
    print(main(audio_path))
