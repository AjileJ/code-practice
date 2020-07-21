def arrayMaximalAdjacentDifference(inputArray):
    final = 0
    for item in range(len(inputArray) - 1):
        if inputArray[item] >= inputArray[item + 1]:
            greatest = inputArray[item]
            smallest = inputArray[item + 1]
        else:
            greatest = inputArray[item + 1]
            smallest = inputArray[item]
        if abs(greatest - smallest) >= final:
            final = greatest - smallest
    
    return final