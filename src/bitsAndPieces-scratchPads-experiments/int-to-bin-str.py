 
def int_to_bin_str(intIn, numBits=8):
      tempStr = ((bin(intIn))[2:numBits+2])
      tempStr = ((numBits - len(tempStr))*"0") + tempStr
      return tempStr



myInt = 23
print(int_to_bin_str(myInt))

