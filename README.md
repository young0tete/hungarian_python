# hungarian_python
Hungarian algorithm module written in python using numpy for assignment problem.

# input
The input object must satisfy the following conditions.
1. the type of the object must be **np.ndarray**
2. the dimension of array must be **2D**
3. the array must be **square matrix**

# Usage Example
```pyton
from hungarian import *

# create example data
cost_matrix = np.random.randint(0, 100, size=(100, 100)) 
a=hungarian(cost_matrix)

# usage example: how to get the result
print('total cost: ', a.result().total_cost)
for row, col in a.result().matching:
    print(f'row {row} and column {col} is matched')
```
