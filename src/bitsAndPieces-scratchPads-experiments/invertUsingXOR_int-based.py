# have gone a different route and am using strings to store the binary
# values in the sim as they are easier to follow on their
# journey through the processes in the computer sim.

def int_to_bin_str(intIn, numBits=8, spacer=0):
      tempStr = (str(bin(intIn))[2:])
      tempStr = ((numBits - len(tempStr))*"0") + tempStr
      outStr = ""
      for c in tempStr:
          outStr = outStr + c + (" " * spacer)
      return outStr
    
anInt1 = 73
print(int_to_bin_str(anInt1))


invertedReult = anInt1 ^ 255 #for 8-bit values
print(int_to_bin_str(invertedReult))

