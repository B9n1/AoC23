### part 1
def readDocument(input_document):
    inputArray = []
    with open(input_document, 'r') as file:
        for line in file:
            line = line.strip('\n')
            inputArray.append(line)
    return inputArray

def getFirstValue(input):
    for char in input:
        if str.isdigit(char):
            return char

def getCalibrationValue(input):
    sum = 0
    for string in input:
        firstDigit = getFirstValue(string)
        lastDigit = getFirstValue(string[::-1])
        number = firstDigit + lastDigit
        sum += int(number)
    return sum
    

inputArray = readDocument('01_input')
calibrationValue = getCalibrationValue(inputArray)
print("The calibration value in part 1 is: " +  str(calibrationValue))

### part 2

def strToInt(string):
    string = string.replace("one", "on1e")
    string = string.replace("two", "tw2o")
    string = string.replace("three", "thre3e")
    string = string.replace("four", "fou4r")
    string = string.replace("five", "fiv5e")
    string = string.replace("six", "si6x")
    string = string.replace("seven", "sev7en")
    string = string.replace("eight", "eigh8t")
    string = string.replace("nine", "ni9ne")
    return string
def convertNumbersToStringInArray(array):
    return_array = []
    for string in array:
        return_array .append(strToInt(string))
    return return_array

partTwoIputArray = convertNumbersToStringInArray(inputArray)
calibrationValueTwo = getCalibrationValue(partTwoIputArray)
print("The calibration value in part 2 is: " +  str(calibrationValueTwo))