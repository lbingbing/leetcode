Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Note:
M=1000
D=500
C=100
L=50
X=10
V=5
I=1

Solution:
for each strictly increasing subsequent (longest as possible), its value equals to the last digit (largest) minus the sum of the rest digits.