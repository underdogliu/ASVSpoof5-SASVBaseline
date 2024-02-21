#!/bin/bash

set -e
. ./path.sh

stage=0

team_id=team_gongcheng-1

. ./utils/parse_options.sh

wavdir=/home/smg2/share/joint-projects/ASVspoof5/phase2/data
bonafide_wavdir=$wavdir/bonafide
spoof_wavdir=$wavdir/spoof/$team_id

src_protocol_dir=/home/smg/xuecliu/asvspoof5-asv-baselines/data/protocols_phase2_v1
protocol_dir=data/protocols_phase2_sasv_v1

if [ $stage -le -10 ]; then
    python3 asvspoof5_phase2/prepare_evaluation_list.py \
        $spoof_wavdir \
        $src_protocol_dir \
        $protocol_dir
fi

if [ $stage -le 0 ]; then
    CUDA_VISIBLE_DEVICES=0 python trainSASVNet.py \
        --eval \
        --eval_frames 0 \
        --num_eval 1 \
        --eval_list $protocol_dir/p2_eval_asv_gi.trl \
        --enroll_path $bonafide_wavdir/flac \
        --eval_path $spoof_wavdir/flac \
        --model SKA_TDNN \
        --initial_model ./models/ckpts/ska_tdnn.model
fi