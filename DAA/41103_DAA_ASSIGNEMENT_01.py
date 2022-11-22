def iterative_fibonacci(n):
    a = 0
    b = 1
    c = 0
    if n < 0:
        return "Incorrect input"
    if n == 1:
        return b
    if n == 0:
        return a
    
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c
    
def recursive_fibonacci(n):
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

print(iterative_fibonacci(15))
print(recursive_fibonacci(12))