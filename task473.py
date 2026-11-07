n, m = map(int, input().split())

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2 == 0:
            row.append('.')
        else:
            row.append('*')
    matrix.append(row)

for row in matrix:
    print(' '.join(row))