f=open("demofile.txt","x")
f.write("Now the file has more content!!\n this same")
f.close()

f=open("demofile.txt","r")
print(f.read())