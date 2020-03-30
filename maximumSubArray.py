def maxSubArray(nums, n):
        max_far, max_end = nums[0],nums[0]
        for i in range(1,len(nums)):
            max_end = max(nums[i], max_end+nums[i])
            max_far = max(max_far, max_end)
        print(max_far) 
a = [-7,-5,-6]
maxSubArray(a,len(a))