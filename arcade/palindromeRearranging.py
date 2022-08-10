from collections import Counter


def palindromeRearranging(inputString):
    c = Counter(inputString).most_common()

    odd_counts = [count for letter, count in c if count % 2]

    return not len(odd_counts) > 1