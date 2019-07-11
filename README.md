# sbatch_submit
Helper script to submit jobs on Slurm


```
usage: sbatch_submit.py [-h] (-i INPUT | -f FILE) [-n NTASKS] [-t TIME]
                        [-m MEM] [-q {bbdefault,bbshort}]

Submit Matlab code or script as a Slurm job

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Matlab code to run (use -i or -f but not both!)
  -f FILE, --file FILE  Path to Matlab file to run
  -n NTASKS, --ntasks NTASKS
                        Number of tasks
  -t TIME, --time TIME  Maximum time to let the job run
  -m MEM, --mem MEM     Memory allocation
  -q {bbdefault,bbshort}, --qos {bbdefault,bbshort}
                        Select a QOS on BlueBear 
```
