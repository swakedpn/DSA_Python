def insertion_sort(A: list):
    for i in range(len(A)):
        cur = A[i]
        j=i
        while j>0 and A[j-1]>cur:
            A[j] = A[j-1]
            j=j-1
        A[j] = cur
    print(A)

arr = [3,6,1,7]
insertion_sort(arr)
