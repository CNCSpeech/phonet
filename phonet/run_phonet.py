# -*- coding: utf-8 -*-
"""
Created on Feb 28 2019
@author: J. C. Vasquez-Correa
        Pattern recognition Lab, University of Erlangen-Nuremberg
        Faculty of Engineering, University of Antioquia,
        juan.vasquez@fau.de
"""

from phonet import Phonet
import os

if __name__=="__main__":

    PATH=os.path.dirname(os.path.abspath(__file__))

    path_audios=os.path.join(PATH, "fondecyt_pataka/PD_VAD/")
    
    path_results=os.path.join(PATH, "fondecyt_pataka_results/PD_VAD/")

    if not os.path.exists(path_results):
        os.makedirs(path_results)

    # file_audio=PATH+"/audios/pataka.wav"
    # file_feat=path_results+"/pataka"
    # phon=Phonet(["target_plosives", "non_target_plosives", "target_vowels", "vocalic"])
    # phon.get_phon_wav(file_audio, file_feat, True)

    # get phonological posteriors from de audio files included in a directory
    phon=Phonet(["target_plosives", "non_target_plosives", "target_vowels", "vocalic"])
    phon.get_phon_path(path_audios, path_results, plot_flag = False)

    # compute the posteriorgram for an audio_file for different phonological posteriors
    # phon=Phonet(["target_plosives", "non_target_plosives", "target_vowels", "vocalic"])
    # phon.get_posteriorgram(file_audio)