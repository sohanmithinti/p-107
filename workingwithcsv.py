import csv
from collections import Counter 

with open("height-weight.csv", newline="")as f :
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

height_list = []

for i in range(len(file_data)):
    num = file_data[i][1]
    height_list.append(float(num))           

n = len(height_list)
height_list.sort()

total = 0

for x in height_list:
    total = total + x

mean = total/n

print(mean)

if n%2 == 0:
    median1 = float(height_list[n//2])
    median2 = float(height_list[n//2-1])
    median = (median1 + median2)/2
else:
    median = float(height_list[n//2])    

print(median) 

newdata = Counter(height_list)

data_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0,
}

for height, occurance in newdata.items():
    if 50<float(height)<60: 
        data_range["50-60"] = data_range["50-60"] + occurance
    elif 60<float(height)<70: 
        data_range["60-70"] = data_range["60-70"] + occurance  
    elif 70<float(height)<80: 
        data_range["70-80"] = data_range["70-80"] + occurance      

modeRandge, modeOccurance = 0, 0

for range, occurance in data_range.items():
    if occurance > modeOccurance:
        modeRandge, modeOccurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance

mode = float((modeRandge[0] + modeRandge[1]) //2)

print(mode)