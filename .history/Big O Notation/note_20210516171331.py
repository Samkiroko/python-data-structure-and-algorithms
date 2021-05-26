# def biggestNum(arr):
#     big_num = arr[0]
#     for index in range(1, len(arr)):
#         if arr[index] > big_num:
#             big_num = arr[index]
#         return big_num


arr = [56, 67, 89, 57, 99, 120]

# print(biggestNum(arr))

big_num = 0
for num in arr:
    if num > big_num:
        big_num = num
print(big_num)
