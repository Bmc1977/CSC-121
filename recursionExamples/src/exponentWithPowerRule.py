def exponentWithPowerRule(a, n):
    # Step 1: Determine the operations to be performed.
    print(f"------ {a} to the {n} ------")
    opStack = []
    while n > 1:
        if n % 2 == 0:
            # n is even
            opStack.append('square')
            print('square')
            n = n // 2
        elif n % 2 == 1:
            # n is odd
            n -= 1
            opStack.append('multiply')
            print('multiply')
    print("-------- now calculate --------")
    # Step 2: Perform the operations in reverse order.
    result = a # Start result at `a`
    while opStack:
        op = opStack.pop()

        if op == 'multiply':
            result *= a
            print(f"multiply by {a}->{result} ")

        elif op == 'square':
            result *= result
            print(f"square->{result} ")

    return result

print(exponentWithPowerRule(3, 6))
print(exponentWithPowerRule(10, 3))
print(exponentWithPowerRule(17, 10))
