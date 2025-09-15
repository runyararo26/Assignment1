import random

nums = [random.randint(1, 100) for _ in range(10)]
avg = sum(nums) / len(nums)
print("Numbers:", nums)
print("Average:", avg)