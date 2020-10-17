import argparse


def read_input(input_paths):
    """
    Read the input files.
    :param input_paths:
    :return:
    """
    result = []
    for input_path in input_paths:
        with open(input_path, 'r') as f:
            lines = f.read().split('\n')
            # Check for the empty files
            if len(lines) == 1 and len(lines[0]) == 0:
                continue
            result.extend(lines)

    return result


def parse_input(lines):
    """
    :param lines:
    :return:
    """
    data = []
    for i in range(len(lines)):
        contents = lines[i].split(':')
        # Check if the input if of a correct length
        if len(contents) != 4:
            raise ValueError(
                'Error line {}: Expected 4 values split by \':\''.format(i))

        data.append(contents)

    return data


def generate_usernames(data):
    """
    generate usernames
    a list to store the usernames and check if the username already exists
    :param data:
    :return:
    """
    usedUsernames = []

    for entry in data:  # start loop
        fname = entry[1]
        lname = entry[2]

        original_username = fname[0] + lname  # make username
        username = original_username
        counter = 1

        while username in usedUsernames:
            username = original_username + str(counter)
            counter += 1

        usedUsernames.append(username)

        entry.insert(1, username)


def write_output(path, data):
    with open(path, 'w') as f:
        f.write('\n'.join([':'.join(entry).lower() for entry in data]))


if __name__ == '__main__':
    try:
        # code for a help method
        parser = argparse.ArgumentParser(description='This is my help')
        # an argument to add the output file
        parser.add_argument('-o', '--output', type=str,
                            required=True, help='create an output file')
        # an argument to add the input files
        parser.add_argument('input_files', type=str, nargs='+', )
        args = parser.parse_args()

        lines = read_input(args.input_files)
        data = parse_input(lines)
        generate_usernames(data)
        write_output(args.output, data)
    except Exception as e:
        print(str(e))
