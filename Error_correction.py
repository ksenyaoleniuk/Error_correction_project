import numpy
import binascii


class ErrorCorrection:
    #   generator_matrix = np.matrix([[1, 0, 1, 1], [1, 1, 0, 1], [0, 0, 0, 1], [1, 1, 1, 0], [0, 0, 1, 0],
    # [0, 1, 0, 0], [1, 0, 0, 0]])

    def __init__(self, data):
        self.data = data
        self.check_input_data(self.data)
        self.bits = 8
        self.check_bits = [1, 2, 4, 8]

    def chars_to_bin(self, chars):
        """Transforming characters into binary code."""
        assert not len(chars) * 8 % self.bits
        print(''.join([bin(ord(c))[2:].zfill(8) for c in chars]))
        c = "0"
        c += '0'.join(format(ord(x), 'b') for x in chars)
        # print(c)
        return c



    """def bin_to_chars(self, bin):
        n = int(bin, 2)
        s = binascii.unhexlify('%x' % n)
        print(s)"""

    @staticmethod
    def check_input_data(data):
        if type(data) != str:
            raise TypeError("This data type is incorrect.")



error = ErrorCorrection('data')
error.chars_to_bin('Apple')
#error.bin_to_chars('0b110100001100101011011000110110001101111')
