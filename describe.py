import sys
import pandas as pd
import numpy as np
import math
from pandas.api.types import is_numeric_dtype

# try:
# 	dataset = sys.argv[1]
# 	input = pd.read_csv(dataset)
# except:
# 	print("no valid dataset supplied")


input = pd.read_csv('datasets/dataset_train.csv')
df = input

countOfFeatures = len(df.columns)
countOfData = len(df)
toDrop = []
for i in range(countOfFeatures):
	# print(is_numeric_dtype(df.loc[0][i]))
	if not is_numeric_dtype(df.loc[0][i]):
		toDrop.append(i)
df = df.drop(df.columns[toDrop], axis=1)

def count(df):
	count = 0.0
	print(df[20])
	for i in range(len(df)):
		if not math.isnan(df[i]):
			count += 1
	return count


data = np.full((8, 14), 0.0)
output = pd.DataFrame(data, columns=df.columns, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
countOfFeatures = len(df.columns)
for i in range(countOfFeatures):
	colName = df.columns[i]
	output[colName]['count'] = count(df[colName])


# print(df["Astronomy"].count())
# print(df.head())
print(input.describe())
# print(len(df))
# print(len(df.columns))
print(output)
tableInfo = "\n[" + str(len(output)) + " rows x " + str(len(output.columns)) + " columns]"
print(tableInfo)

# print(df[colName])