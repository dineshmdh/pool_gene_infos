#!/bin/bash

## Created on Nov 18, 2017

#SBATCH -o python_%A_%a.out # Standard output
#SBATCH -e python_%A_%a.err # Standard error
#SBATCH --array=1-127
#SBATCH --mem=5G

python get_pileups_for_roadmap_imputed_dnase.py
