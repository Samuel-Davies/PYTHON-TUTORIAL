# we go from start to end and find the min value
def sort(nums):
    for i in range(9):
        minPosition = i
        for j in range(i, 10):
            if nums[j] > nums[minPosition]:
                minPosition = j
            
        temp = nums[i]
        nums[i] = nums[minPosition]
        nums[minPosition] =temp


        print(nums) # this is to just display progress of the whole selection sort algorigthm



                
nums = [5,2,4,15,7,8,19,7,54,3]

sort(nums)

print(nums)