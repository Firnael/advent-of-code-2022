# Day 2
from utils.file_reader import read 
data = read(__file__)

# A & X : Rock
# B & Y : Paper
# C & Z : Scissors

outcomes = {
    "AX" : "draw", "AY" : "win", "AZ" : "lose",
    "BX" : "lose", "BY" : "draw", "BZ" : "win",
    "CX" : "win", "CY" : "lose", "CZ" : "draw"
}

outcome_scores = {
    "lose" : 0,
    "draw" : 3,
    "win" : 6 
}

def compute_match_result(a, b):
    # shape score + outcome score
    return { "X" : 1, "Y" : 2, "Z" : 3 }[b] + outcome_scores[outcomes[a+b]]

def compute_move_for_outcome(a, b):
    if b == "Z": # want a win
        return { "A" : "Y", "B" : "Z", "C" : "X" }[a]
    elif b == "X": # want a lose
        return { "A" : "Z", "B" : "X", "C" : "Y" }[a]
    # want a draw
    return { "A" : "X", "B" : "Y", "C" : "Z" }[a]

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