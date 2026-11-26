def solution(A):
    A.sort()                   # Sort the array in ascending order
    L = A[-1] * A[-2] * A[-3]  # Product of three largest elements
    S = A[0] * A[1] * A[-1]    # Product of two smallest and the largest element
    R = max(L, S)              # Return the maximum of the two products
    return R
