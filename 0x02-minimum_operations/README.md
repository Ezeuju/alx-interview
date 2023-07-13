0x02-minimum_operations
Table of Contents
0x02-minimum_operations
Table of Contents
Prime Factors
Why does this work?
Example
Prime Factors
This problem is easily solved (with math) by returning the sum of its prime factors. The prime factors of a number are the prime numbers that multiply together to make that number. For example, the prime factors of 12 are 2, 2, and 3. The prime factors of 15 are 3 and 5.

The prime factors of a number can be found by dividing the number by the smallest prime number that divides evenly into the number. For example, the smallest prime number that divides evenly into 12 is 2. 12 / 2 = 6. The smallest prime number that divides evenly into 6 is 2. 6 / 2 = 3. The smallest prime number that divides evenly into 3 is 3. 3 / 3 = 1. The prime factors of 12 are 2, 2, and 3.

Why does this work?
The reason why this can be solved with math is because ...

For every copy all operation, A new prime factor is initiated in the process, reduced by 1(for the copy operation), and then the number of paste operations increases as that prime factor decreases to zero.

Example
if we are given n as 12. We start dividing by the smallest prime number that divides evenly into 12.

H  # H = 1
So the first prime factor is 2. We copy all(H), and then paste 1 times. which is 2 operations. first prime is now 0.

HH  # H * 2
The second prime factor is 2 again. We copy all(HH), and then paste 1 times, which is 2 operations. second prime is now 0.

HHHH  # HH * 2
The third prime factor is 3. We copy all(HHHH), and paste 2 times which is 3 operations.

HHHHHHHHHHHH  # HHHH * 3
The sum total of operations is 7.

This is the same as the sum of the prime factors of 12. 2 + 2 + 3 = 7. This is the same for any number. The sum of the prime factors of a number is the same as the minimum number of operations to get to that number.

There are many cases where you are forced to copy all and keep pasting that same number until you reach the desired number. For example, if you are given n as 11. The prime factors of 11 are 11. So you have to copy all and paste 10 times. This is 11 operations. This is the same as the sum of the prime factors of 11. 11 = 11.