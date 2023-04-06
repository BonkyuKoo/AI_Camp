#BucketSort

def bucket_sort(seq):
    buckets =  [[] for _ in range(len(seq))]
    for value in seq:
        bucket_index = value * len(seq) // (max(seq) + 1)
        buckets[bucket_index].append(value)

    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(quick_sort(bucket))
    return sorted_list


def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
    
if __name__ == '__main__':
    unsorted = [4, 2, 7, 3, 2, 6, 8, 9, 2, 3, 1]
    sorted = bucket_sort(unsorted)

    print(sorted)