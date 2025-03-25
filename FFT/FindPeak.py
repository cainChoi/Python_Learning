def FindPeak(voltage):
    for idx in range(1,len(voltage) - 1):
        prevVal = voltage[idx - 1]
        nextVal = voltage[idx + 1]
        if(prevVal < voltage[idx] and voltage[idx] > nextVal) :
            return idx
    
    