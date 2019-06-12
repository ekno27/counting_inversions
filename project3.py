import itertools
import math

# retrieve data from txt file
with open('input1.txt') as textFile:
    input = [line.split() for line in textFile][0]
    numberList = list(map(int, input))

# functions
def merge(firstHalf, secondHalf): 
  i = 0
  j = 0
  inversionCount = 0
  # merging into a final array
  while i < len(firstHalf) and j < len(secondHalf):
    if firstHalf[i] < secondHalf[j]:
      i+=1
    else: 
      # adding inversions
      j+=1
      inversionCount += (len(firstHalf) - i)
  return inversionCount

def countInversions(numberList):
  # base case: 
  if len(numberList) == 1: 
    return 0
  # creating inversion count algo using mergesort
  else:
    inversionCount = 0
    firstHalf = numberList[:int(len(numberList)/2)]
    secondHalf = numberList[int(len(numberList)/2):]
    inversionCount = countInversions(firstHalf)
    inversionCount += countInversions(secondHalf)
    inversionCount += merge(firstHalf, secondHalf)
    return inversionCount
    
# def countInversions(list):


def main():
  print(countInversions(numberList))


main()
