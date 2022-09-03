def solution(votes, k):
    highest_original_vote = max(votes)
    
    possible_votes = [vote + k for vote in votes]

    if k == 0 and len([vote for vote in votes if vote == highest_original_vote]) == 1:
        return 1
    
    possibles = [vote for vote in possible_votes if vote > highest_original_vote]
    
    return len(possibles)
