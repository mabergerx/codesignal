import numpy as np

def solution(a):
    team1 = a[::2]
    team2 = a[1::2]
    
    weight_team1 = np.sum(team1)
    weight_team2 = np.sum(team2)

    return [weight_team1, weight_team2]
