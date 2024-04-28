# Python Challenge Readme

## Pybank:
I had a lot of trouble creating a path to the pybank csv file, and had trouble getting my code to read the file as I thought it was actually an excel file, so I asked xpert how to solve this. I eventually figured out the budget_data file really was a csv file, but xpert did help me troubleshoot and create a code to go to the correct file path.

Although I remember doing this in class, I was unsure how to do this at first when I thought the resources file had an excel file. This is the script that xpert gave me when I was still tring to figure out what file path to use:
reader = csv.reader(csvfile)
    next(reader) (forgot how to skip the first row in a csv file)

When I received some errors running my code, xpert had me convert int to str in the print function, so that it could concatenate the month count in the financial analysis.

Xpert also reminded me about using column index to find the sum of the second column, and how to put column index into the function to find the sum correctly. However, I decided later on to just put " for row in reader: month_count += 1" into my code, as I knew that every row (except for the header row) had a month assigned to it. This is also something xpert helped me with.

Along with the help that has been documented thus far, I also got help from xpert with finding the sum of the values in the second bullet point in the instructions. Xpert recommended that I use "float" type variables, along with recommending that I initialize the maximum change and the minimum change in profits with negative infinity and infinity, respectively. While I also had a pretty good idea on how to find the maximum and minimum in this part, there were some errors that xpert helped me refine, and it also helped me find the right location to put this code. This is the code that xpert gave me, which I ended up using. "if previous_profit != 0:
            change = profit - previous_profit
            changes.append(change)
            if change > max_change:
                max_change = change
            if change < min_change:
                min_change = change
        previous_profit = profit"

This code was also given to me by xpert, but I had pretty much already calculated this in my own code. I ended up using this one instead, as creating more variables was confusing and this one was overall more readable. "average_change = sum(changes)/len(changes)"

Lastly, when writing the code that would make an output text file with the results, I found a post on reddit that was asking how to do this correctly. In the comments, I found this code "f = open("output.txt", "w")
"# and now you use print like before but with a file parameter:"
print(..., file=f)" in one of the comments. 
Here is the link to the post that I got this information from. https://www.reddit.com/r/learnpython/comments/12emhsa/how_do_i_save_the_output_of_the_python_code_as_a/

I would also like to note, just for transparency, that xpert helped me with general calculations and helping me identify other errors in my code, such as where in the code to put calculations to prevent the code from making mistakes. 

## Pypoll

I was able to work more independently on this second part of the project, but I still got the following help: 

I had an idea of how to assign the candidate names to values, but had trouble making sure each value didn't end up being the same name as the others. I had xpert help refine my code to keep the candidate names separate from the others. unique_candidates = set() 
candidate_votes[voter_id] += 1
        else: candidate_votes[voter_id] = 1           
"Voter_id" Does not actually represent the voter id's in the first column of this dataset. This variable was just created to represent the names of the candidates. THis is the code that I ended up with for finding the unique candidate names. 
if voter_id not in unique_candidates:
            unique_candidates.add(voter_id)
            if cand1 is None:
                cand1 = voter_id
            elif cand2 is None:
                cand2 = voter_id
            elif cand3 is None:
                cand3 = voter_id
This code is also something that I started on my own, but turned to xpert for help when it assigned the same name to all of the candidates. I had created 3 "if" functions, but because they were separate, they all ended up doing the same thing. I had xpert's help to turn it to a singular "if" function, with "elif" statements.

totalvotes = sum(candidate_votes.values())   Another piece of code that xpert helped with, for finding the sum of the votes that each candidate received, as my original code wasn't correctly calculating this.

Xpert helped convert "print(str(cand3) + ": " + {str((cand3_votes/vote_count) * 100).2f} + "%  ("+ str(cand3_votes) + ")")", which was my original code, to "print(f"{cand3}: {(cand3_votes/vote_count) * 100:.2f}%  ({cand3_votes})")"

I was unsure how to assign the amount of votes that each candidate received correctly, so xpert gave me this function that I used for all candidates. cand1_votes = candidate_votes.get(cand1, 0)

This function was also something xpert helped me with. Although I had developed a similar one on my own, I chose to use this one to simplify the script. totalvotes = sum(candidate_votes.values())

A function that xpert suggested before I had gotten to this part of the instructions, which I ended up using. winner = max(candidate_votes, key=candidate_votes.get)

I used the same help from reddit to create the analysis output text file.

Along with that, I also used the script from pybank as a reference to start my code, which is why there are some similarities. This includes any help that I got from xpert for pybank, where it would be relevant for the pypoll code.
