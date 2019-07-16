#!/usr/bin/python3

class PACKET:
    def __init__(self,order,time,source,destination,protocol,length):
        self.order = order
        self.time = time
        self.source = source
        self.destination = destination
        self.protocol = protocol
        self.length = length

# class Process:
#     def __init__(self,key):
#         self.key = key
#
#     def __lt__(self, other) :
#         if self.key < other.key:
#             return True
#         return False

class PCAP:
    def __init__(self):
        self.container = []
        self.dict = {}

    def mergeSort(self,listFull):
        if (len(listFull) <= 1) :
            return listFull
        else:
            mid =len(listFull)//2
            LeftList = listFull[:mid]
            RightList = listFull[mid:]
            RightList = self.mergeSort(RightList)
            LeftList = self.mergeSort(LeftList)
            listFull = self.merge(listFull,LeftList,RightList)

    def merge(self,listFull,LeftList,RightList):
        m=n=k=0
        while (m < len(LeftList)) and (n<len(RightList)):
            if LeftList[m]<RightList[n]:
                listFull[k]=LeftList[m]
                m+=1
            else:
                listFull[k]=RightList[n]
                n+=1
            k+=1
        while (m < len(LeftList)):
            listFull[k] = LeftList[m]
            m+=1
            k+=1
        while (n < len(RightList)):
            listFull[k] = RightList[n]
            n+=1
            k+=1
        return listFull


    def appendCSV(self,filename):
        fd = open(filename,'r')
        file_read = fd.readline()
        while file_read!="":
            lineSplit = file_read.split(",")
            self.container.append(PACKET(lineSplit[0].strip("\""),lineSplit[1].strip("\""),lineSplit[2].strip("\""),lineSplit[3].strip("\""),lineSplit[4].strip("\""),lineSplit[5].strip("\"\n")))
            file_read = fd.readline()

    def sourceByPackets(self):
        newList = []
        for i in range(len(self.container)-1):
            # newList.append((self.container[i].source,self.container[i].length))
            newList.append((self.container[i].length))
        someList = self.mergeSort(newList)

    def sourceByBytes(self):
        ...

    def protocolByPackets(self):
        ...

    def connectionByPackets(self):
        ...

    def connectionByBytes(self):
        ...

def main():
    PCtest = PCAP()
    PCtest.appendCSV('test.csv')
    PCtest.sourceByPackets()



main()
