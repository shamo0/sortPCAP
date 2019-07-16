#!/usr/bin/python3

class CAPTURE:
    def __init__(self,order,time,source,destination,protocol,length):
        self.order = order
        self.time = time
        self.source = source
        self.destination = destination
        self.protocol = protocol
        self.length = length

class PCAP:
    def __init__(self):
        # self.order = []
        # self.time = []
        # self.source = []
        # self.destination = []
        # self.protocol = []
        # self.length = []
        self.container = []

    def mergeSort(self,list):
        if len(list) <= 1 :
            return list
        else:
            listFirst = list[:len(list)/2]
            listSecond = list[len(list)/2:]
            listFirst = mergeSort(listFirst)
            listSecond = mergeSort(listSecond)
            list = merge(listFirst,listSecond)

    def appendCSV(self,filename):
        fd = open(filename,'r')
        file_read = fd.readline()
        while file_read!="":
            lineSplit = file_read.split(",")
            self.container.append(CAPTURE(lineSplit[0].strip("\""),lineSplit[1].strip("\""),lineSplit[2].strip("\""),lineSplit[3].strip("\""),lineSplit[4].strip("\""),lineSplit[5].strip("\"\n")))
            # self.order.append(lineSplit[0].strip('"'))
            # self.time.append(lineSplit[1].strip('"'))
            # self.source.append(lineSplit[2].strip('"'))
            # self.destination.append(lineSplit[3].strip('"'))
            # self.protocol.append(lineSplit[4].strip('"'))
            # self.length.append(lineSplit[5].strip('\"\n'))
            file_read = fd.readline()
        print(self.container)
    def sourceByPackets(self):
        ...
        # List = []
        # for item in self.source:
        #     List.append((item,self.length[self.source.index(item)]))


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
    # PCtest.sourceByPackets()



main()
