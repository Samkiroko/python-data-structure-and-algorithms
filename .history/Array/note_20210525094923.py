from array import*

arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('d', [1.3, 1.5, 1.6])


# arr1.insert(6, 7)
# arr1.insert(0, 0)
# print(arr1, arr2)

def traverseArray(array):
    for i in array:
        print(i)


print(traverseArray(arr1))
