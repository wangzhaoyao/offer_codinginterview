class Queue:
    def __init__(self):
        self.stockA=[]
        self.stockB=[]
    def push(self, node):
        self.stockA.append(node)
    def pop(self):
        if self.stockB==[]:
            if self.stockA==[]:
                return None
            else:
                for i in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        return self.stockB.pop()

if __name__=='__main__':
    times=5
    testList=list(range(times))
    testQueue=Queue()
    for i in range(times):
        testQueue.push(testList[i])
    print(testList)
    for i in range(times):
        print(testQueue.pop(),',',end='')   #end=''可以让 print 输出不换行