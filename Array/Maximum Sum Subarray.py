Time: O(N)
Space: O(N)
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def max_Sum(arr):
	dp = [arr[0]]
	for i in range(1, len(arr)):
		dp.append(max(dp[-1] + arr[i], arr[i]))
	return max(dp)
print(max_Sum(arr))

Optimal

Time:O(N)
Space: O(1)

def max_Sum(arr):
	max_so_far = max_end = arr[0]
	for i in range(1, len(arr)):
		max_so_far = max(max_so_far + arr[i], arr[i])
		max_end = max(max_end, max_so_far)
	return max_end
print(max_Sum(arr))