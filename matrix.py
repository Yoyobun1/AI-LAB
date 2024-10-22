# program to find the sum of the diagonal and off diagonal of a matrix

class Matrix:
    
    def __init__(self):
        self.matrix = []
    
    def input_matrix(self, n):
        
        for i in range(n):
            self.matrix.append(list(map(int, input(f"Enter the elements of row {i}: ").split())))
        return self.matrix
            
    def sum_diagonals(self, n):
        
        # sum of diagonal
        diagonal_sum = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    diagonal_sum += self.matrix[i][j]
        
        return diagonal_sum            
                    
    def sum_off_diagonal(self, n):
        
        # off diagonal sum
        off_diagonal_sum = 0
        for i in range(n):
            j = n - 1 - i
            off_diagonal_sum += self.matrix[i][j]
  
        return off_diagonal_sum
        
        
if __name__ == "__main__":
    mat = Matrix()
    print("The number of rows must be equal to the number of columns of the matrix")
    n = int(input("Enter the size of the matrix: "))
    matrix =mat.input_matrix(n)
    
    diagonal = mat.sum_diagonals(n)
    print(f"sum of diagonals: {diagonal}")
    
    off_diagonal = mat.sum_off_diagonal(n)
    print(f"sum of off diagonals: {off_diagonal}")
        
        