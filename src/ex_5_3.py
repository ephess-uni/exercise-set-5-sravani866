""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

def process_data(infile, outfile):
    # Load the data from the file
    data = np.loadtxt(infile, delimiter=',')

    # Modify the input data so that it has a mean of 0
    mean_centered_data = data - np.mean(data, axis=0)

    # Modify the zero mean data so that it has a standard deviation of 1
    processed_data = mean_centered_data / np.std(mean_centered_data, axis=0)

    # Save the processed data to OUTFILE using numpy routines
    np.savetxt(outfile, processed_data, delimiter=',')
if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    parser = ArgumentParser(description="This program shifts and scales the data to a mean of 0 and a standard deviation of 1.")

    # Add positional arguments
    parser.add_argument("infile", help="Input filename for the data file that needs to be processed.")
    parser.add_argument("outfile", help="Output filename for the processed data.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Process the data
    process_data(args.infile, args.outfile)

    print(f"Data processed and saved to {args.outfile}.")


