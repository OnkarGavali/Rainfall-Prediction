#import libraries
import pandas as pd
import numpy as np

# cleaning data
#
# read data in pandas dataframe
data = pd.read_csv("austin_weather.csv")

#print(data.columns)
# drop theunnecessary columns in the data
data = data.drop(['Events','SeaLevelPressureHighInches','SeaLevelPressureLowInches','Date'],axis=1)

data = data.replace('T',0.0)
data = data.replace('-',0.0)
#Save the to the csv file
data.to_csv('austin_final.csv')
