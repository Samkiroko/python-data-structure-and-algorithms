# # # def biggestNum(arr):
# # #     big_num = arr[0]
# # #     for index in range(1, len(arr)):
# # #         if arr[index] > big_num:
# # #             big_num = arr[index]
# # #         return big_num


# # arr = [56, 67, 89, 57, 99, 120]

# # # print(biggestNum(arr))


# # # def big(arr):
# # #     big_num = 0
# # #     for num in arr:
# # #         if num > big_num:
# # #             big_num = num
# # #     return(big_num)


# # # print(big(arr))

# # def findMax(arr, n):
# #     if n == 1:
# #         return arr[0]
# #     return max(arr[n-1], findMax(arr, n-1))


# # n = len(arr)

# # print(findMax(arr, n))


# import math
# # I am beginging by importing math, then will define newtons method
# # I will use an estimate
# # adding in a loop with a while statement
# # formatting is a key to getting the columns
# # using lib math, sqrt, abs value, with newtons
# # I also use the elif and then ask it to print.


# def newtons(n):
#     x = n / 2
#     i = 0
#     while i < 10:
#         y = (x + n / x) / 2  # newtons method
#         x = y
#         i += 1
#     return y


# def libmath(n):
#     return math.sqrt(n)


# def format(w):
#     w = str(w)
#     if len(w) > 3:
#         return w


# def printout():
#     for i in range(1, 26):
#         i = float(i)
#         n = str(newtons(i))
#         l = str(libmath(i))
#         ab = abs(newtons(i) - libmath(i))
#         if (len(n) or len(l)) == 3:
#             print(i, n, '         ', l, '          ', ab)
#         elif len(n) == 12:
#             print(i, n, '', l, ' ', ab)
#         else:
#             print(i, n, l, '', ab)


# printout()


from bigO import BigO
from bigO import algorithm

def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(array)