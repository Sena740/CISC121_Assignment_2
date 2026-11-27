def solution(A):
    for i in range(len(A)):     # Loop through the array
        A[i] = abs(A[i])        # Convert each element to its absolute value
    return len(set(A))          # Return the number of unique absolute values in the array
