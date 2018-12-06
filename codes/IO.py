# save data to file
data = input("Data to write to file: ")
f= open("data.txt","w+")
f.write(data)
f.close()
# open file and read data
f=open("data.txt","r+")
rdata = f.read()
print("data from file: {}".format(rdata))

