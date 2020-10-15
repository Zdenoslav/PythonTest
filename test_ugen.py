import unittest
import ugen
import tempfile


class TestGenerator(unittest.TestCase):

    def test_read_input(self):
        lines = ['hello', 'line two man',
                 'wewaada', 'set fireeeeee to the rain', 'input_file1.txt', 'input_file2.txt']
        with tempfile.NamedTemporaryFile(mode='w') as f:
            # start indentation
            f.write('\n'.join(lines))
            f.flush()
            result = ugen.read_input([f.name])
            self.assertListEqual(lines, result)
            # end intentation

   # def test_generate_usernames(self):

   # def test_write_output(self):
   #     pass


if __name__ == '__main__':
    unittest.main()
