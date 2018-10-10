def digitsToStrings(listOfDigits):
    listOfStrings = ['zero', 'one', 'two', 'three', 'four','five','six','seven','eight','nine']
    result = []

    for i in range(len(listOfDigits)):
        result.append(listOfStrings[listOfDdigitsToStrings[i]])

    return result

def stringsToDigits(inputStrings):
    dictionary = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    result = []

    for i in range(len(inputStrings)):
        result.append(dictionary[inputStrings[i]])
        
    return result