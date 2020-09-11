#!/bin/bash
#SBATCH --nodes _nodes
#SBATCH --ntasks _ntasks
#SBATCH --cpus-per-task _cpus
#SBATCH --time _time
#SBATCH --mem _mem
#SBATCH --qos _qos
#SBATCH --error _dir/slurm-%j.err
#SBATCH --output _dir/slurm-%j.out


##################################################
# This template is filled in by sbatch_submit.py #
##################################################

set -e

module purge; module load bluebear
_setup
_input

