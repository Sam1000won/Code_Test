def solution(n, k):
    total_cost = n * 12000
    total_cost += k * 2000
    free_drinks = n // 10
    total_cost -= free_drinks * 2000
    return total_cost
