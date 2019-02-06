#!/bin/bash
#SBATCH --ntasks _ntasks
#SBATCH --time _time
#SBATCH --mem _mem
#SBATCH --qos _qos
#SBATCH --error=slurm-%j.err

#### This template is filled in by sbatch_submit.py

set -e

module purge; module load bluebear
module load apps/matlab/r2017a

# # Set up scratch space
# BB_WORKDIR=$(mktemp -d /scratch/${USER}_${SLURM_JOBID}.XXXXXX)
# export TMPDIR=${BB_WORKDIR}

matlab -nodisplay -r _input

# # Copy your files back to the current directory
# test -d ${BB_WORKDIR} && /bin/cp -r ${BB_WORKDIR} ./

# # Delete the temporary files
# test -d ${BB_WORKDIR} && /bin/rm -rf ${BB_WORKDIR}
