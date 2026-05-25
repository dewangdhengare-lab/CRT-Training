# Q. Compute the nearest larger number by interchanging its digits updated. Given 2
# numbers a and b find the smallest number greater than b by interchanging the digits of
# a and if not possible print -1.
# . Input Format : 2 numbers a and b, separated by space.
# . Output Format: A single number greater than b. If not possible, print -1
# . Constraints: 1 <= a,b <= 10000000

# Explanation of the Examples:
# Example 1:
# Input:
# a=459
# b=500
# Permutations of 459:[459,495,549,594,945,954]
# Valid numbers greater than 500: [549,594,945,954]
# Smallest valid number:
# 549

# from itertools import permutations
# def generate_permutations(number):
# number_str = str(number)
# perm = permutations(number_str)
# perm_list =[".join(p) for p in perm]
# return perm_list
# # Example usage:
# number = 459
# permu = generate_permutations(number)
# print(permu)
from itertools import permutations
def generate_permutation(a,b):
    res = []
    number_str=str(a)
    perm = permutations(number_str)
    permList = [''.join(p) for p in perm]

    for i in range(permList):
        if i >=b:
            res.append(permList[i])
    for n in rnage
    return permList

if __name__=='__main__':
    print(generate_permutation(495))