from math import ceil
from collections import defaultdict

def calculate_call_cost(total_minutes):
    basic_time = 100
    basic_fee = 10
    unit_time = 50
    unit_fee = 3

    if total_minutes <= basic_time:
        return basic_fee
    else:
        extra_time = total_minutes - basic_time
        extra_units = ceil(extra_time / unit_time)
        return basic_fee + extra_units * unit_fee

def convert_time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def main():
    n = int(input())
    call_records = [input().strip() for _ in range(n)]

    call_durations = defaultdict(int)

    for record in call_records:
        time_str, student_name = record.split()
        minutes = convert_time_to_minutes(time_str)
        call_durations[student_name] += minutes

    student_costs = [(name, calculate_call_cost(minutes)) for name, minutes in call_durations.items()]
    student_costs.sort(key=lambda x: (-x[1], x[0]))

    for student, cost in student_costs:
        print(f"{student} {cost}")

if __name__ == "__main__":
    main()