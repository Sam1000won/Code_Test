import sys
input = sys.stdin.readline

dancer = int(input())
dance_mojige = {'ChongChong'}

for _ in range(dancer):
    first_dancer, dancer_01 = input().rstrip().split()
    
    if first_dancer in dance_mojige or dancer_01 in dance_mojige:
        dance_mojige.add(first_dancer)
        dance_mojige.add(dancer_01)

print(len(dance_mojige))
