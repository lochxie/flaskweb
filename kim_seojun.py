# def solution(nums):
#     nums_plus = []
#     for i in range(len(nums)):
#         for j in range(i + 1,len(nums)):
#             plus = 0
#             plus = plus + nums[i] + nums[j]
#             nums_plus.append(plus)
#     for l in range(len(nums_plus)):
#         for a in range(1,101):
#             counted = nums_plus.count(a)
#             if counted > 1:
#                 for _ in range(counted - 1):
#                     nums_plus.remove(a)
#     nums_plus.sort()
#     return nums_plus

# numbers = [2,1,3,4,1]
# print(solution(numbers))

# def 그냥_마음대로(n):
#     sum = 0
#     score = 0
#     for i in n:
#         print(i,end = ' ')
#         if i == 'O':
#             score += 1
#             sum += score
#         else:
#             score = 0
#     return sum

# numbers = 'OOXXOXXOOO'
# print(그냥_마음대로(numbers))

# def solution(abs,s):
#     r = 0
#     for i in  range(3):
#         if s[i] == True:
#             r = r + abs[i]
#         else:
#             r = r - abs[i]
#     return r

# absolution = [4,7,12]
# sign = [True,False,True]
# print(solution(absolution,sign))

def besu_pattern(chiper, code):
    score = ''
    for i in range(len(chiper)):
        if (i+1) % code == 0:
            score += chiper[i]
            
    return score

chiper = 'dfjardstddetckdaccccdegk'
code = 4
print(besu_pattern(chiper,code))