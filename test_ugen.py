import unittest
import ugen
import tempfile


class TestGenerator(unittest.TestCase):

    # Testing for one input file
    def test_read_input(self):
        lines = ['hello\n', 'line two man\n', 'wewaada\n',
                 'set fireeeeee to the rain']
        # adding a temporary file
        # randomized file
        with tempfile.NamedTemporaryFile(mode='w') as f:

            f.write(''.join(lines))
            f.flush()
            result = ugen.read_input([f.name])
            self.assertListEqual(lines, result)

    # Testing for 2 input files
    def test_read_input2(self):

        lines = ['hello\n', 'line two man\n',
                 'wewaada\n', 'set fireeeeee to the rain']
        # two possible files as inputs to test
        lines2 = ['Olaaa\n', 'Goooo\n', 'ooooo']

        with tempfile.NamedTemporaryFile(mode='w') as f, tempfile.NamedTemporaryFile(mode='w') as f2:

            f.write(''.join(lines))
            f.flush()
            f2.write(''.join(lines2))
            f2.flush()

            result = ugen.read_input([f.name, f2.name])

            # combining the lists
            lines[-1] += "\n"
            lines.extend(lines2)
            self.assertListEqual(lines, result)

    # test if the function generates the username
    def test_generate_usernames(self):

        data = ['123:terry:crews:develop', '435:jeanluc:picard:starfleet']

        expected = ['123:tcrews:terry:crews:develop',
                    '435:jpicard:jeanluc:picard:starfleet']

        result = ugen.generate_usernames(data)
        self.assertEqual(expected, result)

    def test_generate_usernames_duplicated_usernames(self):
        data = ['123:terry:crews:develop', '435:tumbi:crews:starfleet']

        result = ugen.generate_usernames(data)
        username1 = result[0].split(':')[1]
        username2 = result[1].split(':')[1]
        self.assertNotEqual(username1, username2)

    def test_write_output(self):

        data = ['jpicard']

        result = ugen.test_write_output()
        self.assertEqual('output.txt')

    def test_write_output(self):

        data = ['123:tcrews:terry:crews:develop\n',
                '435:jpicard:jeanluc:picard:starfleet']

        with tempfile.NamedTemporaryFile(mode='w') as f:
            ugen.write_output(data, f.name)

            written = f.readlines()
            self.assertListEqual(data, written)


if __name__ == '__main__':
    unittest.main()
