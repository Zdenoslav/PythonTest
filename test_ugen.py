import unittest
import ugen
import tempfile

# UNIT TESTS


class TestGenerator(unittest.TestCase):

    # Testing for one input file
    def test_read_input(self):
        lines = ['hello', 'line two man',
                 'wewaada', 'set fireeeeee to the rain']
        # adding a temporary file
        # randomized file
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write('\n'.join(lines))
            f.flush()

            result = ugen.read_input([f.name])
            self.assertListEqual(lines, result)

    # Testing for 2 input files
    def test_read_input2(self):
        lines = ['hello', 'line two man',
                 'wewaada', 'set fireeeeee to the rain']
        lines2 = ['Olaaa', 'Goooo', 'ooooo']
        expected = lines + lines2

        with tempfile.NamedTemporaryFile(mode='w') as f, tempfile.NamedTemporaryFile(mode='w') as f2:
            f.write('\n'.join(lines))
            f.flush()
            f2.write('\n'.join(lines2))
            f2.flush()

            result = ugen.read_input([f.name, f2.name])
            self.assertListEqual(expected, result)

    def test_parse_input(self):
        lines = ['1234:terry:crews:develop', '435:jeanluc:picard:starfleet']
        expected = [['1234', 'terry', 'crews', 'develop'],
                    ['435', 'jeanluc', 'picard', 'starfleet']]

        result = ugen.parse_input(lines)

        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertListEqual(result[i], expected[i])

    def test_parse_input_missing_data(self):
        def func():
            lines = ['1234:terry:crews']
            ugen.parse_input(lines)

        self.assertRaises(ValueError, func)

    # test if the function generates the username
    def test_generate_usernames(self):
        data = [['1234', 'terry', 'crews', 'develop'],
                ['435', 'jeanluc', 'picard', 'starfleet']]
        expected = [['1234', 'tcrews', 'terry', 'crews', 'develop'],
                    ['435', 'jpicard', 'jeanluc', 'picard', 'starfleet']]

        ugen.generate_usernames(data)

        self.assertEqual(len(data), len(expected))
        for i in range(len(data)):
            self.assertListEqual(data[i], expected[i])

    def test_generate_usernames_duplicated_names_usernames_different(self):
        data = [['1234', 'terry', 'crews', 'develop'],
                ['435', 'tumbi', 'crews', 'starfleet']]

        ugen.generate_usernames(data)

        self.assertNotEqual(data[0][1], data[1][1])

    def test_write_output(self):
        data = [['1234', 'terry', 'crews', 'develop'],
                ['435', 'jeanluc', 'picard', 'starfleet']]
        expected = '1234:terry:crews:develop\n435:jeanluc:picard:starfleet'

        with tempfile.NamedTemporaryFile(mode='r') as f:
            ugen.write_output(f.name, data)

            written = f.read()
            self.assertEqual(expected, written)


if __name__ == '__main__':
    unittest.main()
