with open('file1.txt', mode='r') as file:
    data1 = file.readlines()
with open('file2.txt', mode='r') as file:
    data2 = file.readlines()
data1 = [dat.strip('\n') for dat in data1]
data2 = [dat.strip('\n') for dat in data2]

print(data1)
print(data2)


result = [item for item in data1 if (item in data2)]
print(result)