import sys
import itertools
n = int(input())
k = int(input())
cards = [sys.stdin.readline().strip() for _ in range(n)]
print(len(set("".join(i) for i in itertools.permutations(cards, k))))