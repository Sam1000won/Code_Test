import sys

start, end = map(int, sys.stdin.readline().split()) 
lst = []
dic = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero"
}

for num in range(start, end+1):
    number = num
    num_to_string = ""

    while num > 0:
        num_to_string = dic[num % 10] + " " + num_to_string
        num //= 10

    lst.append([num_to_string.rstrip(), number])

lst.sort()

for i in range(len(lst)):
    print(lst[i][1], end=" ")

    if (i+1) % 10 == 0:
        print()
