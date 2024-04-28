import os
import csv

vote_count = 0
unique_candidates = set()
cand1 = None
cand2 = None
cand3 = None
totalvotes = 0
candidate_votes = {}
with open("C:/Users/genna/Desktop/python-challenge/pypoll/resources/PyPoll/Resources/election_data.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        vote_count+= 1
        voter_id = str(row[2])
        totalvotes += 1
        if voter_id in candidate_votes:
            candidate_votes[voter_id] += 1
        else: candidate_votes[voter_id] = 1
        if voter_id not in unique_candidates:
            unique_candidates.add(voter_id)
            if cand1 is None:
                cand1 = voter_id
            elif cand2 is None:
                cand2 = voter_id
            elif cand3 is None:
                cand3 = voter_id
totalvotes = sum(candidate_votes.values())
winner = max(candidate_votes, key=candidate_votes.get)

cand1_votes = candidate_votes.get(cand1, 0)
cand2_votes = candidate_votes.get(cand2, 0)
cand3_votes = candidate_votes.get(cand3, 0)

with open("C:\\Users\\genna\\desktop\\python-challenge\\pypoll\\analysis\\analysis_output.txt", "a") as f:
    print("", file=f)
    print("Election Results", file=f)
    print("", file=f)
    print("------------------------------------------------------", file=f)
    print("", file=f)
    print("Total Votes: " + str(vote_count), file=f)
    print("", file=f)
    print("------------------------------------------------------", file=f)
    print("", file=f)
    print(f"{cand1}: {(cand1_votes/vote_count) * 100:.3f}%  ({cand1_votes})", file=f)
    print("", file=f)
    print(f"{cand2}: {(cand2_votes/vote_count) * 100:.3f}%  ({cand2_votes})", file=f)
    print("", file=f)
    print(f"{cand3}: {(cand3_votes/vote_count) * 100:.3f}%  ({cand3_votes})", file=f)
    print("", file=f)
    print("------------------------------------------------------", file=f)
    print("", file=f)
    print("Winner: " + winner, file=f)
    print("", file=f)
    print("------------------------------------------------------", file=f)
    print("", file=f)

print("")
print("Election Results")
print("")
print("------------------------------------------------------")
print("")
print("Total Votes: " + str(vote_count))
print("")
print("------------------------------------------------------")
print("")
print(f"{cand1}: {(cand1_votes/vote_count) * 100:.3f}%  ({cand1_votes})")
print("")
print(f"{cand2}: {(cand2_votes/vote_count) * 100:.3f}%  ({cand2_votes})")
print("")
print(f"{cand3}: {(cand3_votes/vote_count) * 100:.3f}%  ({cand3_votes})")
print("")
print("------------------------------------------------------")
print("")
print("Winner: " + winner)
print("")
print("------------------------------------------------------")
print("")