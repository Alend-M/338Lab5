import sys
def polish_notation(expression):
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
    }
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    stackOfNumbers = []

    for value in reversed(expression.replace('(', ' ').replace(')', ' ').split()):
        if value in digits:
            stackOfNumbers.append(int(value))
            print(stackOfNumbers)
        elif value in operators:
            x = stackOfNumbers.pop()
            y = stackOfNumbers.pop()
            result = operators[value](x,y)
            stackOfNumbers.append(result)
    
    print(f"Result {stackOfNumbers.pop()}")
    

# Test the function
polish_notation(sys.argv[1])
