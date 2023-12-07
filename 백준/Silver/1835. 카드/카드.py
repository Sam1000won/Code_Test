'''
힌트로 
2 1 4 3에서 2를 가장 뒤로 옮긴다. (1 4 3 2)
1을 책상 위에 옮겨놓는다. (4 3 2)
4 3 2 에서 4, 3을 뒤로 옮긴다. (2 4 3)
2를 책상 위로 옮겨놓는다. (4 3)
4 3 에서 가장 앞에 있는 것을 뒤로 3번 옮긴    다. (3 4)
3을 책상 위로 옮겨놓는다. (4)
4를 책상 위로 옮겨놓는다. (완료)

앞, 뒤 모두 삽입 삭제가 가능한 덱 자료구조를 활용하는 문제이다. 
n을 덱에 넣고, n부터 1까지 역순으로 반복하며 앞에 i를 appendleft한 뒤, 
맨 마지막 원소를 pop하여 또 다시 맨 앞으로 appendleft하는 과정을 i번 반복한다.

'''

from collections import deque

n = int(input())
d = deque()
d.append(n)

for i in range(n-1, 0, -1):
    d.appendleft(i)
    for j in range(i):
        d.appendleft(d.pop())

print(*d)
