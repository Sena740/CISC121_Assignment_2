def solution(A):
    A.sort()                        # Sort the array in ascending order
    for i in range(len(A)-2):       # Check the triangle condition
        if A[i] + A[i+1] > A[i+2]:
            return 1                # A triangular triplet exists
    return 0                        # No triangular triplet found
