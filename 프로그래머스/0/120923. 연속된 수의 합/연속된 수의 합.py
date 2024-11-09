def solution(num, total):
    ans = total//num
    return [i for i in range(ans - (num-1)//2, ans+(num+2)//2)]