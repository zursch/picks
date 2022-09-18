#!/usr/bin/python3
import csv

picksDict = dict()
with open('picks.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    init = False
    # sort everything into a dic
    for row in spamreader:
        if init:
            row = row[0].split(',')
            picksDict[row[1]] = [row[0], row[2], row[3], row[4], row[5]]
        else:
            init = True

print("Team Rank SpreadLast LastTeamRank Vs Rank SpreadLast")
for row in picksDict:
    print(row + " " + str(picksDict[row][0]) + " " + str(int(picksDict[row][2]) - int(picksDict[row][3])) + " " + picksDict[picksDict[row][1]][0] + " " + picksDict[row][4] + " " + str(picksDict[picksDict[row][4]][0]) + " "  + str(int(picksDict[picksDict[row][4]][2]) - int(picksDict[picksDict[row][4]][3])) + " " + picksDict[picksDict[picksDict[row][4]][1]][0])
