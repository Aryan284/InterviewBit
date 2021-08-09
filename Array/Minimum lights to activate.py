A = [ 0, 0, 1, 1, 1, 0, 0, 1]
B = 3
 def solve(self, A, B):
    i = cnt = 0
    n = len(A)
    while i < n:
        flag = False
        j = min(i + B - 1, n - 1)
        while j >= i - B + 1 and j < n and j > 0:
            if A[j] == 1:
                flag = True
                i = j + B
                cnt += 1
                break
            j -= 1
        if not flag: return -1
    return cnt
print(solve(A, B))