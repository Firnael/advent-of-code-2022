# Day 2
from utils.file_reader import read 
data = read(__file__)

# A & X : Rock
# B & Y : Paper
# C & Z : Scissors

# - Total score = sum of rounds scores
# - Round score = score for the selected shape + score of outcome

shapes_pairs = { "X" : "A", "Y" : "B", "Z" : "C" }
outcomes = {
    "AY" : "win", "AZ" : "lose",
    "BX" : "lose", "BZ" : "win",
    "CX" : "win", "CY" : "lose",
}
shape_scores = { "X" : 1, "Y" : 2, "Z" : 3 }
outcome_scores = { "lose" : 0, "draw" : 3, "win" : 6 }
looking_for_outcome = { "X" : "lose", "Y" : "draw", "Z": "win" }

get_a_win = { "A" : "Y", "B" : "Z", "C" : "X" }
get_a_lose = { "A" : "Z", "B" : "X", "C" : "Y" }
get_a_draw = { "A" : "X", "B" : "Y", "C" : "Z" }

def compute_match_result(a, b):
    # get shape score
    score = shape_scores[b]
    # get outcome score
    if a == shapes_pairs[b]:
        score += outcome_scores["draw"]
    else:
        score += outcome_scores[outcomes[a+b]]
    return score

def compute_move_for_outcome(a, b):
    wanted_outcome = looking_for_outcome[b]
    if wanted_outcome == "win":
        return get_a_win[a]
    elif wanted_outcome == "lose":
        return get_a_lose[a]
    else: # want draw
        return get_a_draw[a]

scoreP1 = 0
scoreP2 = 0
for match in data:
    split = match.split(" ")
    a = split[0]
    b = split[1]
    # Part one
    scoreP1 += compute_match_result(a, b)
    # Part two
    move = compute_move_for_outcome(a, b)
    scoreP2 += compute_match_result(a, move)

print(f'Part ONE solution : ', scoreP1)
print(f'Part TWO solution : ', scoreP2)