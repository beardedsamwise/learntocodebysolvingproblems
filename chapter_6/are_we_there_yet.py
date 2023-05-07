# https://dmoj.ca/problem/ccc18j3

def process_distances(distances):
    distance_table = []
    for i in range(len(distances)):
        distance_table.append(process_city(i, distances))
    return(distance_table)

def process_city(city_index, distances):
    distance_list = []
    for i in range(len(distances)):
        distance_list.append(abs(distances[city_index] - distances[i]) + sum(distance_list))
    return(distance_list)

def print_table(results):
    for table in results:
        print(*table, sep=' ')

# Main Program

# gather input

distances = input().split(" ",)

distances = list(map(int, distances))

distances.insert(0,0)

# process input

results = process_distances(distances)

print_table(results)

