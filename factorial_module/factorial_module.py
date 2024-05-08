def factorial_iterative(n):
    res = 1
    if n == 1:
        return 1
    if n < 1:
        return "enter positive value"
    for i in range(1, n+1):
        res *= i
    return res

def factorial_rcursioun(n):
    if n < 1:
        return "Enter positive value"
    if n == 1:
        return 1
    else: 
        return factorial_rcursioun(n-1) * n
    
def clumsy(n):
    if n == 1:
        return 1
    stack = [n]
    current_op = 0  # Index to cycle through operations: 0 -> '*', 1 -> '/', 2 -> '+', 3 -> '-'

    for i in range(n - 1, 0, -1):
        if current_op == 0:  # Multiplication
            stack[-1] *= i
        elif current_op == 1:  # Division
            if stack[-1] < 0 and stack[-1] % i != 0:
                stack[-1] = stack[-1] // i + 1
            else:
                stack[-1] //= i
        elif current_op == 2:  # Addition
            stack.append(i)  # Push the next number onto the stack
        elif current_op == 3:  # Subtraction
            stack.append(-i)  # Push the negative of the next number onto the stack
        
        # Update current_op for the next iteration (cycle through 0, 1, 2, 3)
        current_op = (current_op + 1) % 4
    return sum(stack)

print(clumsy(13))