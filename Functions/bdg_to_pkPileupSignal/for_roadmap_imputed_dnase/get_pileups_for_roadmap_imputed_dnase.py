# Created on November 18, 2017

import os
rank = os.environ["SLURM_ARRAY_TASK_ID"]

pkFiles_list = "/data/gordanlab/dinesh/predicting_gex/Functions/bdg_to_pkPileupSignal/list_of_DHS_pkFiles_for_DNase_pileup.txt"  # in the same directory as this script
bdgDir = "/data/gordanlab/dinesh/predicting_gex/Input_files/roadmap/DNase_signal/imputed/bedgraph"
outputDir = "/data/gordanlab/dinesh/predicting_gex/Output/roadmap_signal/dnase_imputed"

bdg_file = os.path.join(bdgDir, sorted(os.listdir(bdgDir))[int(rank)-1])
cmd = "python ~/bin/pileup_forManyPkFiles_usingOneBdgFile.py -c useWholePk -z ~/bin/hg19.chromSizes.txt -f 0 -p {} -b {} -o {}".format(pkFiles_list, bdg_file, outputDir)
os.system(cmd)
