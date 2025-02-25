import pandas as pd
a=[1,2,3]
myvar=pd.Series(a,index=["x","y","z"])
print(myvar)

calories={"day1":420,"day2":380,"day3":390}
myvar1=pd.Series(calories,index=["day1","day2"])

print(myvar1)