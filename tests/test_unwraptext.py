# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from unwraptext.unwraptext import unwrap_markdown


class TestUnwrapText(unittest.TestCase):

    def test_markdown_1(self):
        with open("./tests/test1_in.md") as f_in:
            with open("./tests/test1_out.md") as f_out:
                text_in = f_in.read()
                text_out = f_out.read()
                self.assertEqual(unwrap_markdown(text_in), text_out)


if __name__ == '__main__':
    unittest.main()
