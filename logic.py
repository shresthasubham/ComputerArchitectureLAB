def AND(first,second):
     return first*second
def OR(first,second):
   return int(bool(first+second==1))
def NOT(first):
    if first==1:
        return 0
    else:
        return 1
def XOR(first,second):
    return first!=second
def NAND(first,second):
    return NOT(AND(first,second))
def NOR(first,second):
   return NOT(OR(first,second))