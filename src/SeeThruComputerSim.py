# ---- imports ----
from time import sleep 

# ---- variables ----
clockSpd = 1000 #int
progCntr = 0 #int
accum = "00000000"
status = 2
statStr = ["stop =", "run ==", "write "]
opcode = "0000"
operand = "0000"


# default empty memory
memory = ["00000000", # 0000 
          "00000000", # 0001 
          "00000000", # 0010 
          "00000000", # 0011 
          "00000000", # 0100 
          "00000000", # 0101 
          "00000000", # 0110 
          "00000000", # 0111 
          "00000000", # 1000 
          "00000000", # 1001 
          "00000000", # 1010 
          "00000000", # 1011 
          "00000000", # 1100 
          "00000000", # 1101 
          "00000000", # 1110 
          "00000000"] # 1111 

# The file  "../files/Sample-Programs-for-SeeThruComputer.txt"  contains
# some sample programs. To use them copy the memory array initialization
# code and paste it in place of the default momory array code above.

# ---- functions ----

# Provides a bit-wise binary 'not' return 
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


# takes a binary value in string form
# returns a same number of bits 2s complement binary string
def twosComp(inBinStr):
    invInBinStr = not_binStr(inBinStr)
    binCompStr = ("0" * (len(inBinStr) - 1)) + "1" 
    binCompStr = adder_binStr(invInBinStr, binCompStr)
    return binCompStr


# takes two binary values in string format, inputs must be same length
# uses boolean expressions to produce a binary sum
# Because of collection indexing numbers the colum index
# variable 'i' starts at numBits - 1 for the right most LSB digit
# The left most MSB digit is column index i = 0
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

# converts a positive integer value into a string of 1' and 0'
# unsigned binary representation, includes leading 0s
def int_to_bin_str(intIn, numBits=8):
      tempStr = ((bin(intIn))[2:])
      tempStr = ((numBits - len(tempStr))*"0") + tempStr
      return tempStr 

# adds spaces between each charachter to make it more readable on the screen
def expandBinStr(inBinStr, spaceNum=1):
      outStr = ""
      for c in inBinStr:
          outStr = outStr + c + (" " * spaceNum)
      return outStr

# changes the status to run and startes the execution of the program in memory
def runProg():
    global progCntr
    global status
    global opcode
    global operand
    
    #print("running prog")
    progCntr = 0
    whileCnt = 0
    status = 1
    while(status == 1):
        #print('while count ', whileCnt) #debug
        whileCnt += 1
        currentMem = memory[progCntr]
        opcode = currentMem[:4]
        operand = currentMem[4:]
        #print("opcode= ", opcode, " - operand= ", operand) #debug
        doInstruction()
        #print("*** return from doInst - PC= ", progCntr) #debug
        if clockSpd == 0:
            input("push enter for next step")
        else:
            sleep(clockSpd/1000.0)

        if progCntr > 15:
            progCntr = 15
            status = 0

# CPU instruction interpreter
def doInstruction(): 
    # connect the CPU to all of it's register memories 
    global progCntr
    global status
    global accum
    global opcode
    global operand

    xopcode = opcode
    xoperand = operand
    
    # for simulator use, the program counter is a numeric integer value  
    nextPC = progCntr + 1 
    # convert operand string to int for simulator index use
    memLoc = int(xoperand,2) 
    # retrive the binary as string contents of referenced memory location
    memBinStr = memory[memLoc]
    
    if xopcode == '0000':
        #print("inside opcode 0000")
        pass
      
    elif xopcode == '0001': # SHIFT R
        accum = "0" + accum[:len(accum)-1]
        
    elif xopcode == '0010': # SHIFT L
        accum = accum[1:] + "0"
        
    elif xopcode == '0011': # NOT 
        accum = not_binStr(accum)
        
    elif xopcode == '0100': # AND
        tempAccum = ""
        tempMem = memBinStr
        for i in range(len(accum)):
          if accum[i] == "1" and tempMem[i] == "1":
             tempAccum += "1"
          else:
             tempAccum += "0" 
        accum = tempAccum
        
    elif xopcode == '0101': # OR
        tempAccum = ""
        tempMem = memBinStr
        for i in range(len(accum)):
           if accum[i] == "0" and tempMem[i] == "0":
              tempAccum += "0"
           else:
              tempAccum += "1"
        accum = tempAccum 
        
    elif xopcode == '0110': # XOR
        tempAccum = ""
        tempMem = memBinStr
        for i in range(len(accum)):
           if accum[i] == tempMem[i]:
              tempAccum += "0"
           else:
              tempAccum += "1" 
        accum = tempAccum
        
    elif xopcode == '0111': # UNDEFINED
        pass
      
    elif xopcode == '1000': # LOAD
        accum = memory[memLoc]
        
    elif xopcode == '1001': # STORE
        memory[memLoc] = accum
        
    elif xopcode == '1010': # ADD
          accum = adder_binStr(accum, memBinStr) 
        
    elif xopcode == '1011': # SUB
          twosCompMemBinStr = twosComp(memBinStr) 
          accum = adder_binStr(accum, twosCompMemBinStr)
 
    elif xopcode == '1100': # GOTO
        nextPC = memLoc 
        
    elif xopcode == '1101':  # IFZERO jump
        if accum == "00000000":
            nextPC = memLoc
        
    elif xopcode == '1110': # UNDEFINED
        pass
    elif xopcode == '1111': # STOP
        nextPC = progCntr
        status = 0
        #print("*** called stop - PC= ", progCntr) #debug

    showStatus()
    
    if nextPC > 15:
        progCntr = 15
        status = 0
    else:
        progCntr = nextPC
        #print("*** leav doInst - PC= ", progCntr) #debug


def showStatus():
    global opcode
    global operand
    global accum
    print("\n\n\n  -----------------------------------------------------------\n  ===================== status = " + statStr[status] + "======================")
    print('''  -----------------------------------------------------------
  |  program  |  current  |   current   |    accumulator    |
  |  counter  |  op code  |   operand   |     contents      |
  -----------------------------------------------------------''')
    PCbinStr = expandBinStr(int_to_bin_str(progCntr, 4))
    print("  |  " + PCbinStr + " |  " + expandBinStr(opcode) + " |   " + expandBinStr(operand) + "  |  " +  expandBinStr(accum) + " |")
    print('''  ===========================================================
  | memory contents:               |
  | PC | address  |   stored data  |
  |                                |''')
      
    count = 0
    for count in range(16):
          lineLead = "  |       "
          if count == progCntr:
              lineLead = "  | PC>   "
          memStr = memory[count]
          PCstr = int_to_bin_str(count, 4)
          print(lineLead + PCstr + "  - - -  " + memStr + "    |")

    print("  ##########################################################")


# ---- pre-run program input loop ----  

while(True):
    showStatus()
    print('''
    select operation:
    (a)run program
    (b)store binary data in current memory address
    (c)change current Program Counter pointer
    (d)set clock speed in milliseconds (enter an integer value)
    ''', end="")
    
    inStr = input("enter-> ")

    command = inStr[0].lower()
    inTrimStr = inStr[1:9] # for 8-bit inputs
    
    if command == 'a': 
        runProg()
        break
    elif command =='b':
        memory[progCntr] = inTrimStr
        if progCntr < 15:
           progCntr += 1
    elif command == 'c':
        inInt = int(inTrimStr, 2)
        progCntr = inInt
    elif command == 'd':
        inTimeStr = inStr[1:]
        inTimeInt = int(inTimeStr)
        clockSpd = inTimeInt 



