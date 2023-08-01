import pandas as pd

trains = pd.read_excel("DataForPerceptron.xlsx", sheet_name="TRAINData")
xtrain = trains.iloc[:, 1:10].values
ytrain = trains.iloc[:, 10:11].values
xtrain_data = xtrain.tolist()
ytrain_data = ytrain.tolist()
tests = pd.read_excel("DataForPerceptron.xlsx", sheet_name="TESTData")
xtest = tests.iloc[:, 1:10].values
xtest_data = xtest.tolist()

for i in range (len(xtest_data)):
    xtest_data[i].append(1)

for i in range (len(xtrain_data)):
    xtrain_data[i].append(1)

alfa = 1
w = [1,1,1,1,1,1,1,1,1,1]

while True: 
    m = 0 
    
    for i in range (len(xtrain_data)):
        wt = []
        for k in range (len(xtrain_data[i])):
            wt.append(w[k] * xtrain_data[i][k])

        if sum(wt)<= 0 and ytrain_data[i][0] == 4:
            for k in range(len(xtrain_data[i])):
                w[k] = w[k] + (xtrain_data[i][k] * alfa)
                
            m += 1 

        elif sum(wt)>= 0 and ytrain_data[i][0] == 2:
            for l in range(len(xtrain_data[i])):
                w[l] = w[l] - (xtrain_data[i][l] * alfa)

            m -= 1
    
    if m == 0:
        break 

print(w)

ytest = []
for x in xtest_data :
    sum = 0
    for i in range(len(x)):
        sum += x[i] * w[i] 

    if sum <= 0 :
        ytest.append(2)

    elif sum > 0: 
        ytest.append(4)

tests["Class"] = ytest

with pd.ExcelWriter("DataForPerceptron.xlsx") as writer:
    trains.to_excel(writer, sheet_name='TRAINData', index=False)
    tests.to_excel(writer, sheet_name='TESTData', index=False)