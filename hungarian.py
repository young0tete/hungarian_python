import numpy as np

def checking_eli_idx (elimination_array, n):
    zero_indices = np.where(elimination_array == 0)[0]
    index_to_change = zero_indices[n]
    elimination_array[index_to_change] = 1

    return elimination_array

def find_one_to_one(coordinates):
    x_to_y = {}

    for x, y in coordinates:
        if x not in x_to_y:
            x_to_y[x] = y

    one_to_one_coordinates = [[x, y] for x, y in x_to_y.items()]

    return one_to_one_coordinates

class hungarian:
    def __init__(self, cost_matrix):
        self.cost_matrix=cost_matrix
        
        try:
            if not isinstance(self.cost_matrix, np.ndarray):
                raise TypeError('TypeError: The input type MUST BE np.ndarray.')
            elif len(self.cost_matrix.shape)!=2:
                raise TypeError('TypeError: The input MUST BE 2D.')
            elif self.cost_matrix.shape[0]!=self.cost_matrix.shape[1]:
                raise TypeError('TypeError: The size of row and column MUST BE identical.')
        except TypeError as e:
            print(e)
    
    def result (self):
        original_matrix=self.cost_matrix.copy()
        n=len(self.cost_matrix)
        # Step 1: Subtract the minimum element of each row
        for i in range(n):
            self.cost_matrix[i]=self.cost_matrix[i]-min(self.cost_matrix[i])
            
        # Step 2: Subtract the minimum element of each column
        for i in range(n):
            self.cost_matrix[:, i]=self.cost_matrix[:, i]-min(self.cost_matrix[:, i])
        
        while True:
            matrix=self.cost_matrix.copy()
            elimination=np.zeros(n*2, dtype=int)
            
            # Step 3: Remove zeros
            while True:
                rows, cols=matrix.shape
                
                row_cnt=np.array([np.sum(row == 0) for row in matrix])
                col_cnt=np.array([np.sum(matrix[:, i] == 0) for i in range(cols)])
                zero_cnt=np.concatenate((row_cnt, col_cnt))
                
                
                if max(zero_cnt)==0:
                    break
                elif np.argmax(zero_cnt)<rows:  # The maximum count of zeros is in the row
                    matrix = np.delete(matrix, np.argmax(zero_cnt), axis=0)
                    elimination=checking_eli_idx(elimination, np.argmax(zero_cnt))
                else: # The maximum count of zeros is in the column
                    matrix = np.delete(matrix, np.argmax(zero_cnt)-rows, axis=1)
                    elimination=checking_eli_idx(elimination, np.argmax(zero_cnt))
            
            # Step 4 or 5: Check if enough lines cover all zeros
            if sum(elimination)==n:
                break
            
            # Step 4: Adjust the matrix by subtracting the minimum uncovered value
            # Ensure that the matrix is not empty before computing the minimum
            if matrix.size > 0:
                m = np.min(matrix)
            else:
                break  # Exit the loop if the matrix becomes empty
        
            elim_rows, elim_cols=elimination[:n], elimination[n:]
            
            cal_mat=np.full((n, n), -m)
            cal_mat[elim_rows.astype(bool)]=0
            cal_mat[:, elim_cols.astype(bool)]=0

            for row in np.where(elim_rows == 1)[0]:
                for col in np.where(elim_cols == 1)[0]:
                    cal_mat[row, col]=m
            
            self.cost_matrix=self.cost_matrix+cal_mat
            
        
        # Step 5: Assignment
        zero_indices = np.argwhere(self.cost_matrix == 0)

        self.matching = find_one_to_one(zero_indices)

        # Calculate total cost
        self.total_cost=0
        for coordinate in self.matching:
            self.total_cost+=original_matrix[coordinate[0], coordinate[1]]

        return self