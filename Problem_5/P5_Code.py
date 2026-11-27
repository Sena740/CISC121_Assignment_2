def solution(A):
    A.sort()
    s = 0                        # Start pointer
    l = len(A) - 1               # End pointer
    m = float('inf')

    while s <= l:
        t = A[s] + A[l]          # Calculate the sum of the two pointers
        m = min(m, abs(t))       # Update the minimum absolute sum
        if t > 0:                # If the sum is positive
            l -= 1               # Move the right pointer left
        elif t < 0:              # If the sum is negative
            s += 1               # Move the left pointer right
        else:
            return 0             # If the sum is zero, return 0 immediately

    return m
