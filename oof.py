import itertools
inversionCount = 0

# retrieve data from txt file
with open('input2.txt') as textFile:
    input = [line.split() for line in textFile][0]
    numberList = list(map(int, input))

# functions
def merge(firstHalf, secondHalf): 
  i = 0
  j = 0
  inversions = 0
  mergedList = []
  while i < len(firstHalf) and j < len(secondHalf):
    if firstHalf[i] < secondHalf[j]:
      mergedList.append(firstHalf[i])
      i+=1
    else: 
      mergedList.append(secondHalf[j])
      j+=1
      inversions+=len(firstHalf) - i
      print(inversions)

  # append leftover elements
  mergedList +=firstHalf[i:]
  mergedList +=secondHalf[j:]
  print(mergedList)
  return mergedList

def mergeSort(numberList):
  # base case: 
  if len(numberList) == 1: 
    return numberList
  else: 
    firstHalf = mergeSort(numberList[:int(len(numberList)/2)])
    secondHalf = mergeSort(numberList[int(len(numberList)/2):])
    
    return merge(firstHalf, secondHalf)
    
# def countInversions(list):


def main():
  print(mergeSort(numberList))
  # print(inversionCount)



main()
