# # REVERSE SOLUTION
# def reverse(strng):
#     if len(strng) <= 1:
#       return strng
#     return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])
# # IS PALINDROME SOLUTION
# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])
# # SOME RECURSIVE SOLUTION
# def someRecursive(arr, cb):
#     if len(arr) == 0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:], cb)
#     return True

# def isOdd(num):
#     if num%2==0:
#         return False
#     else:
#         return True
# # FLATTEN SOLUTION
# def flatten(arr):
#     resultArr = []
#     for custItem in arr:
#         if type(custItem) is list:
#             resultArr.extend(flatten(custItem))
#         else:
#             resultArr.append(custItem)
#     return resultArr


# def capitalizeFirst(arr):
#     resultArr = []
#     if len(arr) == 0:
#         return resultArr
#     resultArr.append(arr[0][0].upper() + arr[0][1:])
#     print(resultArr)
#     return resultArr + capitalizeFirst(arr[1:])


# print(capitalizeFirst(['car', 'girl', 'happy']))

# def nestedEvenSum(obj, sum=0):
#     for key in obj:
#         if type(obj[key]) is dict:
#             sum += nestedEvenSum(obj[key])
#         elif type(obj[key]) is int and obj[key]%2==0:
#             sum+=obj[key]
#     return sum
  
# def stringifyNumbers(obj):
#     newObj = obj
#     for key in newObj:
#         if type(newObj[key]) is int:
#             newObj[key] = str(newObj[key])
#         if type(newObj[key]) is dict:
#             newObj[key] = stringifyNumbers(newObj[key])
#     return newObj
  
# def collectStrings(obj):
#     resultArr = []
#     for key in obj:
#         if type(obj[key]) is str:
#             resultArr.append(obj[key])
#         if type(obj[key]) is dict:
#             resultArr = resultArr + collectStrings(obj[key])
#     return resultArr