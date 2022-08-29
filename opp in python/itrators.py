from optparse import Values


class TopTen:
    def __init__(self) -> None:
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration



values = TopTen()


print(next(values))

for i in values:
    print(i)
















# nums = [7,8,9,5]

# for i in nums:
#     print(i)

# print()

# #itrators in python

# it = iter(nums)
# print(it.__next__())
# print(it.__next__())


# print()
# for i in nums:
#     print(i)