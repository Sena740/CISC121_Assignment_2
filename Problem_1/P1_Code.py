def solution(A): 
    if not A:                 # Check if the list is empty
        return 0 
    else: 
        return len(set(A))    # Use set to get unique elements and return the length of the set
