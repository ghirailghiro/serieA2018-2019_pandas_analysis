import pandas as pd
from itertools import islice
import matplotlib.pyplot as plt


serieA = pd.read_csv("Es1_tabella.csv")

Team = "Genoa"
resTot = serieA[(serieA.HomeTeam == Team) | (serieA.AwayTeam == Team)]

#Selecting all the matches of a Team
#print(resTot)

maxHomeShots = resTot[["HS"]][(resTot.HomeTeam == Team)].max()
maxAwayShots = resTot[["AS"]][(resTot.AwayTeam == Team)].max()

maxShots = max(maxHomeShots[0],maxAwayShots[0])
#print(maxShots)

matchesWithMostShots = resTot[((resTot.HomeTeam == Team) & (resTot.HS == maxShots)) | ((resTot.AwayTeam == Team) & (resTot.AS == maxShots))]

#print(matchesWithMostShots)
#Selecting the matches with the most shots on target

points_column=[0]

firstRow = resTot.head(1)

print(firstRow["FTR"].iloc[0])


if(firstRow["FTR"].iloc[0] == "D"):
    points_column[0]+=1
elif(firstRow["FTR"].iloc[0] == "H" and firstRow["HomeTeam"].iloc[0] == Team):
    points_column[0]+=3
elif(firstRow["FTR"].iloc[0] == "A" and firstRow["AwayTeam"].iloc[0] == Team):
    points_column[0]+=3
    
i=1
for index,row in islice(resTot.iterrows(),1,None):
    if(row["FTR"] == "D"):
        points_column.append(points_column[i-1]+1)
    elif(row["FTR"] == "H" and row["HomeTeam"] == Team):
        points_column.append(points_column[i-1]+3)
    elif(row["FTR"] == "A" and row["AwayTeam"] == Team):
        points_column.append(points_column[i-1]+3)
    else:
        points_column.append(points_column[i-1])
    i+=1

print(len(points_column))

#adding points column
resTot['PTS'] = points_column

#print(resTot)

resTot.plot(kind = "line",x="Date", y="PTS")

plt.show()

    
    


