# its all about comparing and swaping


def sort(nums):
    for i in range(len(nums)-1,0,-1 ):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j+1] = temp

                
nums = [5,2,4,15,7,8,19,7,54,3]

sort(nums)

print(nums)