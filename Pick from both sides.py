def pick_arr(arr, b):
	nums = arr[:b]
	idxsum = sum(nums)
	maxsum = idxsum
	for i in range(b):
		remove = nums.pop()
		add = arr.pop()
		idxsum = idxsum - remove + add
		maxsum = max(maxsum, idxsum)
	return maxsum

print(pick_arr([5,-2,3,1,2], 3))
