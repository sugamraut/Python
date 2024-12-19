number=[1,4,7,8,15,20,35,45,55]
for i in number:
    if i>15:
        break
    else:
        print(i)

# Given sentence
sentence = "mariya mennen"

# Initialize counters for 'n' and 'm'
count_n = 0
count_m = 0

# Loop through each character in the sentence
for char in sentence:
    if char == 'n':
        count_n += 1
    elif char == 'm':
        count_m += 1

# Display the results
print(f"Count of 'n': {count_n}")
print(f"Count of 'm': {count_m}")

count=0
for i in range(1,6):
    count=count+1
    if count>2:
        break
    else:
        print(i)
else:
    print("Done")
