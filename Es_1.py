import pandas as pd
from itertools import islice
import matplotlib.pyplot as plt


def pretty_print(KeyWord, Value):
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print(KeyWord)
    print(Value)
    print("__________________________________________________________________________________________________________________________________________________")


serieA = pd.read_csv("Es1_tabella.csv")

Team = "Milan"
TeamMatches = serieA.loc[(serieA.HomeTeam == Team) | (serieA.AwayTeam == Team)].copy()

#Selecting all the matches of a Team
pretty_print(f"All {Team} matches 2018/19",TeamMatches)

maxHomeShots = TeamMatches[["HS"]][(TeamMatches.HomeTeam == Team)].max()
maxAwayShots = TeamMatches[["AS"]][(TeamMatches.AwayTeam == Team)].max()

maxShots = max(maxHomeShots[0],maxAwayShots[0])
#print(maxShots)

matchesWithMostShots = TeamMatches[((TeamMatches.HomeTeam == Team) & (TeamMatches.HS == maxShots)) | ((TeamMatches.AwayTeam == Team) & (TeamMatches.AS == maxShots))]

pretty_print(f"{Team}'s matches with most shots on target ({maxShots} shots)",matchesWithMostShots)


#Selecting the matches with the most shots on target

points_column=[0]

firstRow = TeamMatches.head(1)


if(firstRow["FTR"].iloc[0] == "D"):
    points_column[0]+=1
elif(firstRow["FTR"].iloc[0] == "H" and firstRow["HomeTeam"].iloc[0] == Team):
    points_column[0]+=3
elif(firstRow["FTR"].iloc[0] == "A" and firstRow["AwayTeam"].iloc[0] == Team):
    points_column[0]+=3
    
i=1
for index,row in islice(TeamMatches.iterrows(),1,None):
    if(row["FTR"] == "D"):
        points_column.append(points_column[i-1]+1)
    elif(row["FTR"] == "H" and row["HomeTeam"] == Team):
        points_column.append(points_column[i-1]+3)
    elif(row["FTR"] == "A" and row["AwayTeam"] == Team):
        points_column.append(points_column[i-1]+3)
    else:
        points_column.append(points_column[i-1])
    i+=1



#adding points column
newSeries = pd.Series(points_column)
TeamMatches['PTS'] = newSeries.values

#print(TeamMatches)
TeamMatches.plot(kind = "line", x="Date", y="PTS")

plt.show()

prevPoints = 0
maxStreak = 0
currentStreak = 0


for index, value in TeamMatches["PTS"].items():
    if (prevPoints+3 == value):
        currentStreak += 1
        
    else:
        if (currentStreak > maxStreak):
            maxStreak = currentStreak
            currentStreak = 0
        else:
            currentStreak = 0
    prevPoints = value 

pretty_print(f"{Team}'s longest winnin streak",maxStreak)
    
