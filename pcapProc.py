#!/usr/bin/python3

class PACKET:
    def __init__(self,order,time,source,destination,protocol,length):
        '''Packet initializer with attributes'''
        self.order = order
        self.time = time
        self.source = source
        self.destination = destination
        self.protocol = protocol
        self.length = length

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
        newList = []
        returnList=[]
        for i in range(len(self.container)-1):
            newList.append((int(self.container[i].length),self.container[i].source))
        someList = self.mergeSort(newList)
        for item in someList:
            returnList.append((item[1],item[0]))
        return returnList

    def sourceByBytes(self):
        '''Returns a list of tuples (source,totalBytes)'''
        someList=[]
        returnList=[]
        list = self.sourceByPackets()
        for item in list:
            if item[0] in self.dict:
                self.dict[item[0]]+=item[1]
            else:
                self.dict[item[0]]=item[1]
        for item in self.dict:
            someList.append((self.dict[item],item))
        someList=self.mergeSort(someList)
        for item in someList:
            returnList.append((item[1],item[0]))
        return returnList

    def protocolByPackets(self):
        '''Returns a list of tuples (protocol,numPackets)'''
        newList = []
        returnList=[]
        for i in range(len(self.container)-1):
            newList.append((int(self.container[i].length),self.container[i].protocol))
        someList = self.mergeSort(newList)
        for item in someList:
            returnList.append((item[1],item[0]))
        return returnList

    def connectionByPackets(self):
        '''Returns a list of tuples (source,destination,numPackets)'''
        newList = []
        returnList=[]
        for i in range(len(self.container)-1):
            newList.append((int(self.container[i].length),self.container[i].source, self.container[i].destination))
        someList = self.mergeSort(newList)
        for item in someList:
            returnList.append((item[1],item[2],item[0]))
        return returnList

    def connectionByBytes(self):
        '''Returns a list of tuples (source,destination,totalBytes)'''
        returnList=[]
        someList=[]
        list = self.connectionByPackets()
        for item in list:
            if str(item[0])+"{}"+str(item[1]) in self.dict:
                self.dict[str(item[0])+"{}"+str(item[1])]+=item[2]
            else:
                self.dict[str(item[0])+"{}"+str(item[1])]=item[2]
        for item in self.dict:
            splitSrcDest = item.split("{}")
            someList.append((self.dict[item],splitSrcDest[0],splitSrcDest[1]))
        someList= self.mergeSort(someList)
        for item in someList:
            returnList.append((item[1],item[2],item[0]))
        return returnList

'''Uncomment the code for testing'''
def main():
    PCtest = PCAP()
    PCtest.appendCSV('pcap.csv')
    # print(PCtest.sourceByPackets())
    # print(PCtest.sourceByBytes())
    # print(PCtest.protocolByPackets())
    # print(PCtest.connectionByPackets())
    print(PCtest.connectionByBytes())

main()

