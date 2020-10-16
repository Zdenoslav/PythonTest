import random
import names
import io
import argparse
import os
import tempfile
import json

# why this main?
if __name__ == '__main__':
    # code for a help method
    parser = argparse.ArgumentParser(description='This is my help')
    parser.add_argument('tested_files', type=str, help='create an output file')
    parser.add_argument('test_data', type=str)
    args = parser.parse_args()

    file = open(args.test_data, 'r')
    tests = json.load(file)
    file.close()

    testsFailed = 0
    testsSucceeded = 0

    results = []

    for test in tests:
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write(test['input'])
            f.flush()  # and run the test
            os.system('python3 ugen.py -o output.txt {}'.format(f.name))

            # read the output.txt file
            file = open('output.txt', 'r')
            output = file.read()
            file.close()

            result = {}

            result['input'] = test['input']
            result['output'] = test['output']

            if test['output'] == output:
                testsSucceeded += 1
                result['passed'] = True

            else:
                print(test['output'])
                print(output)
                result['passed'] = False
                testsFailed += 1

            results.append(result)

    file = open('results.json', 'w')
    json.dump(results, file, sort_keys=True, indent=4)
    file.close()

print(results)
print(testsSucceeded)
print(testsFailed)
