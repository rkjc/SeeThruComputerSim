# val_A and val_B must be strings that contain exactly 8 characters.
# the only allowed characters are '1' and '0'

def add_bin_str(val_A, val_B):
    # sum = A’B’C + A’BC’ + ABC + AB’C’
    # carry-out = AB + BC + AC 

    temp_sum = ""

    carry = '0' # carry is always zero for the calculation in the LSB column 

    # for the binary values as a string: <01234567>
    # the LSB column index is 7
    # the MSB column index is 0 
    for col_index in range(7,-1,-1):  # count down from 7 to 0
        A = (val_A[col_index] == '1') # if the digit in this column position is a 1, then A is True
        B = (val_B[col_index] == '1') # if the digit in this column position is a 1, then B is True
        C = (carry == '1') # if the carry bit is 1 then C is True
                           
        # determine the sum digit for the current column col_index
        term_1 = (not A) and (not B) and  C     # A’B’C
        term_2 = (not A) and B and (not C)      # A’BC’
        term_3 = A and B and C                  # ABC
        term_4 = A and (not B) and  (not C)     # AB’C’
        
        if (term_1 or term_2 or term_3 or term_4):  # (A’B’C) + (A’BC’) + (ABC) + (AB’C’)
            sum_diget = "1"
        else:
            sum_diget = "0"

        # determine and update the carry digit for the next column
        carry_out = (A and B) or (B and C) or (A and C)   # AB + BC + AC
        
        if (carry_out == True):
            carry = "1"
        else:
            carry = "0"

        # update the sum after column bit values have been calculated
        # concatinate the sum digit, build the result string from right to left
        temp_sum = sum_diget + temp_sum
        
    return temp_sum
