"""
The problem to solve is the following: 2 to the power of fifteen is equal to 32768
and the sum of its digits is 26
what is the sum of the digits fo 2 to the one thousendth power
"""

numb = 1
for i in range(1000):
    numb = numb*2

print(numb)
digits = []

while numb > 0:
    digits.append(numb%10)
    numb = numb//10

total = 0
for j in range(len(digits)):
    total += digits[j]

print(total)