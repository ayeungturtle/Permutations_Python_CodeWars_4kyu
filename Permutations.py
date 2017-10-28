def permutations(input):
    
    if (len(input) == 1):
        return1 = [input]
        return return1

    runningPermutationList = []
    tempPermutationList = []
    starter1 = input[0] + input[1]
    starter2 = input[1] + input [0]
    runningPermutationList.append(starter1)
    runningPermutationList.append(starter2)
    nextInsertIndex = 2
    numberOfPermutation = 1

    while (nextInsertIndex < len(input)):
        for i in range (0,len(runningPermutationList)):
            for j in range (0,len(runningPermutationList[i])+1):
                comboToAdd = StringInsert(runningPermutationList[i], j, input[nextInsertIndex])
                tempPermutationList.append(comboToAdd)
        
        runningPermutationList = []

        for i in range (0,len(tempPermutationList)):
            stringToAdd = tempPermutationList[i]
            runningPermutationList.append(stringToAdd)

        tempPermutationList = []
        nextInsertIndex += 1

    return list(set(runningPermutationList))  '''the set deletes duplicates'''

def StringInsert (parentString, insertLocation, thingToInsert):
    finalString = parentString[0:insertLocation] + thingToInsert + parentString [insertLocation:]
    return finalString
print (permutations('1234'))





    

