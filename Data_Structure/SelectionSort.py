# SelectionSort.py
# 맨 뒷자리로 큰수를 이동시켜 정렬

def selectionSort2(A):
    for last in range(len(A)-1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]
    return A

def theLargest(A, last):
    Largest = 0
    for i in range(last+1):
        if A[i] > A[Largest]:
            Largest = i      
    return Largest


if __name__ == '__main__':
    unsorted = [5, 2, 1, 4, 3]
    unsorted_ = unsorted.copy()
    
    sorted_ = selectionSort2(unsorted)

    print(unsorted_)
    print('---------------')
    print(sorted_)