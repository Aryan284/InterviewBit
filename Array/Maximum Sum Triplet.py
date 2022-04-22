from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1
def solve(A):
    n = len(A)
    right_max = [-1]*n
    maxi = A[-1]
    for i in reversed(range(n-1)):
        right_max[i] = maxi
        maxi = max(maxi, A[i])
    sk = []
    c = 0
    for i in range(n):
        if sk:
            while sk and sk[-1]>=right_max[i]:
                sk.pop()
            while sk and sk[-1] < A[i] and A[i]<right_max[i]:
                c = max(c , sk[-1] + A[i] + right_max[i])
                sk.pop()
        sk.append(A[i])
    return c 
    # n = len(A)
    # dp = [0] * n

    # dp[n - 1] = A[n - 1]

    # for i in range(n - 2, -1, -1):
    #     dp[i] = max(dp[i + 1], A[i])

    # list_ = []
    # max_ele = 0

    # list_.append(A[0])
    # for i in range(1, n-1):
    #     res = BinarySearch(list_, A[i])
    #     if(res!=-1):
    #         if dp[i + 1] <= A[i]:
    #             continue
    #         ans = list_[res] + A[i] + dp[i + 1]
    #         max_ele = max(max_ele , ans)

    #     list_.insert(res + 1, A[i])
    # return max_ele



if __name__=='__main__':
    A = [1,3,3]
    ans = solve(A)
    print(ans)
