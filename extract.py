import timeit
start = timeit.default_timer()

#1
import numpy as np
import pandas as pd

dataset = pd.read_csv('Basic_Arbiter_70000_simulation_data.csv', header=None)
df = dataset.iloc[:, :-1].values
pf = dataset.iloc[:,:].values
print(df.shape)
print(pf.shape)

def custom_phi(x):
	if(x%2==1):
		return -1
	else:
		return 1

rows = len(df)
columns = len(df[0])

print(rows, columns)
print(df)


for r in range(rows):
	# print(df[r])
	x = 0
	flag = 0
	for i in range(columns):
		if(df[r][i]==0):
			x=x+1
	# print(r, x, df[r][i], pf[r][i])
	for i in range(columns):
		if(df[r][i]==0):
			flag=1
		# pf[r][i] = custom_phi(x)
		if(flag==1):
			flag=0
			x=x-1
	# print(r, x, df[r][i], pf[r][i])

# pd.DataFrame(df).to_csv("extracted.csv")
# a = numpy.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
a = pf
np.savetxt("data/features.csv", a, delimiter=",")

#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start) 