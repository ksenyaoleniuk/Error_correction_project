import numpy as np
import random


class ErrorCorrection:
    GENERATOR_M = np.matrix([[1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
    PARITY_CHECK_M = np.matrix([[1,0,1,0,1,0,1], [0,1,1,0,0,1,1], [0,0,0,1,1,1,1]])
    R_M  = np.matrix([[0,0,1,0,0,0,0], [0,0,0,0,1,0,0], [0,0,0,0,0,1,0], [0,0,0,0,0,0,1]])

    def __init__(self, matrix):
        """matrix 4xn"""
        if matrix.shape[0] != 4:
            raise TypeError("Wrong size of a matrix")
        #if type(matrix) != "numpy.matrixlib.defmatrix.matrix":
         #   raise TypeError
        self.matrix = matrix
        self.check_bits = [1, 2, 4, 8]


    def encode_hamming(self, matrix):
        """Generate a matrix of Hamming's codewords from matrix of binary words to encode"""
        return ErrorCorrection.GENERATOR_M.dot(matrix) % 2

    def decode(self, matrix):
        """Return a matrix of decoded words"""
        return ErrorCorrection.R_M.dot(matrix)


    def correct_errors(self, matrix):
        """Correct errors in the columns of matrix(max 1 error for 1 column)"""
        for i in range(matrix.shape[1]):
            error_syndrome = ErrorCorrection.PARITY_CHECK_M.dot(matrix[:, i]) % 2
            print(error_syndrome)
            num_col_err = int(''.join([str(error_syndrome[i, 0]) for i in range(3)]), 2)

            if num_col_err:
                print(num_col_err - 1)
                matrix[num_col_err - 1, i] = int( not matrix[num_col_err - 1, i])
        return matrix

    def simulate_noisy_channel(self, matrix):
        """Randomly chooses a bit to invert(or not ) in each column of a 7xn matrix,
         this way simulating conditions, where Hamming's code(7, 3) is useful"""
        for i in range(matrix.shape[1]):
            err = random.choice([0,1])
            if err:
                bit = random.randint(0, 6)
                print(bit)
                matrix[bit, i] = int(not matrix[bit, i])
        return matrix




class DataConversion:
    def __init__(self, data):
        DataConversion.check_input_data(data)
        self.bits = 8
        self.data = data

    def str_to_bin(self, chars):
        """Transforming characters into binary code."""
        assert not len(chars) * 8 % self.bits
        #c = "0"
        #c += '0'.join(format(ord(x), 'b') for x in chars)
        c = ''.join([bin(ord(k))[2:].zfill(8) for k in chars])
        return c

    def bits_to_str(self, bit_str):
        """Transform binary seq into string"""
        result = ''
        for i in range(len(bit_str) // 8):
            start = i * 8
            end = (i + 1) * 8
            word = bit_str[start:end]
            result += chr(int(word, 2))
        return result

    def bit_str_to_matrix(self, bit_str):
        """Transform bin seq into 4 x len(bin_str) / 4 matrix"""
        lst = []
        for i in range(len(bit_str) // 4):
            start = i * 4
            end = (i + 1) * 4
            nibble = bit_str[start:end]
            lst.append([int(j) for j in nibble])
        return np.matrix(lst).T

    def matrix_to_bit_str(self, matrix):
        """Transform binary matrix into binary seq"""
        return ''.join([''.join([str(nibble[0,i]) for i in range(nibble.shape[1])])for nibble in matrix.T])

    @staticmethod
    def check_input_data(data):
        if type(data) != str:
            raise TypeError("This data type is incorrect.")




def main(str):
    dc = DataConversion(str)

    dc.data = dc.str_to_bin(dc.data)
    matrix = dc.bit_str_to_matrix(dc.data)
    print(matrix)
    err = ErrorCorrection(matrix)

    err.matrix = err.encode_hamming(err.matrix)

    wrong_matrix = err.simulate_noisy_channel(err.matrix)
    #wrong_matrix = err.matrix
    wrong_str = dc.bits_to_str(dc.matrix_to_bit_str(err.decode(wrong_matrix)))

    right_matrix = err.correct_errors(wrong_matrix)

    right_str = dc.bits_to_str(dc.matrix_to_bit_str(err.decode(right_matrix)))

    return wrong_str, right_str


print(main("bty"))











