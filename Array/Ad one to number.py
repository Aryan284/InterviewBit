nums = [1,7,8,9]
def add_one(nums):
	for i in range(n - 1, -1, -1):
		if nums[i] != 9:
			nums[i] += 1
			while nums[0] == 0:
				del nums[0]
			break
		else: nums[i] = 0
	nums.insert(0, 1)
	return nums
