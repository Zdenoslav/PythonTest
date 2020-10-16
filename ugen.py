import argparse
import io
import random

# read the input files


def read_input(input_paths):

    lines = []
    for input_path in input_paths:
        # in loop
        f = open(input_path, 'r')
        lines.extend(f.readlines())
        lines[-1] += '\n'
        f.close()  # end loop  return lines

    lines[-1] = lines[-1][:-1]

    return lines
# generate usernames
# a list to store the usernames and check if the username already exists


def generate_usernames(lines):

    output = []
    usedUsernames = []

    for line in lines:  # start loop

        split = line.split(':')

        fname = split[1]
        lname = split[2]

        username = fname[0] + lname  # make username

        if username in usedUsernames:
            # start
            username += str(random.randint(0, 9))
        # end
        usedUsernames.append(username)

        split.insert(1, username)
        line = ':'.join(split)
        output.append(line)  # end loop

    return output


def write_output(username, path):

    f = open(path, 'w')
    f.write(''.join(username).lower())
    f.close()


if __name__ == '__main__':
    # code for a help method
    parser = argparse.ArgumentParser(description='This is my help')
# an argument to add the output file
    parser.add_argument('-o', '--output', type=str,
                        required=True, help='create an output file')
# an argument to add the input files
    parser.add_argument('input_files', type=str, nargs='+',)
    args = parser.parse_args()

    lines = read_input(args.input_files)
    username = generate_usernames(lines)

    path = args.output
    write_output(username, path)
