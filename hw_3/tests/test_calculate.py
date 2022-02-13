from unittest import TestCase
from calcalc.CalCalc import calculate


def test_easy_operations():
    inputs = [[10, 12],
              [65, 32],
              [0.3, 1.24],
              [2.2, 2]]
    operations = ['+',
                  '-',
                  '*',
                  '/']
    outputs = [22,
               33,
               0.372,
               1.1]
    for (i, xy) in enumerate(inputs):
        xy_as_string = operations[i].join([str(k) for k in xy])
        assert calculate(xy_as_string) == outputs[i]


def test_long_operations():
    inputs = ['2 * (3+4)',
              '2 + 3**2 / 3']
    outputs = [14,
               5]
    for (i, xy) in enumerate(inputs):
        assert calculate(xy) == outputs[i]


def test_wolfram_string():
    inputs = ['speed of sound in m/s',
              'distance to the moon in feet',
              'distance to the moon in inches']
    outputs = ['340.27 m/s (meters per second)',
               '1.317×10^9 feet',
               '1.58×10^10 inches']
    for (i, xy) in enumerate(inputs):
        assert calculate(xy, return_float=False) == outputs[i]


def test_wolfram_float():
    inputs = ['speed of sound in m/s',
              'distance to the moon in feet']
    scale_by = [2,
                0.5]
    outputs = [340.27,
               1.317e9]
    for (i, xy) in enumerate(inputs):
        assert scale_by[i] * calculate(xy) == scale_by[i] * outputs[i]


class TestErrorCodes(TestCase):
    def test_bad_inputs(self):
        inputs = [['not a string'],
                  23.2 / 15]
        for i in inputs:
            with self.assertRaises(ValueError):
                calculate(i)

    def test_nonsense(self):
        inputs = ['gorilla',
                  'mass of a frog',
                  'how to train your dragon']
        for i in inputs:
            self.assertEqual(calculate(i), 'idk')
