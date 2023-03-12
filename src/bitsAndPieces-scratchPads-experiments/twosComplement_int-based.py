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

def twos_comp_to_bin_str(inInt, numBits=8):
      if inInt < 0:
            


      
anInt1 = 73
print(int_to_bin_str(anInt1))

anInt2 = 99
print(int_to_bin_str(anInt2))

subResult = anInt1 - anInt2
print(subResult) 
print(bin(subResult))

