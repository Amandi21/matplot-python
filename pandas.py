import pandas as pd

data = {'x':[1,2,3,4,5], 'y':[2,4,6,8,10]}

# df = pd.DataFrame(data)

# print(df.loc[0])

df = pd.read_csv('example.csv')
print(df)
a = df.to_numpy()
a.reshape(2,5)
print(a)