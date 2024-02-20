def findOneSoln():
    given_nums = []

    print("Let's solve 24! Enter the 4 given numbers one by one below.\n")
    for i in range(4):
        given_nums.append(input("Enter number: "))

    print(given_nums)

    
def solnSearch(nums):
    if len(nums) == 2:
        for operation, result in applyOperations(nums):
            if result == 24:
                return str(num[0]) + " " + operation + " " + str(num[1])

def applyOperations(nums):
    nums = sorted(nums, reverse = True)
    results = {}

    results['+'] = sum(nums)
    results['-'] = abs(nums[0] - nums[1])
    results['x'] = nums[0] * nums[1]
    if nums[0] % nums[1] == 0:                  # if num is divisible
        results['/'] = nums[0] // nums[1]
    
    return results


print(applyOperations([4, 8]))

'''
notes
    * if not whole num, end

'''