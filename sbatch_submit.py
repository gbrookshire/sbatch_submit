#!/usr/bin/env python

"""
Submit a batch job to SLURM on BlueBear.
"""

import os
import subprocess
import tempfile
import argparse

def main():
    # Read in the template file
    lib_dir = os.path.dirname(os.path.realpath(__file__))
    with open(lib_dir + '/sbatch_template.sh') as f:
        template = f.readlines()
    template = ''.join(template)

    args = [['n', 'ntasks', 'Number of tasks', 1, {}],
            ['t', 'time', 'Maximum time to let the job run', '5:0:0', {}],
            ['m', 'mem', 'Memory allocation', '10G', {}],
            ['q', 'qos', 'Select a QOS on BlueBear', 'bbdefault',
             {'choices': ['bbdefault', 'bbfast']}],
            ['i', 'input', 'Script to run as a Slurm job', None,
             {'required': True}]]

    # Make the arg parser
    desc = 'Submit Matlab scripts as Slurm jobs'
    parser = argparse.ArgumentParser(description=desc)
    for arg in args:
        parser.add_argument('-' + arg[0],
                            '--' + arg[1],
                            help=arg[2],
                            default=arg[3],
                            **arg[4])
    args = parser.parse_args()

    # Replace the parameters in the sbatch script
    for arg in ['ntasks', 'time', 'mem', 'qos', 'input']:
        template = template.replace('_' + arg, str(getattr(args, arg)))

    # Write a temporary sbatch script
    tf = tempfile.NamedTemporaryFile()
    tf.writelines(template)

    # Run the job
    p = subprocess.call('sbatch ' + temp_filename, shell=True)


if __name__ == "__main__":
    main()
