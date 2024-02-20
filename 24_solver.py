def findOneSoln():
    given_nums = []

    print("Let's solve 24! Enter the 4 given numbers one by one below.\n")
    for i in range(4):
        given_nums.append(input("Enter number: "))

    print(given_nums)

    print(solnSearch(sorted(nums)))

class Node:
    def __init__(self, nums):
        self.children = []
        self.nums = nums
        self.operation = ""

def buildTree(node):
    if len(node.nums) == 2:
        childNums = node.nums[0] + node.nums[1]
        child = Node(childNums)
        node.children.append(child)
        return
    for i in range(len(node.nums)-1):
        for j in range(i+1, len(node.nums)):
            num1, num2 = node.nums[i], node.nums[j]
            combinedNum = num1 + num2
            numsCopy = node.nums.copy()
            numsCopy.pop(j) # removing i first messes up indexing for j
            numsCopy.pop(i)
            childNums = numsCopy + [combinedNum]
            child = Node(childNums)
            node.children.append(child)
    for child in node.children:
        buildTree(child)

def renderTree(node):
    print(node.nums)
    if node.children == []:
        return
    for child in node.children:
        renderTree(child)
    
            
def applyOperations(nums):
    # goal: return all valid results from arithmetic operations in a dict
    # input: list of 2 nums
    # output: {('+', 7), ('-', 1), ('x', 12)}
    nums = sorted(nums, reverse = True)
    results = {}

    results['+'] = sum(nums)
    results['-'] = nums[0] - nums[1]
    results['x'] = nums[0] * nums[1]
    
    # check first if num is divisible
    if nums[0] % nums[1] == 0:
        results['/'] = nums[0] // nums[1]
    
    return results

nums = ["a", "b", "c", "d"]
root = Node(nums)
buildTree(root)
renderTree(root)