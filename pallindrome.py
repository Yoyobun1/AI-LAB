# program to check if a string is pallindrome or not

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        
    def palindrome(self, expression):
        for i in expression:
            self.stack.append(i)
        for i in range(len(expression)//2):
            # compare the popped item from stack to the current item in expression string
            if self.stack.pop() != expression[i]:
                return False
            
        return True
                                
        
if __name__ == "__main__":
    expression = input("Enter any string: ").lower().replace(" ", "")
    
    # Instantiate the stack and check if the string is a palindrome
    stk = Stack()
    if stk.palindrome(expression):
        print("It is a palindrome")
    else:
        print("Not a palindrome")