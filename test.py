import random
import names
import io
import argparse
import os
import tempfile


# run the ugen.py program and give it the input files


# read the output file and see if the data is as expected


if __name__ == '__main__':
    # code for a help method
    parser = argparse.ArgumentParser(description='This is my help')
    parser.add_argument('tested_files', type=str, help='create an output file')
    parser.add_argument('test_data', type=str)
    args = parser.parse_args()

    with tempfile.NamedTemporaryFile(mode='w') as f:
        f.write(args.test_data)
        f.flush()

        os.system('python3 ugen.py -o output.txt {}'.format(f.name))
