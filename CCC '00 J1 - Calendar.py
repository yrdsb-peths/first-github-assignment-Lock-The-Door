from array import array


inputStuff = input()
inputArray = inputStuff.split(' ')

# days of the week
print('Sun Mon Tue Wed Thr Fri Sat')

currentDay = 1

def getNextNumbers(numberOfNumbers):
    nList = [f"{i: 2d}" for i in range(currentDay, currentDay + numberOfNumbers + 1)]

# first line
print('    ' * inputArray[0] + getNextNumbers(6-inputArray[0]))