import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_rows=9999
df= pd.read_csv('data.csv')
#print(df.to_string())
#print(df.head(10))
#print(df.tail(10))
df.plot()
plt.show()