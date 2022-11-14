SeeThruComputerSim Project
===

> ## Simulated 4-bit computer

<br>

This simulation computer is written in Python3 and runs in a terminal, so hopefully this program should be cross platform. I tried to keep the Python code as strait forward as possible, but hey, reading someone else code is always a challenge.  

The program uses a string value of 1's and 0's to represent binary data.  
This allows for a simpler way of demonstrating boolean logical and arithmetic operations. Most languages make it difficult to access the 2's complement process involved in signed binary math operations.  

This simulated computer has a memory with an address space of 16 locations. Each address in memory can hold 1-byte of binary data (8-bits). This means it has a massive 16 bytes of memory!  

This system only has a volatile memory that is reset when re-started. It has no persistent storage drive. The program can be re-written to start with a memory snapshot that has pre-recorded values, but that is only for expediency sake. BareBonesBinary model-2 will probably ship with a 'hard drive' file ... later.

The instruction format is 8-bits, with the first 4-bits as the Operation Code, and the second 4-bits as the Operand.  
| Op-Code |    Operand |  
| :---: | :---: |
| 4-bits | 4-bits | 

The Operand data in this architecture is a memory address value for the instructions that need to use it.  

<br>

================================================================

## Operation:  

To run the program in the memory enter the single character  
`a`  
at the prompt and hit `enter`  
the Program counter will be reset to `0000`  
and the computer will start running the instruction at memory location `0000`  

***

To enter data into the memory location indicated by the Program Counter,
enter the letter `b` followed by an 8-bit binary number, with no spaces

example:  
`b10010101`  
then hit `enter`  
will store the binary value `10010101` at that address and then increment the Program Counter

***

To move the program counter enter a `c` followed by a 4-bit binary number, with no spaces

`c1010`  
This will move the program counter to the memory address `1010`

***

The default program execution speed is one instruction per clock cycle (1000 milliseconds).  
To change the clock speed enter the letter `d` followed by an integer value in milliseconds.  

`d500`  
For example this will set it to run an instruction every 0.5 seconds.

To run the program manually set the clock speed to zero.  
`d0`  
Every time the enter key is pressed the next instruction will be executed.

------------------------------------------------------------------------------  
<br>

Instruction Set for this computer:
---
```
  opcode	Name	Description
  
   0000	    NOP 	No operation; safely ignored.

 logic instructions
   shift
     0001	SHIFTR 	Bit shift the accumulator to the right by 1 position.
     0010	SHIFTL 	Bit shift the accumulator to the left by 1 position.

   boolean
     0011	NOT 	Bit-wise Binary NOT of the accumulator, saved to accumulator.
     0100	AND 	Bit-wise Binary AND of the accumulator with the value stored at operand address, saved to accumulator.
     0101	OR 	Bit-wise Binary OR of the accumulator with the value stored at operand address, saved to accumulator.
     0110	XOR 	Bit-wise Binary XOR of the accumulator with the value stored at operand address, saved to accumulator.

I/O  data transfer instructions
     1000	LOAD DIRECT <operand> - Load the accumulator with the value stored at the operand as an address.
     0111 LOAD INDIRECT <operand> - Load accumulator with value from address pointed to by contents of the address pointed to by the operand.
     1110 LOAD IMEADIATE <operand> - operand is loaded to accumulator.
     1001	STORE 	Copy the accumulator into an address.

arithmetic instructions 
     1010	ADD 	Add the value stored at an address to the accumulator.
     1011	SUB 	Subtract the value stored at an address from the accumulator.

control instructions 
     branch
     1100	GOTO 	Jump to a program address.
     1101	IFZERO 	If the accumulator is zero, jump to a program address.
     1111	STOP 	Stop program execution.

```     
--------------------------------------------------  
Example program that counts from 1 to 9 
---

<img src=images/SeeThruComputerSim-1-screenshot-countTo9.png>

--------------------------------------------------  
<br>

Acknowledgment:  
This project was inspired by:  
https://github.com/freedosproject/toycpu  
Thank you, but I needed something even simpler.  
