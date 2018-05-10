import csv
import matplotlib.pyplot as plt

# read and transpose.csv
with open('Test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    Challenges = []
    Champion = []
    Data = []
    i = 0
    for row in readCSV:
        if i < 1:
            i += 1
            continue
        if i == 1:
            Champion = row[1:]
            i += 1
        else:
            data = []
            for col in row[1:]:
                data.append(1 if col != '' else 0)
            Data.append(data)
            Challenge = row[0]
            Challenges.append(Challenge)

    m = len(Data)
    n = len(Data[0])
    results = [([0] * n) for i in range(n)]
    for j in range(0, n):
        for i in range(0, m):
            if Data[i][j] == 1:
                for k in range(j + 1, n):
                    if Data[i][k] == 1:
                        results[j][k] = results[j][k] + 1
                        results[k][j] = results[k][j] + 1
    print(results)

# Convert to .csv
fl = open('Output.csv', 'w')
writer = csv.writer(fl)
writer.writerow(['label1', 'label2', 'label'])
for values in results:
    writer.writerow(values)
fl.close()