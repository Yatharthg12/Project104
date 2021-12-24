import csv 
from collections import Counter
with open('HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader) 
    
file_data.pop(0)
newdata = []
for i in range(len(file_data)):
    n = file_data[i][1]
    newdata.append(float(n))

data = Counter(newdata)
mode = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height,occurance in data.items():
    if 50<float(height)<60:
        mode ["50-60"]+=occurance
    elif 60<float(height)<70:
        mode ["60-70"]+=occurance
    elif 70<float(height)<80:
        mode ["70-80"]+=occurance

mode_range,mode_occurance = 0,0
for range,occurance in mode.items():
    if occurance>mode_occurance:
        mode_range,mode_occurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance


m = float((mode_range[0]+mode_range[1])/2)
print("mode is", m)