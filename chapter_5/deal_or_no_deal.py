# https://dmoj.ca/problem/ccc07j3

briefcases = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]

num_cases_opened = int(input())
opened_cases = []

for i in range(num_cases_opened):
    opened_case = int(input())
    opened_cases.append(briefcases[opened_case - 1])

offer = int(input())

for opened_case in opened_cases:
    briefcases.pop(briefcases.index(opened_case))

average_value = sum(briefcases) / len(briefcases)

if offer > average_value:
    print("deal")
else:
    print("no deal")