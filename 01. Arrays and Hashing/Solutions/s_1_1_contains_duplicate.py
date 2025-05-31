def contains_duplicate_brute_force(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate_sort(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


def contains_duplicate_hash(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


nums = [1, 2, 3, 4, 5, 1]

print(contains_duplicate_brute_force(nums))  # True
print(contains_duplicate_sort(nums))         # True
print(contains_duplicate_hash(nums))         # True