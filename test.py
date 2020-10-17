import argparse
import json
import tempfile

# import two additional subprocesses
from subprocess import Popen, PIPE


def run_test(input):
    with tempfile.NamedTemporaryFile(mode='w') as prog_in, tempfile.NamedTemporaryFile(mode='r') as prog_out:
        # save the input into the input file
        prog_in.write(input)
        prog_in.flush()

        # and run the test
        # runs "python3 ugen.py - o outputfile inputfile"
        # and redirects the prints (stdout and stderr) so that we can read them
        proc = Popen(['python3', 'ugen.py', '-o',  prog_out.name, prog_in.name],
                     stdout=PIPE, stderr=PIPE)
        # read the outputs form prints and erros in code
        stdout, stderr = proc.communicate()
        # decode them into normal strings so it's readable
        stdout, stderr = stdout.decode(), stderr.decode()

        output = prog_out.read()

        return output, stdout, stderr


def execute_test(test_data):
    # run the test
    output, stdout, stderr = run_test(test_data['input'])

    # save the run information into the config
    result = {
        'input': test_data['input'],
        'actual_output': output,
        'actual_stdout': stdout,
        'actual_stderr': stderr
    }

    passed = True

    # check conditions for whether the test passed
    if 'wanted_output' in test:
        # if user defined some wanted output, check if it matches
        # the actual output
        result['wanted_output'] = test_data['wanted_output']
        passed = passed and test_data['wanted_output'] == output
    if 'wanted_stdout' in test:
        # is user defined some wanted stdout, check if it matches
        # the actual stdout
        result['wanted_stdout'] = test_data['wanted_stdout']
        passed = passed and test_data['wanted_stdout'] == stdout
    if 'wanted_stderr' in test:
        # if user defined some wanted stderr, check if it matches
        # the actual stderr
        result['wanted_stderr'] = test_data['wanted_stderr']
        passed = passed and test_data['wanted_stderr'] == stderr

    # save whether or not the test passed
    result['passed'] = passed
    return passed, result


if __name__ == '__main__':
    # code for a help method
    parser = argparse.ArgumentParser(description='This is my help')
    parser.add_argument('tested_files', type=str, help='create an output file')
    parser.add_argument('test_data', type=str, help="put the input data")

   # parser.print_help()
    args = parser.parse_args()

    with open(args.test_data, 'r') as f:
        tests = json.load(f)

    failed = 0
    succeeded = 0

    results = []

    for test in tests:
        passed, result = execute_test(test)
        results.append(result)

        if passed:
            succeeded += 1
        else:
            failed += 1

    # Write the report with json
    with open('results.json', 'w') as f:
        json.dump(results, f, sort_keys=True, indent=4)

    # Print the result statement to the console
    print('Ran {} test. {} Succeeded, {} Failed'.format(
        (succeeded + failed), succeeded, failed))
