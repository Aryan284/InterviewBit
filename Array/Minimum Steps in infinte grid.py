A = [0, 1, 1]
B = [0, 1, 2]
def path_grid(A, B):
	n = len(A)
	x, y = A[0], B[0]
	steps = 0
	for i in range(n):
	    dx = abs(x - A[i])
	    dy = abs(y - B[i])
	    steps += max(dx, dy)
	    x = A[i]
	    y = B[i]
	return steps
print(path_grid(A, B))