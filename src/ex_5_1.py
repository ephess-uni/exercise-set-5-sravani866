"""ex_5_1.py"""
import argparse
import subprocess

try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
     parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")

    # Add a positional argument 'infile' to the parser
     parser.add_argument('infile', help='The input file to count lines.')

    # Parse the command-line arguments
     args = parser.parse_args()

    # Call the main function with the infile argument
     main(args.infile)

    # Additional code to run tests using a system call
     try:
        # Replace 'pytest' with the actual command to run your tests
         subprocess.run(['testpy', 'tests/src.ex_5_0.py'])
     except FileNotFoundError:
         print("Error: Please make sure 'pytest' is installed.")


      
   
