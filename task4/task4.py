import sys
path = sys.argv[1]
with open(path) as f:
    filenum = f.readlines()
    nums = [int(a) for a in filenum]
nums.sort()
med = nums[len(nums) // 2]
moves = sum(abs(x - med) for x in nums)
if moves <= 20:
    print(moves)
else:
    print('20 ходов недостаточно для приведения всех элементов массива к одному числу')
