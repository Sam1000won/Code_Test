def solution(money):
    price_per_coffee = 5500
    max_cups = money // price_per_coffee
    remaining_money = money % price_per_coffee 

    return [max_cups, remaining_money]