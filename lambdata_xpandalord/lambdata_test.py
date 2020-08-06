import unittest
from random import randint

# unittest supports a type of tests called unit tests
# A unit is the smallest cohesive piece of code we can test
# (usually something like a function or method)

# Other types of tests (you won't write now, just to be aware):
# - Integration: testing multiple pieces working together
# - End to end: testing a full "flow"/use case
# There are also manual/non-code tests that are common
# - User acceptance testing: show it to a user, get feedback
# - Manual running and checking

from example_module import increment, COLORS
from oop_examples import SocialMediaUser

class ExampleUnitTests(unittest.TestCase):
    """Making sure our examples behave as expected."""
    def test_increment(self):
        """Testing that increment adds one to a number."""
        x1 = 5
        y1 = increment(x1)
        x2 = -106
        y2 = increment(x2)
        # Now we make sure the output is as expected with assertions
        self.assertEqual(y1, 6)
        self.assertEqual(y2, -105)

    def test_increment_random(self):
        """Test increment with randomly geenrated input."""
        x1 = randint(1, 1000000)
        y1 = increment(x1)
        self.assertEqual(y1, x1 + 1)

    def test_colors(self):
        """Testing presence/absence of expected colors."""
        self.assertIn('Orange', COLORS)
        self.assertNotIn('Aquemarine', COLORS)
        self.assertEqual(len(COLORS), 6)


if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()