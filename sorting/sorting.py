def bubblesort(nums):
    l = len(nums)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if num[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]

def insertsort(nums):
    for i in range(1,n):
        j = i - 1
        while j >= 0:
            if nums[i] > nums[j]:
                num[j+1] = nums[j]
                j -= 1
            else:
                break
        nums[j+1] = nums[i]
        