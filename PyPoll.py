# Add module dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total_votes variable and set equal to zero
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary for candidate votes.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the election with the reader function.
    file_reader = csv.reader(election_data)

    # Read and Omit the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Iterate through each row to add to the total_vote count
        total_votes += 1
        # Print/Retrieve the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # Initialize candidate_results variable
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    
        # Print out each candidate's name, vote count, and percentage of votes.
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate


    # Print out the winning candidate, vote count and percentage to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)








# The Beginning list of data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.