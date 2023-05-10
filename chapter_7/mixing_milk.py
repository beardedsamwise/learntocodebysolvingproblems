# http://www.usaco.org/index.php?page=viewproblem2&cpid=855

input_file = open('mix_milk.in', 'r')
output_file = open('mix_milk.out', 'w')

NUM_BUCKETS = 3
NUM_POURS = 100

buckets_capacity = []
buckets_volume = []

for i in range(NUM_BUCKETS):
    bucket = input_file.readline().split()
    buckets_capacity.append(bucket[0])
    buckets_volume.append(bucket[1])

print(buckets_capacity)
print(buckets_volume)

# TO DO - create milk mixing function

# TO DO - call function

# TO DO - output results