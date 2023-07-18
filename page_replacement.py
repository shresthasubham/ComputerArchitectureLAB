def FIFO():
    pageFrame = int(input("Insert Frame size : "))
    case = ""
    insertAt = 4
    hit=0
    refString = [2,3,2,1,5,2,4,5,3,2,5,2] #given input
    total=len(refString)
    cache = []
    print("Insert\t","Cache box\t","\tResult")
    for i in refString:
        if cache.count(i) > 0 :
            case = "\thit"
            hit=hit+1
        else:
            case = "\tmiss"
            if len(cache) < pageFrame : #frame not full
                cache.append(i)
            else: # Frame full
                cache[insertAt%pageFrame] = i
            insertAt += 1
        print (i,"\t",cache,"\t", case)
    ratio=hit/total
    print("Hit Ratio =",ratio)

def LRU():
    leastUsed = []
    cache = []
    case = ""
    #refString = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
    hit=0
    refString = [2,3,2,1,5,2,4,5,3,2,5,2] #given input
    total=len(refString)
    pageFrame = int(input("Input Frame size : "))
    print("Insert\t","Cache\t\t","Result\tLeast Used")
    for i in refString :
        if cache.count(i) > 0 :
            case = "hit "
            hit=hit+1
            leastUsed.remove(i)
            leastUsed.append(i)
        else:
            case = "miss"
            if len(cache) < pageFrame : #frame not full
                cache.append(i)
                leastUsed.append(i)
            else: # Frame full
                cache[cache.index(leastUsed[0])] = i
                leastUsed.pop(0)
                leastUsed.append(i)
        print (i,"\t",cache, "\t",case,"\t",leastUsed)
    rati=hit/total
    print("Hit Ratio =",rati)
if __name__ == "__main__":
   print("First In First Out\n")
   FIFO();
   print("\n\nLeast Frequently Used\n")
   LRU();

