# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
class jobs:
    def __init__(self,name,rt,pt,size):
        self.name=name
        self.rt=rt
        self.pt=pt
        self.size=size
class machines:
    def __init__(self,id,name,capacity,at):
        self.id=id
        self.name=name
        self.capacity=capacity
        self.at=at
file = open('data.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
jobList=[]
for row in csvreader:
    jobList.append(jobs(row[0],row[1],row[2],row[3]))
def readCSV():
    file = open('mcdata.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    mcList=[]
    for row in csvreader:
        mcList.append(machines(row[0],row[1],row[2],row[3]))
    mcList.sort(key=lambda x:int(x.at))    
    return mcList
def printJob(arr):
    for i in range(len(arr)):
        print(arr[i].name,arr[i].at);
def arrToStr(arr):
    st=",".join([str(i) for i in arr])
    return st
def writeCSV(rows,fields,address):
    filename = address    
    with open(filename, 'w', newline='') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
            
        # writing the fields 
        csvwriter.writerow(fields) 
            
        # writing the data rows 
        csvwriter.writerows(rows)
# how to do the lpt as the release time should also be considered
# assuming that the size of all the machine is greter than all the sizes of the RMDs
# How to solve for a situation when a job has to wait
def deleteElement(jobName,jobList):
    for i in jobList:
        if i.name==jobName:
            jobList.remove(i)
# mcList.sort(key=lambda x:int(x.at))
def mbbf(jobList):
    mcList=readCSV()
    numBatch=[0 for i in range(len(mcList))]
    l1=sorted(jobList,key=lambda x: x.rt)
    l2=sorted(jobList,key=lambda x: x.size, reverse=True)
    row=[]
    while(len(l1)>0):
        batch=[];
        pt=0;
        st=0;
        batch.append(l1[0].name)
        currName=l1[0].name
        batchSize=int(l1[0].size);
        pt=max(0,int(l1[0].pt));
        mcSize=int(mcList[0].capacity);
        st=max(st,int(mcList[0].at))
        deleteElement(currName,l1)
        deleteElement(currName,l2)
        for i in l2:
            if batchSize<mcSize and int(i.size)<=(mcSize-batchSize):
               batch.append(i.name)
               batchSize+=int(i.size)
               pt=max(int(i.pt),pt);
               st=max(st,int(i.rt))
               deleteElement(i.name,l1)
               deleteElement(i.name,l2)
        numBatch[int(mcList[0].id)-1]+=1;
        mcList[0].at=pt+st;
        bst=arrToStr(batch)
        row.append([mcList[0].id,numBatch[int(mcList[0].id)-1],bst,st,pt,st+pt]);
        mcList.sort(key=lambda x:int(x.at))
        if(batchSize>=mcSize):
            batch=[]
    fields=['machine','batch','jobs','starting time','processing time','completion time']
    writeCSV(row,fields,'output/mbbf.csv') 
    print(row)
def mbwf(jobList):
    l1=sorted(jobList,key=lambda x: int(x.rt))
    l2=sorted(jobList,key=lambda x: int(x.size))
    # printJob(l2)
    mcList=readCSV();
    numBatch=[0 for i in range(len(mcList))]

    row=[]
    while(len(l1)>0):
        batch=[];
        pt=0;
        st=0;
        batch.append(l1[0].name)
        currName=l1[0].name
        batchSize=int(l1[0].size);
        pt=max(0,int(l1[0].pt));
        mcSize=int(mcList[0].capacity);
        st=max(st,int(mcList[0].at))
        deleteElement(currName,l1)
        deleteElement(currName,l2)
        for i in l2:
            if batchSize<mcSize and int(i.size)<=(mcSize-batchSize):
               batch.append(i.name)
               batchSize+=int(i.size)
               pt=max(int(i.pt),pt);
               st=max(st,int(i.rt))
               deleteElement(i.name,l1)
               deleteElement(i.name,l2)
        numBatch[int(mcList[0].id)-1]+=1;
        mcList[0].at=pt+st;
        bst=arrToStr(batch)        
        row.append([mcList[0].id,numBatch[int(mcList[0].id)-1],bst,st,pt,st+pt]);
        mcList=sorted(mcList,key=lambda x:int(x.at))
        if(batchSize>=mcSize):
            batch=[]
    fields=['machine','batch','jobs','starting time','processing time','completion time']
    writeCSV(row,fields,'output/mbwf.csv') 
    print(row)
def mbff(jobList):
    mcList=readCSV()
    numBatch=[0 for i in range(len(mcList))]
    l1=sorted(jobList,key=lambda x: int(x.rt))
    row=[]
    batch=[]
    batchSize=0
    pt=0
    st=0
    mcSize=int(mcList[0].capacity)
    while(len(l1)>0):
        if int(l1[0].size)<=(mcSize-batchSize):
            batch.append(l1[0].name)
            pt=max(int(l1[0].pt),pt)
            st=max(st,int(l1[0].rt))
            batchSize+=int(l1[0].size)
            deleteElement(l1[0].name,l1)
        else:
            bst=arrToStr(batch)
            numBatch[int(mcList[0].id)-1]+=1;
            row.append([mcList[0].id,numBatch[int(mcList[0].id)-1],bst,st,pt,st+pt])
            mcList[0].at=pt+st;
            mcList.sort(key=lambda x:int(x.at))
            mcSize=int(mcList[0].capacity)
            pt=0
            st=0
            batchSize=0
            batch=[]
        # print(len(l1))
        # printJob(l1)
    bst=arrToStr(batch)
    numBatch[int(mcList[0].id)-1]+=1;
    row.append([mcList[0].id,numBatch[int(mcList[0].id)-1],bst,st,pt,st+pt])
    fields=['machine','batch','jobs','starting time','processing time','completion time']
    writeCSV(row,fields,'output/mbff.csv') 
    print(row)
def hjs(jobList):
    mcList=readCSV()
    numBatch=[0 for i in range(len(mcList))]
    l1=sorted(jobList,key=lambda x: int(x.size),reverse=True)
    row=[]
    batch=[]
    batchSize=0
    pt=0
    st=0
    mcSize=int(mcList[0].capacity)
    while(len(l1)>0):
        if int(l1[0].size)<=(mcSize-batchSize):
            batch.append(l1[0].name)
            pt=max(int(l1[0].pt),pt)
            st=max(st,int(l1[0].rt))
            batchSize+=int(l1[0].size)
            deleteElement(l1[0].name,l1)
        else:
            bst=arrToStr(batch)
            numBatch[int(mcList[0].id)-1]+=1;
            row.append([mcList[0].id,numBatch[int(mcList[0].id)-1],bst,st,pt,st+pt])
            mcList[0].at=pt+st;
            mcList.sort(key=lambda x:int(x.at))
            mcSize=int(mcList[0].capacity)
            pt=0
            st=0
            batchSize=0
            batch=[]
        # print(len(l1))
        # printJob(l1)
    bst=arrToStr(batch)
    numBatch[int(mcList[0].id)-1]+=1;
    row.append([mcList[0].id,numBatch[int(mcList[0].id)-1],bst,st,pt,st+pt])
    fields=['machine','batch','jobs','starting time','processing time','completion time']
    writeCSV(row,fields,'output/hjs.csv') 
    print(row)
def lpt(jobList):
    mcList=readCSV();
    numBatch=[0 for i in range(len(mcList))]
    l1=sorted(jobList,key=lambda x: int(x.pt),reverse=True)
    row=[]
    batch=[]
    batchSize=0
    pt=0
    st=0
    mcSize=int(mcList[0].capacity)
    while(len(l1)>0):
        if int(l1[0].size)<=(mcSize-batchSize):
            batch.append(l1[0].name)
            pt=max(int(l1[0].pt),pt)
            st=max(st,int(l1[0].rt))
            batchSize+=int(l1[0].size)
            deleteElement(l1[0].name,l1)
        else:
            bst=arrToStr(batch)
            numBatch[int(mcList[0].id)-1]+=1;
            row.append([mcList[0].id,numBatch[int(mcList[0].id)-1],bst,st,pt,st+pt])
            mcList[0].at=pt+st;
            mcList=sorted(mcList,key=lambda x:int(x.at))
            mcSize=int(mcList[0].capacity)
            pt=0
            st=0
            batchSize=0
            batch=[]
        # print(len(l1))
        # printJob(l1)
    bst=arrToStr(batch)
    numBatch[int(mcList[0].id)-1]+=1;
    row.append([mcList[0].id,numBatch[int(mcList[0].id)-1],bst,st,pt,st+pt])
    fields=['machine','batch','jobs','starting time','processing time','completion time']
    writeCSV(row,fields,'output/lpt.csv') 
    print(row)
    # mcList=mcTemp

lpt(jobList);
mbwf(jobList);
mbbf(jobList)
hjs(jobList)
mbff(jobList)
