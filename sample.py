# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         y = str(x)
#         print(y)
#         if y == y[::-1]:
#             print("true")
#         else: print("false")
s = int(input())
y = str(s)
if y == y[::-1]:
    print("t")
else: print('f')