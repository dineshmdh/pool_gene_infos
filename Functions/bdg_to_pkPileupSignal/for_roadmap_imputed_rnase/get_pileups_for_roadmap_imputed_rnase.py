# Created on November 18, 2017

import os
rank = os.environ["SLURM_ARRAY_TASK_ID"]

pkFiles_list = "list_of_bedFiles_for_RNaseq_pileup.txt"  # in the same directory as this script 
bdgDir = "/data/gordanlab/dinesh/predicting_gex/Input_files/roadmap/RNase_signal/imputed/bedgraph"
outputDir = "/data/gordanlab/dinesh/predicting_gex/Output/roadmap_signal/rnase_imputed"

bdg_file = os.path.join(bdgDir, sorted(os.listdir(bdgDir))[int(rank)-1])
cmd = "python ~/bin/pileup_forManyPkFiles_usingOneBdgFile.py -c useWholePk -z ~/bin/hg19.chromSizes.txt -f 0 -p {} -b {} -o {}".format(pkFiles_list, bdg_file, outputDir)
os.system(cmd)
