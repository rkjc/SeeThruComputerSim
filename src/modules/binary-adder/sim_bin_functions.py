
# ------------- functions ----------------
# Logical NOT
# takes a binary value of any length in string format
# returns the 'not' or inverted binary string of same length
def not_binStr(inBinStr):
    tempBinStr = ""
    for c in inBinStr:
        if c == "1":
            tempBinStr += "0"
        else:
            tempBinStr += "1"
    return tempBinStr


# Twos Complement
# takes a binary value in string form
# returns a same number of bits twos complement binary string
def twosComp(inBinStr):
    inverted_InBinStr = not_binStr(inBinStr)
    binCompStr = ("0" * (len(inBinStr) - 1)) + "1"
    binCompStr = adder_binStr(inverted_InBinStr, binCompStr)
    return binCompStr

"""
ADD two binary numbers
takes two binary values in string format, inputs must be same length
uses boolean expressions to produce a binary sum
Because of collection indexing numbers the colum index
variable 'i' starts at numBits - 1 for the right most LSB digit
The left most MSB digit is column index i = 0
"""
def adder_binStr(val1, val2):
    # sum = A’B’C + A’BC’ + ABC + AB’C’
    # carry-out = AB + BC + AC
    numBits = len(val1)
    tempSum = ""
    # carry value is an array of chars instead of a binary as string
    # but it is only used in the method and not returned
    carry = ['0'] * numBits  # makes an array of '0's to match the length of the input values

    # for these binary numbers as strings, the LSB column index is numBits-1
    # using range statement attributes that gives i = numBits - 1 down to 0
    for i in range(numBits-1, -1, -1):
        # determine the sum diget for the current column i
        trm1 = val1[i] == "0" and val2[i] == "0" and  carry[i] == "1" # A’B’C
        trm2 = val1[i] == "0" and val2[i] == "1" and  carry[i] == "0" # A’BC’
        trm3 = val1[i] == "1" and val2[i] == "1" and  carry[i] == "1" # ABC
        trm4 = val1[i] == "1" and val2[i] == "0" and  carry[i] == "0" # AB’C’
        if (trm1 or trm2 or trm3 or trm4):
            sumDiget = "1"
        else:
            sumDiget = "0"

        # determine and update the carry diget for the column i-1
        # Carry is not calculated for column 0 as it will be discarded as overflow
        if i > 0:
            tcry1 = val1[i] == "1" and val2[i] == "1"   # AB
            tcry2 = val2[i] == "1" and  carry[i] == "1" # BC
            tcry3 = val1[i] == "1" and  carry[i] == "1" # AC
            if (tcry1 or tcry2 or tcry3):
                carryDiget = "1"
            else:
                carryDiget = "0"

            # update the carry bit value
            # using i-1 because the carry result is always saved in # the next column to the left of the sum value
            carry[i - 1] = carryDiget

        # update the sum after column bit values have been calculated
        tempSum = sumDiget + tempSum
        # when column 0 only gets a sum value, carry is discarded
    return tempSum
 
