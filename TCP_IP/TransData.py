def DataShift(data):
    byteSend = bytearray(data)
    for idx in range(len(byteSend)):
        #print(idx)
        byteSend[idx] = byteSend[idx] + 1
    return byteSend
