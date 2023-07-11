# Small CPU created using the RISC-V standard

import struct
from op_codes import *

memory = [0b0] * 0x1000

def r32(addr):
        return struct.unpack("I", memory[addr:addr+4])[0]

# x0 is hardwired to the constant 0
# x32 contains the pc
reg = [0]*33

# Simple single cycled CPU
# Steps:

# 1 Instruction fetch
# Takes the current instruction in the register

# 2 Instruction decode
# DECODE BIT SCHEME(LITTLE ENDIAN)
# 0-6                  // OP CODE
# 7-11                 // RD
# 12-14                // Funct3
# 15-19                // RS1
# 20-24                // RS2
# 25-31                // Funct7

# Test add instruction 
# ----------------------------------------------------
# | 0000000 | 00001 | 00000 | 000 |  00010 | 0110011 |
# ----------------------------------------------------
# |   f7    |  rs2  |  rs1  |  f3 |    rd  |   op    |
# ---------------------------------------------------- 
#
instruction = 0b00000000000100000000000100110011

opcode = ((1<<7) - 1) & instruction
rd = (((1<<12) - (1<<7)) & instruction)>>7
funct3 = (((1<<15) - (1<<12)) & instruction)>>12
rs1 = (((1<<20) - (1<<15)) & instruction)>>15
rs2 = (((1<<25) - (1<<20)) & instruction)>>20
funct7 = (((1<<32) - (1<<25)) & instruction)>>25

print("OP: ", bin(opcode))
print("RD: ", bin(rd))
print("FUNCT3: ", bin(funct3))
print("RS1: ", bin(rs1))
print("RS2: ", bin(rs2))
print("FUNCT7: ", bin(funct7))
# 3 Execute

# <========== ADD DEMO ==========>
# TODO: move this to alu
if(opcode == 0b0110011 and funct3 == 0b000 and funct7 == 0000000):
        print("ADDITION")
        memory[rs1] = 0b1010
        memory[rs2] = 0b1010
        memory[rd] = memory[rs1] + memory[rs2]
        print(memory[rd])

# 4 Memory Access
# 5 Write back
