#QuickSort

def quickSort(A, p:int, r:int):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
    return A
    

def partition(A, p:int, r:int) -> int:
    x = A[r]     #제일 마지막 원소
    i = p-1      #
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    print(f'Partitioning array from index {p} to {r}: {A}')
    print(f'Current pivot: {x}')
    print(f'Swapping {A[i+1]} and {A[r]}')
    print(f'Result: {A}\n')
    return i+1

if __name__ == '__main__':
    unsorted = [3, 8, 2, 4, 8, 77, 1, 2, 0, 5, 56, 28]
    sorted_ = quickSort(unsorted, 0, len(unsorted)-1)
    print('---------------------------')
    print('Sorted Array', sorted_)