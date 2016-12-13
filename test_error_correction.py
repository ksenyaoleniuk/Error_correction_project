import unittest
from Error_correction import ErrorCorrection
from Error_correction import DataConversion
import numpy as np


class TestErrorCorrection(unittest.TestCase):

    def test_str_to_bin(self):
        test_str = "testing"
        test_str_2 = "testing code"
        expected = "01110100011001010111001101110100011010010110111001100111"
        expected_2 = "011101000110010101110011011101000110100101101110011001110010000001100011011011110110010001100101"
        C = DataConversion("data")
        result = C.str_to_bin(test_str)
        result2 = C.str_to_bin(test_str_2)
        self.assertEquals(result, expected)
        self.assertEquals(result2, expected_2)

    def test_bits_to_str(self):
        test_str = "01110100011001010111001101110100011010010110111001100111"
        test_str_2 = "011101000110010101110011011101000110100101101110011001110010000001100011011011110110010001100101"
        expected = "testing"
        expected_2 = "testing code"
        C = DataConversion("data")
        result = C.bits_to_str(test_str)
        result2 = C.bits_to_str(test_str_2)
        self.assertEquals(result, expected)
        self.assertEquals(result2, expected_2)

    def test_bit_str_to_matrix(self):
        test_str = "01110100011001010111001101110100011010010110111001100111"
        test_str_2 = "011101000110010101110011011101000110100101101110011001110010000001100011011011110110010001100101"
        expected = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1]]
        expected_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]]
        C = DataConversion("data")
        result = C.bit_str_to_matrix(test_str)
        result2 = C.bit_str_to_matrix(test_str_2)
        self.assertTrue(result.tolist(), expected)
        self.assertTrue(result2.tolist(), expected_2)

    def test_check_input_data(self):
        self.assertRaises(TypeError, lambda: ErrorCorrection(12))
        self.assertRaises(TypeError, lambda: ErrorCorrection(12.0))
        self.assertRaises(TypeError, lambda: ErrorCorrection(np.matrix('1 0;0 1')))
        self.assertRaises(TypeError, lambda: ErrorCorrection([1,2,3]))

    def test_matrix_to_bit_str(self):
        test_matrix = np.matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1]])
        test_matrix_2 = np.matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1]])
        expected = "01110100011001010111001101110100011010010110111001100111"
        expected_2 = "011101000110010101110011011101000110100101101110011001110010000001100011011011110110010001100101"
        C = DataConversion("data")
        result = C.matrix_to_bit_str(test_matrix)
        result2 = C.matrix_to_bit_str(test_matrix_2)
        self.assertTrue(result, expected)
        self.assertTrue(result2, expected_2)

    # -----------------------------------------------------------------------------------

        def test_encode_hamming(self):
        test_str = "apple"
        test = DataConversion(test_str)
        test.data = test.str_to_bin(test.data)
        matrix = test.bit_str_to_matrix(test.data)
        test_err = ErrorCorrection(matrix)
        n = test_err.matrix = test_err.encode_hamming(test_err.matrix)
        expected = [[1, 1, 0, 0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 1]]
        self.assertTrue(n.tolist(), expected)


    def test_correct_errors(self):
        test_str = "apple"
        test = DataConversion(test_str)
        test.data = test.str_to_bin(test.data)
        matrix = test.bit_str_to_matrix(test.data)
        test_err = ErrorCorrection(matrix)
        test_err.matrix = test_err.encode_hamming(test_err.matrix)
        wrong_matrix = np.matrix([[1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]])
        right_matrix, error_bits = test_err.correct_errors(wrong_matrix)
        expected_right_matrix = [[1, 1, 0, 0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 1]]
        expected_error_bits = [2, 11, 18, 41, 42]
        self.assertEqual(right_matrix.tolist(), expected_right_matrix)
        self.assertEqual(error_bits, expected_error_bits)

    def test_decode(self):
        test_str = "apple"
        test = DataConversion(test_str)
        test.data = test.str_to_bin(test.data)
        matrix = test.bit_str_to_matrix(test.data)
        test_err = ErrorCorrection(matrix)
        test_err.matrix = test_err.encode_hamming(test_err.matrix)
        wrong_matrix = test_err.simulate_noisy_channel(test_err.matrix)
        right_matrix, error_bits = test_err.correct_errors(wrong_matrix)
        right_str = test.bits_to_str(test.matrix_to_bit_str(test_err.decode(right_matrix)))
        test_str_2 = "banana"
        test = DataConversion(test_str_2)
        test.data = test.str_to_bin(test.data)
        matrix = test.bit_str_to_matrix(test.data)
        test_err = ErrorCorrection(matrix)
        test_err.matrix = test_err.encode_hamming(test_err.matrix)
        wrong_matrix = test_err.simulate_noisy_channel(test_err.matrix)
        right_matrix, error_bits = test_err.correct_errors(wrong_matrix)
        right_str_2 = test.bits_to_str(test.matrix_to_bit_str(test_err.decode(right_matrix)))
        self.assertEqual(test_str, right_str)
        self.assertEqual(test_str_2, right_str_2 )
if __name__ == '__main__':
    unittest.main()
