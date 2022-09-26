for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
l = 0
r = len(matrix)-1
while(l < r):
    for k in range(len(matrix)):
        matrix[k][l], matrix[k][r] = matrix[k][r], matrix[k][l]
    l += 1
    r -= 1
