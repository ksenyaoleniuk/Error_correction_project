import unittest
from Error_correction import ErrorCorrection


class TestErrorCorrection(unittest.TestCase):

    def test_str_to_bin(self):
        test_str = "testing"
        test_str_2 = "testing code"
        expected = "01110100011001010111001101110100011010010110111001100111"
        expected_2 = "011101000110010101110011011101000110100101101110011001110010000001100011011011110110010001100101"
        C = ErrorCorrection("data")
        result = C.str_to_bin(test_str)
        result2 = C.str_to_bin(test_str_2)
        self.assertEquals(result, expected)
        self.assertEquals(result2, expected_2)


if __name__ == '__main__':
    unittest.main()
