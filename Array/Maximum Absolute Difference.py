# |A[i] - A[j]| + |i - j| can be written in 4 ways
# (A[i] + i) - (A[j] + j)
# -(A[i] - i) + (A[j] - j) 
# (A[i] - i) - (A[j] - j) 
# (-A[i] - i) + (A[j] + j) = -(A[i] + i) + (A[j] + j)


arr = [ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98 ]
def max_diff(arr):
    n = len(arr)
    max_Arr = [A[i] + i for i in range(n)]
    min_Arr = [A[i] - i for i in range(n)]
    return max(max(max_Arr) - min(max_Arr), max(min_Arr) - min(min_Arr))
