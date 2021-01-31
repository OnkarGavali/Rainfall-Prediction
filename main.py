import pandas as pd
import numpy as np
import sklearn as sk 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# read csv from austin_final
data = pd.read_csv('austin_final.csv')

X = data.drop(['PrecipitationSumInches'],axis=1)

Y = data['PrecipitationSumInches']
Y = Y.values.reshape(-1,1)

#select randon day in data set

day_index = 798
days = [i for i in range(Y.size)]

clf = LinearRegression()
clf.fit(X,Y)
inp = np.array([[74], [60], [45], [67], [49], [43], [33], [45],[57], [29.68], [10], [7], [2], [0], [20], [4], [31]])
inp = inp.reshape(1,-1)

#print output

print('The precipitation in inches for the input is:',clf.predict(inp))

print('The precipitation trend graph: ')
plt.scatter(days , Y, color='g')
plt.scatter(days[day_index],Y[day_index],color='r')
plt.title('Precipitation level')
plt.xlabel('days')
plt.ylabel('Percipitation in inches')

plt.show()

x_f = X.filter(['TempAvgF','DewPointAvgF', 'HumidityAvgPercent',
                'SeaLevelPressureAvgInches', 'VisibilityAvgMiles',
                'WindAvgMPH'],axis=1)
print('Precipitation vs Selected Attribute Graph')
for i in range(x_f.columns.size):
    plt.subplot(3,2,i+1)
    plt.scatter(days,x_f[x_f.columns.values[i][:100]],color='g')
    plt.scatter(days[day_index],x_f[x_f.columns.values[i]][day_index],color='r')
    plt.title(x_f.columns.values[i])

plt.show()