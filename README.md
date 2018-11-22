# sbatch_submit
Helper function to submit jobs on Slurm

```
usage: sbatch_submit.py [-h] [-n NTASKS] [-k NODES] [-t TIME] [-m MEM]
                        [-q {bbdefault,bbfast}] -i INPUT

Submit Matlab scripts as Slurm jobs

optional arguments:
  -h, --help            show this help message and exit
  -n NTASKS, --ntasks NTASKS
                        Number of tasks
  -k NODES, --nodes NODES
                        Number of nodes
  -t TIME, --time TIME  Maximum time to let the job run
  -m MEM, --mem MEM     Memory allocation
  -q {bbdefault,bbfast}, --qos {bbdefault,bbfast}
                        Select a QOS on BlueBear
  -i INPUT, --input INPUT
                        Script to run as a Slurm job
```
