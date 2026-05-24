'''
Rearrange positive and negative numbers:
o Question: Given an array containing both positive and negative numbers, rearrange them in an alternating fashion.
o Logic: Seperate positive and negative numbers, then merge them alternatively.
o Sample Input: [-1,2,-3,4,5,-6]
o Expected Output: [-1,2,-3,4,-6,5]
'''
def rearrange_alternate(arr):
    # Separate positive and negative numbers
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]

    # Merge alternatively
    result = []
    i = j = 0

    # Alternate until one list is exhausted
    while i < len(pos) and j < len(neg):
        result.append(neg[j])
        result.append(pos[i])
        i += 1
        j += 1

    # Append remaining elements (if any)
    result.extend(neg[j:])
    result.extend(pos[i:])

    return result


# Sample Input
arr = [-1, 2, -3, 4, 5, -6]
print(rearrange_alternate(arr))
