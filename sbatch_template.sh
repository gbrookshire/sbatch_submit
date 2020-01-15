#!/bin/bash
#SBATCH --ntasks _ntasks
#SBATCH --time _time
#SBATCH --mem _mem
#SBATCH --qos _qos
#SBATCH --error=slurm-%j.err

##################################################
# This template is filled in by sbatch_submit.py #
##################################################

set -e

module purge; module load bluebear
_setup
_input

