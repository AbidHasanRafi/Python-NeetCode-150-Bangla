# Arrays and Hashing

## Problem 1: Contains Duplicate

**Description**
Given an integer array `nums`, return `True` if any value appears more than once in the array, and return `False` if every element is distinct.

---

## Examples

**Example 1**
Input: `nums = [1, 2, 3, 3]`
Output: `True`

**Example 2**
Input: `nums = [1, 2, 3, 4]`
Output: `False`

---

## Approach 1: Brute Force

```python
def contains_duplicate_brute_force(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```

**Explanation**
এই পদ্ধতিতে আমরা প্রতিটি উপাদানের জন্য তার পরবর্তী উপাদানগুলোর সাথে তুলনা করি। যদি কোনো দুটি উপাদান একসাথে মিলে যায়, তবে আমরা `True` রিটার্ন করি। যদি পুরো লিস্ট স্ক্যান করার পরও কোনো মিল না পাই, তাহলে `False` রিটার্ন করি। এই পদ্ধতির টাইম কমপ্লেক্সিটি হচ্ছে `O(n^2)` এবং এটি ছোট ইনপুটের জন্য কাজ করে, কিন্তু বড় ইনপুটে ধীরগতির হয়।

---

## Approach 2: Using Sorting

```python
def contains_duplicate_sort(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
```

**Explanation**
এই পদ্ধতিতে আমরা প্রথমে অ্যারেটি sort করি যাতে একই উপাদানগুলো পরপর থাকে। এরপর প্রতিটি উপাদান তার আগের উপাদানের সাথে তুলনা করি। যদি কোনো দুইটি উপাদান সমান হয়, তাহলে `True` রিটার্ন করি। না হলে `False` রিটার্ন করি। এই পদ্ধতির টাইম কমপ্লেক্সিটি `O(n log n)` যা আগের তুলনায় দ্রুত।

---

## Approach 3: Using Hash Table (Set)

```python
def contains_duplicate_hash(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Explanation**
এই পদ্ধতিতে আমরা একটি খালি `set` তৈরি করি এবং প্রতিটি উপাদানকে সেটিতে রাখার চেষ্টা করি। যদি কোনো উপাদান সেটিতে আগেই থাকে, তাহলে আমরা বুঝি এটি ডুপ্লিকেট এবং `True` রিটার্ন করি। অন্যথায়, সেটিতে উপাদানটি যোগ করি। এটি সবচেয়ে কার্যকর পদ্ধতি কারণ এটি `O(n)` সময়ে চলে এবং বড় ডেটার ক্ষেত্রেও দ্রুত কাজ করে।

---

## Summary

| Method      | Time Complexity | Space Complexity | Notes                       |
| ----------- | --------------- | ---------------- | --------------------------- |
| Brute Force | O(n²)           | O(1)             | Inefficient for large input |
| Sorting     | O(n log n)      | O(1)             | Faster than brute force     |
| Hash Table  | O(n)            | O(n)             | Most efficient overall      |