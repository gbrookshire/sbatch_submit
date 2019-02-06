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

    # Make the arg parser
    desc = 'Submit Matlab code or script as a Slurm job'
    parser = argparse.ArgumentParser(description=desc)

    # Arg specs: Short name, long name, description, default, other args
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--input', help='Code to run on Slurm')
    group.add_argument('-f', '--file', help='Name of file to run on Slurm')

    args = [['n', 'ntasks', 'Number of tasks', 1, {}],
            ['t', 'time', 'Maximum time to let the job run', '5:0:0', {}],
            ['m', 'mem', 'Memory allocation', '10G', {}],
            ['q', 'qos', 'Select a QOS on BlueBear', 'bbdefault',
             {'choices': ['bbdefault', 'bbfast']}]]
    for arg in args:
        parser.add_argument('-' + arg[0],
                            '--' + arg[1],
                            help=arg[2],
                            default=arg[3],
                            **arg[4])
    args = parser.parse_args()

    # Replace the Slurm parameters in the sbatch script
    for arg in ['ntasks', 'time', 'mem', 'qos']:
        template = template.replace('_' + arg, str(getattr(args, arg)))

    # Invoke the code or script
    if args.input is not None:
        # This is specific to my startup script
        startup = 'run /rds/homes/b/brookshg/startup.m'
        msg = "'{}, {}, quit'".format(startup, args.input)
    elif args.file is not None:
        msg = '< {}'.format(args.file)
    template = template.replace('_input', msg)

    # Write a temporary sbatch script
    tf = tempfile.NamedTemporaryFile()
    tf.writelines(template)
    tf.flush()

    # Run the job
    p = subprocess.call('sbatch ' + tf.name, shell=True)


if __name__ == "__main__":
    main()
