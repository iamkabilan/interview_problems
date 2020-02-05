"""
This problem was recently asked by Twitter:
Given a matrix, transpose it. 
Transposing a matrix means the rows are now the column and vice-versa
"""

mat = [
    [1, 2, 3],
    [4, 5, 6],
]
new=[]
for i in range(len(mat[0])):
	new.append([])
	for j in range(len(mat)):
		val=mat[j][i]
		new[i].append(val)
print(new)