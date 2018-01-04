# Created on Nov 15, 2017

import os
import re

rank = os.environ["SLURM_ARRAY_TASK_ID"]
baseDir = "/data/gordanlab/dinesh/predicting_gex/Input_files/roadmap/DNase_signal/imputed"
inputDir = os.path.join(baseDir, "bigwig")
outputDir = os.path.join(baseDir, "bedgraph")

bw_files = [x for x in os.listdir(inputDir) if x.__contains__(".bigwig")]
bw_inFile = bw_files[int(rank)-1]
bdg_outFile = ".".join(re.split("\.", bw_inFile)[:-1])+".bdg"
cmd = "bigWigToBedGraph {} {}".format(os.path.join(inputDir, bw_inFile), os.path.join(outputDir, bdg_outFile))
os.system(cmd)