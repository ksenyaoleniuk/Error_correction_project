import unittest
import numpy
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
        
    def test_bits_to_str(self):
        test_str = "01110100011001010111001101110100011010010110111001100111"
        test_str_2 = "011101000110010101110011011101000110100101101110011001110010000001100011011011110110010001100101"
        expected = "testing"
        expected_2 = "testing code"
        C = ErrorCorrection("data")
        result = C.bits_to_str(test_str)
        result2 = C.bits_to_str(test_str_2)
        self.assertEquals(result, expected)
        self.assertEquals(result2, expected_2)

    def test_bit_str_to_matrix(self):
        test_str = "01110100011001010111001101110100011010010110111001100111"
        test_str_2 = "011101000110010101110011011101000110100101101110011001110010000001100011011011110110010001100101"
        expected = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1]]
        expected_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]]
        C = ErrorCorrection("data")
        result = C.bit_str_to_matrix(test_str)
        result2 = C.bit_str_to_matrix(test_str_2)
        self.assertTrue(result.tolist(), expected)
        self.assertTrue(result2.tolist(), expected_2)
        
    def test_encode_hamming(self):
        test_matrix = np.matrix([[1,1,1,0,0,1,0], [1,0,0,1,1,0,0], [0,1,1,0,0,1,0], [0,1,1,1,0,0,1]])
        expected = np.matrix([[2, 2, 2, 2, 1, 1, 1], [1, 3, 3, 1, 0, 2, 1], [1, 1, 1, 0, 0,1, 0], [1, 2, 2, 2, 1, 1, 1],
                              [1, 0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0], [0,1, 1, 1, 0, 0, 1]]) % 2
        # GENERATOR_M = np.matrix([[1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
        C = ErrorCorrection("data")
        result = C.encode_hamming(test_matrix)
        self.assertTrue(result.tolist(), expected)
        
    def test_correct_errors(self):
        f = ErrorCorrection("data")
        matr = f.bit_str_to_matrix("010010000110010101101111")
        enc_m = f.encode_hamming(matr)
        ans = f.correct_errors(enc_m)
        expected = np.matrix([[1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1], [1 ,0, 0 ,0,0,1], [1, 0, 1, 1, 1,1], [0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 1]])
        self.assertTrue(ans.tolist(), expected)
        
    def test_check_input_data(self):
        self.assertRaises(TypeError, lambda: ErrorCorrection(12))
        self.assertRaises(TypeError, lambda: ErrorCorrection(12.0))
        self.assertRaises(TypeError, lambda: ErrorCorrection(numpy.matrix('1 0;0 1')))
        self.assertRaises(TypeError, lambda: ErrorCorrection([1,2,3]))

if __name__ == '__main__':
    unittest.main()
