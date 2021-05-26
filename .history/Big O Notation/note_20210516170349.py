def biggestNum(arr):
    big_num = arr[0]
    for index in range(1, len(arr)):
        if arr[0] < arr[index]:
            big_num = arr[index]
        return big_num


arr = [56, 67, 89, 57, 99, 120]

print(biggestNum(arr))
