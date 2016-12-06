import numpy as np



class ErrorCorrection:
    GENERATOR_M = np.matrix([[1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
    PARITY_CHECK_M = np.matrix([[1,0,1,0,1,0,1], [0,1,1,0,0,1,1], [0,0,0,1,1,1,1]])
    R_M  = np.matrix([[0,0,1,0,0,0,0], [0,0,0,0,1,0,0], [0,0,0,0,0,1,0], [0,0,0,0,0,0,1]])


    def __init__(self, string):
        self.string = string
        self.check_input_data(self.string)
        self.bits = 8
        self.check_bits = [1, 2, 4, 8]

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
            num_col_err = int(''.join([str(error_syndrome[i, 0]) for i in range(3)]), 2)

            if num_col_err:
                matrix[num_col_err - 1, i] = int( not matrix[num_col_err - 1, i])
        return matrix




    @staticmethod
    def check_input_data(data):
        if type(data) != str:
            raise TypeError("This data type is incorrect.")





err = ErrorCorrection("dxcfg")
print(err.matrix_to_bit_str(np.matrix([[1,3,],[6,7]])))
