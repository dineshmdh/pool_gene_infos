#!/bin/bash

## Created on Nov 15, 2017

#SBATCH -o python_%A_%a.out # Standard output
#SBATCH -e python_%A_%a.err # Standard error
#SBATCH --array=1-127
#SBATCH --mem=4G

python convert_bw_to_bdg_dnase_imputed.py
