def minOperations(n):
    if n <= 1:
        return 0
    
    f_number = 0
    s_number = 2
    
    while n > 1:
        if n % s_number == 0:
            n //= s_number
            f_number += s_number
        else:
            s_number += 1
    
    return f_number

