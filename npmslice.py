import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print (arr[:4])
print(arr[4:])
print(np.median(arr))
print(np.mean(arr))
print(np.std(arr))

arr1=np.array([1,2,3,4,5])
x=arr1.copy()
arr1[0] = 42
print(arr1)
print(x)