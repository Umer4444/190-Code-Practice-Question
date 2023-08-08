def sortedSquaredArray(array):
    out = [0]*len(array)
    mint = 0 
    maxt = len(array) - 1
    i = len(array) - 1
    while mint <= maxt:
        if abs(array[mint]) > abs(array[maxt]):
            out[i] = array[mint] * array[mint]
            mint += 1
        else:
            out[i] = array[maxt] * array[maxt]
            maxt -= 1
        i -= 1
    return out
