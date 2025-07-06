from math import comb

# Total players available in a typical IPL match (11 per team)
total_players = 22

# Select 11 players from 22
team_combinations = comb(total_players, 11)

# For each 11-player team, select 1 Captain and 1 Vice-Captain (must be different)
# 11 choices for Captain × 10 choices for Vice-Captain
captain_vc_combinations = 11 * 10

# Total combinations including Captain and Vice-Captain
total_combinations_with_cvc = team_combinations * captain_vc_combinations

print(total_combinations_with_cvc)
