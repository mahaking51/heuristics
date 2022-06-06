import random
from main import *
jobsNumbers=[10,25,50,75,100]
rtDist=[[1,20],[1,30]]
ptDist=[[1,10],[1,15]]
sizeDist=[[4,10],[4,14]]
row=[]
address="job_data.csv"
def write_CSV(rows,fields,address):
    filename = address    
    with open(filename, 'w', newline='') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
            
        # writing the fields 
        csvwriter.writerow(fields) 
            
        # writing the data rows 
        csvwriter.writerows(rows)
def read_CSV():
    file = open('job_data.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    jobList=[]
    for row in csvreader:
        jobList.append(jobs(row[0],row[1],row[2],row[3]))
    return jobList
for l in range(len(jobsNumbers)):
    for o in range(10):
        
        for i in range(len(rtDist)):
            for j in range(len(ptDist)):
                for k in range(len(sizeDist)):
                    problem=[]
                    for m in range(jobsNumbers[l]):
                        problem.append([m+1,random.randrange(rtDist[i][0],rtDist[i][1]),random.randrange(ptDist[j][0],ptDist[j][1]),random.randrange(sizeDist[k][0],sizeDist[k][1])])
                    row.append(problem)
# print(row)
print(len(row))
for ele in row:
    writeCSV(ele,['name','pt','rt','size'],'all_data.csv')
    write_CSV(ele,['name','pt','rt','size'],address);
    jobList=read_CSV()
    lpt(jobList);
    mbwf(jobList);
    mbbf(jobList)
    hjs(jobList)
    mbff(jobList)
