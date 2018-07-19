import pandas as pd
array = list(range(1, 10000001))

df = pd.DataFrame(array)
df.to_csv('people.csv', index=False, header=False)