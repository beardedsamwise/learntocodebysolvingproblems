# http://www.usaco.org/index.php?page=viewproblem2&cpid=855

def read_file(num_buckets, input_file):
    buckets_capacity = []
    buckets_volume = []
    for i in range(num_buckets):
        bucket = input_file.readline().split()
        buckets_capacity.append(int(bucket[0]))
        buckets_volume.append(int(bucket[1]))
    return buckets_capacity, buckets_volume

def write_file(output_file, bucket_volume):
    for milk in bucket_volume:
        milk = str(milk) + "\n"
        output_file.write(milk)

def mix_milk(num_buckets, num_pours, input_file, output_file):

    buckets_capacity, buckets_volume = read_file(num_buckets,input_file)

    for i in range(num_pours):

        # set source and destination buckets to pour to/from (the last bucket pours into the first)
        source_bucket = i % NUM_BUCKETS
        if not source_bucket == (NUM_BUCKETS - 1):
            dest_bucket = source_bucket + 1
        else:
            dest_bucket = 0

        # pour milk
        milk_to_pour = buckets_volume[source_bucket]
        available_volume = buckets_capacity[dest_bucket] - buckets_volume[dest_bucket]
        if available_volume >= milk_to_pour:
            buckets_volume[dest_bucket] = buckets_volume[dest_bucket] + milk_to_pour
            buckets_volume[source_bucket] = buckets_volume[source_bucket] - milk_to_pour
        else:
            buckets_volume[dest_bucket] = buckets_capacity[dest_bucket]  
            buckets_volume[source_bucket] = buckets_volume[source_bucket] - available_volume
    
    write_file(output_file, buckets_volume)

input_file = open('mixmilk.in', 'r')
output_file = open('mixmilk.out', 'w')
NUM_BUCKETS = 3
NUM_POURS = 100

mix_milk(NUM_BUCKETS, NUM_POURS, input_file, output_file)
