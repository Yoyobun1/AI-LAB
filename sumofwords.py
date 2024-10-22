# program to count number of words in a string
from collections import deque

class Stack:
    
    def __init__(self):
        self.stack = deque()
        
    def word_sum(self, expression):
        for i in expression:
            self.stack.append(i)
        return len(self.stack)
    
if __name__ == "__main__":
    stack = Stack()
    string = input("Enter any set of words: ").split()
    result = stack.word_sum(string)
    print("The number of words are: ",result)