# https://dmoj.ca/problem/ccc20j2

daily_infected = 0 # num of people infected daily
day = 0 # init number of days 
total_infected = 0 # init num of people infected 

target_infected = int(input()) # input target number of infected people
day_zero_infected = int(input()) # input number of people infected on day 0
ref = int(input()) # input ref number (number of people each person infects)

while total_infected <= target_infected: # run the loop until the number of people exceeds the target infected
    if day == 0:
        day = day + 1
        daily_infected =+ ref * day_zero_infected # number of people infected on this day
        total_infected = day_zero_infected + daily_infected # total number of people infected
    else:
        day = day + 1
        daily_infected =+ ref * daily_infected # number of people infected on this day
        total_infected = total_infected + daily_infected # total number of people infected

print(day)