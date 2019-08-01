# sbatch_submit
Helper script to submit Slurm jobs on Bluebear

## Important
Change the variable `matlab_startup` in `sbatch_submit.py` to point to your `startup.m` file.

## Example
```
sbatch_submit.py "my_analysis_func(1, 'some_arg')" -t 5:0 -m 20G
```

## Options
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
