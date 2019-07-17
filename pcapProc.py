#!/usr/bin/python3
'''
      Author: Genadi Shamugia
       Alpha: 216126
        Date: July 16, 2019
Program Name: Sorting
Program Description:
    Program takes a pcap file and sorts it many different ways using object
    oriented programming in python3
'''

class PACKET:
    def __init__(self,order,time,source,destination,protocol,length):
        '''Packet initializer with attributes'''
        self.order = order
        self.time = time
        self.source = source
        self.destination = destination
        self.protocol = protocol
        self.length = length
        self.count=0

class PCAP:
    def __init__(self):
        self.container = []
        self.dict = {}

    def mergeSort(self,listFull):
        '''Merge sort of the list. Completed in O(nlog(n))'''
        if (len(listFull) <= 1) :
            return listFull
        else:
            mid =len(listFull)//2
            LeftList = self.mergeSort(listFull[:mid])
            RightList = self.mergeSort(listFull[mid:])
            return self.merge(LeftList,RightList)

    def merge(self,LeftList,RightList):
        m=n=k=0
        returnList= []
        while (len(returnList) < len(LeftList) + len(RightList)):
            if LeftList[m]<RightList[n]:
                returnList.append(LeftList[m])
                m+=1
            else:
                returnList.append(RightList[n])
                n+=1
            if m==len(LeftList) or n==len(RightList):
                returnList.extend(LeftList[m:] or RightList[n:])
        return returnList

    def appendCSV(self,filename):
        '''Appends packets from CSV formatted file to container of packets'''
        fd = open(filename,'r')
        file_read = fd.readline()
        if "Length" in file_read:
            file_read=fd.readline()
        while file_read!="":
            lineSplit = file_read.split(",")
            self.container.append(PACKET(lineSplit[0].strip("\""),lineSplit[1].strip("\""),lineSplit[2].strip("\""),lineSplit[3].strip("\""),lineSplit[4].strip("\""),lineSplit[5].strip("\"\n")))
            file_read = fd.readline()

    def sourceByPackets(self):
        '''Returns a list of tuples (source,numPackets)'''
        someList = []
        returnList=[]
        for i in range(len(self.container)-1):
            if self.container[i].source in self.dict:
                self.dict[self.container[i].source]+=1
            else:
                self.dict[self.container[i].source]=1
        for item in self.dict:
            someList.append((self.dict[item],item))
        someList=self.mergeSort(someList)
        for item in someList:
            returnList.append((item[1],item[0]))
        return returnList

    def sourceByBytes(self):
        '''Returns a list of tuples (source,totalBytes)'''
        newList = []
        returnList=[]
        someList=[]
        for i in range(len(self.container)-1):
            newList.append((int(self.container[i].length),self.container[i].source))
        list = self.mergeSort(newList)
        for item in list:
            if item[1] in self.dict:
                self.dict[item[1]]+=item[0]
            else:
                self.dict[item[1]]=item[0]
        for item in self.dict:
            someList.append((self.dict[item],item))
        someList=self.mergeSort(someList)
        for item in someList:
            returnList.append((item[1],item[0]))
        return returnList

    def protocolByPackets(self):
        '''Returns a list of tuples (protocol,numPackets)'''
        someList = []
        returnList=[]
        for i in range(len(self.container)-1):
            if self.container[i].protocol in self.dict:
                self.dict[self.container[i].protocol]+=1
            else:
                self.dict[self.container[i].protocol]=1
        for item in self.dict:
            someList.append((self.dict[item],item))

        someList = self.mergeSort(someList)
        for item in someList:
            returnList.append((item[1],item[0]))
        return returnList

    def protocolByBytes(self):
        '''Returns a list of tuples (protocol,totalBytes)'''
        newList = []
        returnList=[]
        someList=[]
        for i in range(len(self.container)-1):
            newList.append((int(self.container[i].length),self.container[i].protocol))
        list = self.mergeSort(newList)
        for item in list:
            if item[1] in self.dict:
                self.dict[item[1]]+=item[0]
            else:
                self.dict[item[1]]=item[0]
        for item in self.dict:
            someList.append((self.dict[item],item))
        someList=self.mergeSort(someList)
        for item in someList:
            returnList.append((item[1],item[0]))
        return returnList

    def connectionByPackets(self):
        '''Returns a list of tuples (source,destination,numPackets)'''
        someList = []
        returnList=[]
        for i in range(len(self.container)-1):
            if (str(self.container[i].source)+"{}"+str(self.container[i].destination)) in self.dict:
                self.dict[(str(self.container[i].source)+"{}"+str(self.container[i].destination))]+=1
            else:
                self.dict[(str(self.container[i].source)+"{}"+str(self.container[i].destination))]=1
        newList=[]
        for item in self.dict:
            splitSrcDest = item.split("{}")
            newList.append((self.dict[item],splitSrcDest[0],splitSrcDest[1]))
        newList= self.mergeSort(newList)
        for item in newList:
            returnList.append((item[1],item[2],item[0]))
        return returnList

    def connectionByBytes(self):
        '''Returns a list of tuples (source,destination,totalBytes)'''
        newList = []
        returnList=[]
        someList=[]
        list=[]
        for i in range(len(self.container)-1):
            newList.append((int(self.container[i].length),self.container[i].source, self.container[i].destination))
        someList = self.mergeSort(newList)
        for item in someList:
            if str(item[1])+"{}"+str(item[2]) in self.dict:
                self.dict[str(item[1])+"{}"+str(item[2])]+=item[0]
            else:
                self.dict[str(item[1])+"{}"+str(item[2])]=item[0]
        newList=[]
        for item in self.dict:
            splitSrcDest = item.split("{}")
            newList.append((self.dict[item],splitSrcDest[0],splitSrcDest[1]))
        newList= self.mergeSort(newList)
        for item in newList:
            returnList.append((item[1],item[2],item[0]))
        return returnList

'''Uncomment the code for testing'''
def main():
    PCtest = PCAP()
    PCtest.appendCSV('pcap.csv')
    # print(PCtest.sourceByPackets()) #this works
    # print(PCtest.sourceByBytes()) #this works
    # print(PCtest.protocolByPackets()) #this works
    # print(PCtest.protocolByBytes()) #this works
    # print(PCtest.connectionByPackets()) #works
    print(PCtest.connectionByBytes()) #this works
main()


