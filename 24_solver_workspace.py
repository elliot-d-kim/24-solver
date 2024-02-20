'''
def solnStatements(nums):
    statements = []
    for i in range(0, len(nums)-1):
        num1 = nums[i]
        for j in range(i + 1, len(nums)-1):
            num2 = nums[j]



def generatePairs(nums):
    nums = ["a", "b", "c", "d"]
    if len(nums) == 2:
        return [nums[0] + nums[1]]
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)-1):
            num1, num2 = nums[i], nums[j]
            combinedNum = num1 + num2
            numsCopy = nums
            numsCopy.pop(i)
            numsCopy.pop(j)
            newNums = numsCopy + [combinedNum]
            generatePairs(newNums)

def statementParser(statements):
    pass
    

def solnSearch(nums):
    # pick pair
    # pick operation
    # store (pair, operation) as a step

'''

'''

def populateTree(nums):
    # goal: create next layer until tree ends
    # input: list of nums
    # output: list of possible lists
    nextLayer = []
    for i in range(0, len(nums)-1):
        num1 = num[i]
        num2 = num[i+1]
        for operation, result in applyOperations(num1, num2):


def applyOperations():
    # goal: return all valid results from arithmetic operations in a list
    # input: [3,4]
    # output: [('+', 7), ('-', 1), ('x', 12)]
    pass



def solnSearch(nums):
    if len(nums) == 2:
        for operation, result in applyOperations(nums).items():
            if result == 24:
                return "(" + str(nums[0]) + " " + operation + " " + str(nums[1]) + ")"
        return
    
    for i in range(0, len(nums)-1):
        num1 = nums[i]
        for j in range(i + 1, len(nums)-1):
            num2 = nums[j]

            for operation, result in applyOperations([num1, num2]).items():
                print(j)
                print(nums)
                print(nums[j+1:])
                new_nums = nums[j:] + [result]
                print(new_nums)
                solnSearchRes = solnSearch(new_nums)
                if solnSearchRes != null:
                    return "(" + str(num1) + " " + operation + " " + str(num2) + ")\n" + solnSearchRes


'''

'''

def populateTree(nums):
    # goal: create next layer until tree ends
    # input: list of nums
    # output: list of possible lists
    nextLayer = []
    for i in range(0, len(nums)-1):
        num1 = num[i]
        num2 = num[i+1]
        for operation, result in applyOperations(num1, num2):


def applyOperations():
    # goal: return all valid results from arithmetic operations in a list
    # input: [3,4]
    # output: [('+', 7), ('-', 1), ('x', 12)]
    pass

'''