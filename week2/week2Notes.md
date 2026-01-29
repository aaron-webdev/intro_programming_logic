# Prog Log Wk 2

## Logic Gates
0 is false
1 is true
### AND
- requies both to output true

### OR
- requires only one to be tru to oupt put true

### NOT
- Inverts the input, ie: false will output true

### NAND
- If both outputs are true, the output will be fasle

### NOR
- outputs true only if both inputs are false

### XOR
- outputs true only if inputs are different

### XNOR
- outputs true if inputs are the same

## Number Systems

### Common NUmber Systems
- Base 10 (0-9); Counting
- Base 12 (0-11); Time
- Base 8 (0-7); Simplify Binary
- Base 16 (0-15,A-F); Hexadecimal
- Base 2 (0-1); Binary


### Converting Systems:
- Binary >> Base 10
    - multiply each bit by 2^n
    - 1010 in Binary is 10 in base 10
    - (1*2^3) + (0*2^2) + (1*2^1) + (0*2^0)

- Binary >> Hex
    - starting at the right most digit, group bits into fours.  Then convert each group into hex
    - 1010111110010 in binary is AF2 in Hex
    - 1010 1111 0010 >> AF2

- Base 10 >> Binary
    - divide the number by two and record the remainders
    - 10/2 = 5r0
    - 5/2 = 2r2
    - 2/2 = 1r0
    - 1/2 = 0r1
    - write the number from the bottom up this result is 1010

- Base 10 >> Hexadecimal
    - divide the mnumber by 16
    - record the remainders
    - convert remainders above 9 to A-F
    - right the new number from the bottom up
    - 254 base 10 >> hex
    -245/16 = 15r14 (14 is E)
    -15/16= 0r15 (15 is F)
    - result is FE

- Hex >> Base 10
    - multiply each digit by 16^n where n is the position from the right


### Practice Problems
1. 10110110 (2) >> Decimal and Hex
2. 7C (16) >> Binary and Decimal
3. 346 (10) Binary and Hex
4. 111100001111 (2) Hex and Decimal
5. 9A (16) Binary and Decimal