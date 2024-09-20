from hungarian import *

# create correct example data
cost_matrix = np.random.randint(0, 100, size=(100, 100)) 
a=hungarian(cost_matrix)

# usage example: how to get the result
print('total cost: ', a.result().total_cost)
for row, col in a.result().matching:
    print(f'row {row} and column {col} is matched')
    
#error example 1: wrong type
b=hungarian([[1,2],[3,4]])

#error example 2: wrong shape
ex1 = np.random.randint(0, 100, size=(4, 5)) 
c=hungarian(ex1)

#error example 3: wrong dimension
ex2 = np.random.randint(0, 100, size=(4, 5, 6))
d=hungarian(ex2)