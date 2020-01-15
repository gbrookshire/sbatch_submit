# sbatch_submit
This script makes it easier to submit Slurm jobs on Bluebear.

## Setting up the environment and loading libraries
Set up the shell environment using the '--setup' argument.
E.g. `./path/to/setup_script.sh`.

## Examples
Make sure to preserve all quotes!
Anything inside triangle brackets `<...>` is code that should be replaced with your specific calls.

### Matlab
```
matlab_load='module load apps/matlab/r2017a'
matlab_startup='run <PATH/TO/startup.m>' # Your Matlab startup script
matlab_call="matlab -nodisplay -r \"$matlab_startup, run tests/test.m, quit\" "
./sbatch_submit.py -i "$matlab_call" -s "$matlab_load" -t 5:0 -m 10G
```

Replace `run tests/test.m` with the code you want to run.

### Python
```
python_load='source <PATH/TO/load_python.sh>'
python_call='python tests/test.py'
./sbatch_submit.py -i "$python_call" -s "$python_load" -t 5:0 -m 10G
```

Replace `tests/test.py` with the script you want to run.


## Options
```
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Shell command to run
  -s SETUP, --setup SETUP
                        Shell command to set up the environment
  -n NTASKS, --ntasks NTASKS
                        Number of tasks
  -t TIME, --time TIME  Maximum time to let the job run
  -m MEM, --mem MEM     Memory allocation
  -q {bbdefault,bbshort}, --qos {bbdefault,bbshort}
                        Select a QOS on BlueBear

```
