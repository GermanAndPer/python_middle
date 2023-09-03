x = 1
y = 2
z = 3
n = 3


Permutations = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
p
#print(Permutations)

'''
Permutations = 
    [[i,j,k] 
        for i in range(x + 1) 
        for j in range(y + 1) 
        for k in range(z + 1)
          if i + j + k != n]

 [[0, 0, 0], 
  [0, 0, 1], 
  [0, 0, 2], 
  [0, 1, 0], 
  [0, 1, 1], 
  [0, 1, 3], 
  [0, 2, 0], 
  [0, 2, 2], 
  [0, 2, 3], 
  [1, 0, 0], 
  [1, 0, 1], 
  [1, 0, 3], 
  [1, 1, 0], 
  [1, 1, 2], 
  [1, 1, 3], 
  [1, 2, 1], 
  [1, 2, 2], 
  [1, 2, 3]]

'''

