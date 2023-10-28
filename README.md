# Task

Please use Python to develop code which will take two input files, both files
consist of lexicographically sorted in the same order ASCII strings, and will
produce two output files - first output file should contain only strings which
were found in first input file, but not in the second one; second output file -
strings found in the second input file, but not in the first one.

## Usage

    process_files.py [-h] [--file1_out FILE1_OUT] [--file2_out FILE2_OUT]
                     FILE1 FILE2

    positional arguments:
      FILE1                 first file
      FILE2                 second file

    optional arguments:
      -h, --help            show this help message and exit
      --file1_out FILE1_OUT
                            output for the first file (default: FILE1 + ".out")
      --file2_out FILE2_OUT
                            output for the second file (default: FILE2 + ".out")


## Tests

To run tests:

    $ python -m pytest


## Examples

File `foo.txt`:

    a
    b
    d
    e
    e
    t
    z
    z
    z
    z
    z


File `bar.txt`:

    a
    b
    e
    e
    x
    x
    x
    x
    x
    z
    z
    z


Run:

    $ cd examples
    $ process_files.py foo.txt bar.txt


Output file `foo.txt.out`:

    d
    t


Output file `bar.txt.out`:

    x
    x
    x
    x
    x
