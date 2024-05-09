import sys
input = sys.stdin.readline

def num_sort(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            if right == mid:
                break
            right = mid
    if nums[mid] == target:
        return mid
    else:
        return -1

n, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])

for i in range(m):
    d = int(input())
    result = num_sort(a, d)
    print(result)
