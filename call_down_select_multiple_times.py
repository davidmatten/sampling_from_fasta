#!/usr/local/bin/python3
from os.path import basename
import argparse
import os
from down_selection import main as dsm


def main(infile, outfile, select_size, repeats):
    fn_path = os.path.split(outfile)[0]
    base_fn = basename(outfile)
    extension = base_fn.split(".")[-1]

    for i in range(repeats):
        built_out_fn = os.path.join(fn_path, base_fn + "_" + str(i) + "_" + extension)
        dsm(infile, built_out_fn, select_size)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calls the down select python script, for a given number of repeats.')
    parser.add_argument('-in', '--infile', type=str, help='The input .fasta file.', required=True)
    parser.add_argument('-out', '--outfile', type=str, help='The pattern to name the output .fasta files. '
                                                            'This can have a path. '
                                                            'If this path is specified and the working direcotry is not'
                                                            ' specified, then then output will be written here. If '
                                                            'this path is specified, and the working directory is '
                                                            'specified then only the file name from this will be used, '
                                                            'and written to the working directory.', required=True)
    parser.add_argument('-sample', '--sample', type=int,
                        help='The size of the sample you want to down select to. If this number if larger than the '
                             'number of sequences in your input file, then all the sequences in your input file will '
                             'be used.', required=True)
    parser.add_argument('-wd', '--working_directory', type=str, help='The directory to write the output to. This has '
                                                                     'a careful interplay with the outfile path/name.',
                        default=None, required=False)

    parser.add_argument('-repeats', '--repeats', type=int,
                        help='The number of times you wish to repeat sampling.', required=True)

    args = parser.parse_args()

    infile = args.infile
    infile = os.path.abspath(infile)

    outfile = args.outfile
    wd = args.working_directory
    # outfile can have a path, or not have a path.
    # If it has a path, we want to keep it as it is.
    # if it doesn't have a path, we want the output file name, to append to the wd, and output there.
    # if wd is None, we use the input file path.
    if not wd:
        wd = os.path.split(infile)[0]
    if os.path.split(outfile)[0] == '':
        outfile = os.path.join(wd, outfile)

    select_size = args.sample

    repeats = args.repeats

    # sample_output_filename = "SVB039BP_1239.fasta"
    # source_filename = "SVB039BP_S39_L001_kept_removeGaps_remove_n.fasta"
    main(infile, outfile, select_size, repeats)
