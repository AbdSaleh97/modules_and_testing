def factorial_iterative(n):
    """
    Calculate the factorial of a non-negative integer n using iterative method.
    
    Args:
        n (int): The non-negative integer for which factorial is to be calculated.
        
    Returns:
        int: The factorial of n.
        str: "enter positive value" if n is less than 1.
    """
    res = 1
    if n == 1:
        return 1
    if n < 1:
        return "enter positive value"
    for i in range(1, n+1):
        res *= i
    return res

def factorial_rcursioun(n):
    """
    Calculate the factorial of a non-negative integer n using recursive method.
    
    Args:
        n (int): The non-negative integer for which factorial is to be calculated.
        
    Returns:
        int: The factorial of n.
        str: "Enter positive value" if n is less than 1.
    """
    if n < 1:
        return "Enter positive value"
    if n == 1:
        return 1
    else: 
        return factorial_rcursioun(n-1) * n
    
def clumsy(n):
    """
    Calculate the clumsy factorial of a non-negative integer n.
    
    Clumsy factorial is calculated as follows:
    For integers from n to 1, perform the following operations cyclically:
    - Multiply for the first operation
    - Divide for the second operation
    - Add for the third operation
    - Subtract for the fourth operation
    
    Args:
        n (int): The non-negative integer for which clumsy factorial is to be calculated.
        
    Returns:
        int: The clumsy factorial of n.
    """
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


class test:
    """
    A simple class for demonstration purposes.
    """
    variable = "blah"
    
    def call(self):
        """
        Print the value of the variable.
        """
        print(self.variable)
