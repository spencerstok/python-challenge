import pandas as pd
import os
import csv
import time
import numpy as np


df = pd.read_csv("C://Users//antea//Desktop//python-challenge//PyBank//Resources//Budget_Data.csv")
df.insert(2, 'Change', df.shape[0]*[np.nan])

df["Profit/Losses"] = pd.to_numeric(df["Profit/Losses"])


for x in range(len(df) -1):
    x = x + 1
    df["Change"].iat[x] = float(df["Profit/Losses"].iat[x]) - float(df["Profit/Losses"].iat[x-1])
    

Months = len(df)
TotalPL = sum(df["Profit/Losses"])

AverageChg = round(df["Change"].mean(), 2)

MaxChg = df["Change"].max()
MinChg = df["Change"].min()

Maxdf = df.loc[df['Change'] == MaxChg]
MaxMonth = str(Maxdf["Date"].iat[0])

Mindf = df.loc[df['Change'] == MinChg]
MinMonth = str(Mindf["Date"].iat[0])


Message = ("Financial Analysis\n\n"+
           "Total Months: " + str(Months) +"\n"
            + "Total: $" + str(TotalPL) + "\n" 
            + "Average Change: $" + str(AverageChg) +"\n" 
            + "Greatest Increatse in Profits: " + str(MaxMonth) + " ($"+ str(MaxChg) +")\n"
            + "Greatest Decrease in Profits: " + str(MinMonth) + " ($"+ str(MinChg) + ")\n")

print(Message)


file1 = open("Analysis/myfile.txt","w")#write mode 
file1.write(Message) 
file1.close() 
