#!/bin/bash
#SBATCH --nodes _nodes
#SBATCH --ntasks _ntasks
#SBATCH --cpus-per-task _cpus
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

