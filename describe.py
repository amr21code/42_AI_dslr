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
	for i in range(len(df)):
		if not math.isnan(df[i]):
			count += 1
	return count

def mean(df, count):
	sum = 0.0
	for i in range(len(df)):
		if not math.isnan(df[i]):
			sum += df[i]
	return (sum / count)
	
def std(df, count, mean):
	sum = 0.0
	for i in range(len(df)):
		if not math.isnan(df[i]):
			sum += (df[i] - mean) ** 2
	return (math.sqrt(sum/(count - 1)))

def min(df):
	min = df[0]
	for i in range(len(df)):
		if not math.isnan(df[i]):
			if min > df[i]:
				min = df[i]
	return min

def max(df):
	max = df[0]
	for i in range(len(df)):
		if not math.isnan(df[i]):
			if max < df[i]:
				max = df[i]
	return max

def perc(df, mod, count, max):
	perc = sorted[round(mod * (count + 1))]
	# print(perc1)
	# perc2 = df[int(mod * (count + 1)) - 1]
	# print(perc2)
	# weight = (perc1 - perc2) * mod
	# print(weight)
	# perc = (perc1 + perc2) / 2 + weight
	return perc
	

data = np.full((8, 14), 0.0)
output = pd.DataFrame(data, columns=df.columns, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
countOfFeatures = len(df.columns)
for i in range(countOfFeatures):
	colName = df.columns[i]
	output[colName]['count'] = count(df[colName])
	output[colName]['mean'] = mean(df[colName], output[colName]['count'])
	output[colName]['std'] = std(df[colName], output[colName]['count'], output[colName]['mean'])
	output[colName]['min'] = min(df[colName])
	output[colName]['max'] = max(df[colName])
	output[colName]['25%'] = perc(df[colName], 0.25, output[colName]['count'], output[colName]['max'])
	# output[colName]['50%'] = perc(df[colName], 0.50, output[colName]['count'], output[colName]['max'])
	# output[colName]['75%'] = perc(df[colName], 0.75, output[colName]['count'], output[colName]['max'])


# print(df["Astronomy"].count())
# print(df.head())
print(input.describe())
# print(len(df))
# print(len(df.columns))
print("\nmine")
pd.options.display.float_format = "{:.6f}".format
print(output)
tableInfo = "\n[" + str(len(output)) + " rows x " + str(len(output.columns)) + " columns]"
print(tableInfo)

# print(df[colName])