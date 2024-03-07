import math, itertools

def solution(product):
        
    def prime_factors(n):
        factors = []
        # Divide by 2 to remove all even factors
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        # Divide by odd numbers starting from 3, up to square root of the number. We do it up to the square root of the number because any number above the square root would have another, smaller factor that we would have already seen before. The square root is kind of the mirror point of the factors. We only get odd numbers by having jump size of 2 in the range loop.
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        # If n is a prime number greater than 2
        if n > 2:
            factors.append(n)
        return factors
        
    if product == 0:
        return 10
    if product == 1:
        return 1

    factors = prime_factors(product)
    
    # Handle cases where a prime factor is greater than 7 (except 7 itself),
    # which automatically makes forming a valid product impossible.
    if any(factor > 7 for factor in factors):
        return -1
    
    # Initialize digit counts
    counts = {2: 0, 3: 0, 5: 0, 7: 0}
    
    # Count occurrences of each prime factor
    for factor in factors:
        if factor in counts:
            counts[factor] += 1

    # Prepare a new dictionary for final digit counts
    final_counts = {i: 0 for i in range(1, 10)}

    # Combine factors into digits
    # Calculate the count of 9s, 8s, 6s, and 4s based on available 2s and 3s
    final_counts[9] = counts[3] // 2
    counts[3] %= 2
    
    final_counts[8] = counts[2] // 3
    counts[2] %= 3

    # After maximizing 8s and 9s, check for 6s (one 2 and one 3)
    sixes = min(counts[2], counts[3])
    final_counts[6] = sixes
    counts[2] -= sixes
    counts[3] -= sixes

    final_counts[4] = counts[2] // 2
    counts[2] %= 2

    # Assign remaining 2s and 3s
    final_counts[2] = counts[2]
    final_counts[3] = counts[3]
    
    # Directly add counts for 5s and 7s, which cannot be combined further
    final_counts[5] = counts[5]
    final_counts[7] = counts[7]

    # Construct the final number from the digits, in ascending order
    result = ''.join(str(i) * final_counts[i] for i in range(1, 10))
    return int(result) if result else -1
    
    # # Directly handle if prime factors include any prime > 7 (other than 7 itself)
    # if any(factor > 7 for factor in factors if factor not in [2, 3, 5, 7]):
    #     return -1
        
    # def combine_factors(factors):
    #     # trivial_combination = "".join(factors)
    #     # current_smallest = int(trivial_combination)
        
    #     string_representation = "".join([str(factor) for factor in factors])
        
    #     # Intuitively, I think what should work is first reducing the amount of digits as much as possible. So when we find let's say 5 factors, so all trivial candidates are 5 digits long, we have to multiply the individual factors in such way that they "collapse" into smaller digits smaller than 10. So maybe we first reduce all the 2's into 8's, 6's, or 4's. Then we reduce the 3's into 6's and 9's, if there are more than 1, because that always benefits as, as it always removes a digit off the total count of digits in the answer.
        
    #     # We prioritize making 8's and 9's, and then 4's and 6's afterwards.
    #     # To reduce all 2's, let's first find the amount of 2's, then decide how many 8s, 6s, 4s, and 2's we can have.
    #     twos_in_combinations = len([i for i in string_representation if i == "2"])
    #     threes_in_combinations = len([i for i in string_representation if i == "3"])
    #     nines = int(threes_in_combinations / 2)
    #     eights = int(twos_in_combinations / 3)
        
    #     threes_after_nines = threes_in_combinations - nines * 2
    #     twos_after_eights = twos_in_combinations - eights * 3
        
    #     sixes = 0
        
    #     for two, three in zip(range(twos_after_eights), range(threes_after_nines)):
    #         sixes += 1
    #         twos_after_eights -= 1
    #         threes_after_nines -= 1
        
    #     fours = int(twos_after_eights / 2)
    #     remaining_twos = twos_after_eights - fours
        
        
    #     # Now to find all other factors that are not 2s or 3s.
    #     other_factors = [factor for factor in factors if factor not in [2, 3]]
        
    #     print("9: ", nines)
    #     print("8: ", eights)
    #     print("6: ", sixes)
    #     print("4: ", fours)
    #     print("3: ", threes_after_nines)
    #     print("2: ", remaining_twos)
    #     print("Other factors: ", other_factors)
        
    #     # Combing together all the final digits
    #     final_digit_list = []
    #     final_digit_list.extend(["9"]*nines)
    #     final_digit_list.extend(["8"]*eights)
    #     final_digit_list.extend(["6"]*sixes)
    #     final_digit_list.extend(["4"]*fours)
    #     final_digit_list.extend(["3"]*threes_after_nines)
    #     final_digit_list.extend(["2"]*remaining_twos)
    #     final_digit_list.extend([str(factor) for factor in other_factors])
        
    #     all_permutations = [int("".join(perm)) for perm in set(itertools.permutations(final_digit_list, len(final_digit_list)))]
        
    #     return min(all_permutations)
        
    # if product == 0:
    #     return 10
    # if product == 1:
    #     return 1
    # else:
    #     factors = prime_factors(product)
    #     return combine_factors(factors)
        
