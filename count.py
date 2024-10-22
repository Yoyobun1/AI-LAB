# write a python program to find the number of occurrences of a character in a string

class Occur:
    
    def __init__(self):
        self.dict = {}
    
    def count(self, expression):
        for i in expression:
            if i not in self.dict:
                self.dict[i] = 1
            else:
                self.dict[i] += 1
        for keys, values in self.dict.items():
            print(f"{keys} occurs {values} times")
            
            
if __name__ == "__main__":
    
    occ = Occur()
    exp = input("Enter any expression:").replace(" ", "")
    occ.count(exp)