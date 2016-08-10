import random


#this python script will show many ways to sort an array and will only deal with internal sorating algorithms.

#--- Vars ---

#an array with no repeating values and only postive whole numbers
array = list(range(21))

#---- global functions ----
def isCorrect(arrayInput):
    if arrayInput == array:
        return True
    else:
        return False

def arrayShuffle(x):
     return random.sample(x, len(x))


#Bubble Sort

#--- Bubble functions ---

def swap (a, b, index, array):
    print ('index ' + str(index) + ' : a ' + str(a) + " : b " + str(b))
    array.insert(index, b)
    array.insert(index+1,a)
    array.pop(index+1)
    array.pop(index+2)
    
def sort(a, b, index, array):
    if a > b:
        swap(a, b, index, array)  
    return

def bubbleSort(bubbleArray):
    print(bubbleArray)
    unordered = True

    count = 0
    while unordered:
        for x in range(len(bubbleArray)-1):
            count = count + 1
            print('----------------------------------\n')
            sort(bubbleArray[x],bubbleArray[x+1], x, bubbleArray)
            print(bubbleArray)
            if isCorrect(bubbleArray):
                unordered = False
                break
    print('the bubble sort took ' + str(count) + ' turn to finish')


#Insertion Sort

#def insertionSort(array):
    #while unordered:
       # for x in range(len(bubbleArray)-1):
          

#Selection Sort

#HeapSport

#MergeSort

        
print(array)
bubbleSort(arrayShuffle(array))
#insertionSort(arrayShuffle(array))

