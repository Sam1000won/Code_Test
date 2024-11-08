import sys
from collections import deque
put = sys.stdin.readline

N = int(put())
S = put().strip()
Q = int(put())

while Q:
    Q -= 1
    l, r = map(int, put().split())

    s = S[l-1:r]

    left = deque(list(s[::-1]))
    right = deque()
    answer = {0}

    while len(left) > 1:
        right.appendleft(left.popleft())
        cnt = 0
        for i in range(min(len(left), len(right))):
            if left[i] == right[i]:
                cnt += 1
        answer.add(cnt)

    print(max(answer))