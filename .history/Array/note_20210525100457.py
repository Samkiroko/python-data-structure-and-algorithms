from array import*

arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('d', [1.3, 1.5, 1.6])


# arr1.insert(6, 7)
# arr1.insert(0, 0)
# print(arr1, arr2)

def traverseArray(array):
    for i in array:  # O(n)
        print(i)  # O(1)


print(traverseArray(arr1))

# Time complexity O(n)


def accessElement(array, index):
    if index >= len(array):  # ------> O(1)
        print("There are non:")  # -----> O(1)
    else:
        print(array[index])  # ----> O(1)


accessElement(arr1, 6)

# Time complexity : O(1)
# space complexity: O(1)


def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The is no element in the array"


print(searchInArray(arr1, 2))
