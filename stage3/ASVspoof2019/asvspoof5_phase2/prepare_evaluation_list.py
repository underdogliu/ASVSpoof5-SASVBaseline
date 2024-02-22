"""
Prepare the evaluation list for stage3 model
from the ASVspoof-5 phase 1 participants.

This is for Phase 2 of the challenge, to check
whether the SASV can be opened as a separate
task and thus track, with solid package. 
"""
import os
import sys
from shutil import copyfile

import glob

if __name__ == "__main__":
    src_wav_folder = sys.argv[1]
    src_list_folder = sys.argv[2]
    
    tar_data_folder = sys.argv[3]
    os.makedirs(tar_data_folder, exist_ok=True)

    src_trn_list = src_list_folder + "/p2_eval_asv_gi.trn"
    src_trl_list = src_list_folder + "/p2_eval_asv_gi.trl"
    tar_trn_list = tar_data_folder + "/p2_eval_asv_gi.trn"
    tar_trl_list = tar_data_folder + "/p2_eval_asv_gi.trl"

    # copy the trn list    
    copyfile(src_trn_list, tar_trn_list)

    # write trl list
    with open(src_trl_list, "r") as s, open(tar_trl_list, "w") as t:
        for line in s:
            spk, utt, asv_decision, spoof_decision = line.split()
            t.write("{} {} {} {}\n".format(spk, utt, spoof_decision, asv_decision))

    # try to ensure the flac (wav) files are there
    flac_files = glob.glob(src_wav_folder + "/flac/*.flac")
    wav_files = glob.glob(src_wav_folder + "/flac/*.wav")
    assert (flac_files != [] or wav_files != []), "empty wav directory for {}".format(src_wav_folder)
