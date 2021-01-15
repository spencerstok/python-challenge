import pandas as pd
import os
import csv
import time
import numpy as np

df = pd.read_csv("C://Users//antea//Desktop//python-challenge//PyPoll//Resources//Election_Data.csv")


TotalVotes = len(df)  
candidatedf = df.drop_duplicates(subset=['Candidate'], keep = 'last')

candidates = []
votes = []
VotePercents = []

for x in range(len(candidatedf)):
    candidate = str(candidatedf['Candidate'].iat[x])
    solodf = df[df.Candidate.str.contains(candidate)]
    
    votecount = len(solodf)
    candidates.append(candidate)
    votes.append(votecount)
    votePercent = round(((votecount/TotalVotes)*100), 2)
    VotePercents.append(str(votePercent)+"%")
    
votecolumns = ["Candidate", "Votes", "Vote %"]
voteinfodf = pd.DataFrame(list(zip(candidates, votes, VotePercents)), columns = votecolumns )


voteinfodf = voteinfodf.sort_values(by=["Votes"], ascending = False)



Message = ("Election Results\n\n" +
           "Total Votes: " + str(TotalVotes) +"\n"
            + str(voteinfodf["Candidate"].iat[0]) + " " + str(voteinfodf["Vote %"].iat[0]) +  " (" + str(voteinfodf["Votes"].iat[0]) + ")\n" 
            + str(voteinfodf["Candidate"].iat[1]) +  " " + str(voteinfodf["Vote %"].iat[1]) + " (" +  str(voteinfodf["Votes"].iat[1]) + ")\n" 
            + str(voteinfodf["Candidate"].iat[2]) +  " " + str(voteinfodf["Vote %"].iat[2]) + " (" +  str(voteinfodf["Votes"].iat[2]) + ")\n" 
            + str(voteinfodf["Candidate"].iat[3]) +  " " + str(voteinfodf["Vote %"].iat[3]) + " (" +  str(voteinfodf["Votes"].iat[3]) + ")\n\n"
            + "Winner: " + str(voteinfodf["Candidate"].iat[0]))
                                                                                         

print(Message)


file1 = open("Analysis/Election_Results.txt","w")#write mode 
file1.write(Message) 
file1.close() 
