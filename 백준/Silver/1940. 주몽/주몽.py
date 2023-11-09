import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
li = sorted(list(map(int, input().split())))
left= 0
right = len(li) - 1
count = 0
while left < right:
    sum_num = li[left] + li[right]
    if sum_num < m:
        left += 1
    elif sum_num > m:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1
 
print(count)