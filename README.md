# sbatch_submit
Helper function to submit jobs on Slurm

```
usage: sbatch_submit.py [-h] (-i INPUT | -f FILE) [-n NTASKS] [-t TIME]
                        [-m MEM] [-q {bbdefault,bbfast}]

Submit Matlab code or scripts as a Slurm job

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Code to run on Slurm
  -f FILE, --file FILE  Name of file to run on Slurm
  -n NTASKS, --ntasks NTASKS
                        Number of tasks
  -t TIME, --time TIME  Maximum time to let the job run
  -m MEM, --mem MEM     Memory allocation
  -q {bbdefault,bbfast}, --qos {bbdefault,bbfast}
                        Select a QOS on BlueBear
```
