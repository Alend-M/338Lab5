import sys
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.items) == 0

def polish_notation(expression):
    
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
    }
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    stackOfNumbers = Stack()

    for value in reversed(expression.replace('(', ' ').replace(')', ' ').split()):
        if value in digits:
            stackOfNumbers.push(int(value))
        elif value in operators:
            x = stackOfNumbers.pop()
            y = stackOfNumbers.pop()
            result = operators[value](x,y)
            stackOfNumbers.push(result)
    
    print(f"Result {stackOfNumbers.pop()}")
    

# Test the function
polish_notation(sys.argv[1])
