# length is n's length
#each piece of message needs to be less than 

def preprocess(message, nLength):
    numArray = []
    #convert message to numbers
    for m in message:
        
        #symbols can also be converted        
        #all convert to capital letters which has only two digits
        m = m.upper()
        numArray.append(str(ord(m)))
        
    
    #truncate message to less than n's length
    #assume each item in the list length is two
    processed = []
    left = 0
    right = nLength // 2
    while right < len(numArray):
        #print(left)
        #print(right)
        processed.append(numArray[left: right])
        left = right 
        if 2 * right < len(numArray):
            right = left + nLength // 2 
        else:
            right = len(numArray)
    
    return processed

#print(preprocess("hello it is me", 5))