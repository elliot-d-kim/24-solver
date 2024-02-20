def main():
    given_nums = []

    print("Let's solve 24! Enter the 4 given numbers one by one below.\n")
    for i in range(4):
        given_nums.append(input("Enter number: "))

    print(given_nums)

    nums = [2, 3, 4, 6]
    root = Node(nums)
    buildTree(root)
    renderTree(root)

class Node:
    def __init__(self, nums):
        self.children = []
        self.nums = nums
        self.operation = ""

def buildTree(node):
    if len(node.nums) == 2:
        for operation, result in applyOperations(node.nums).items():
            child = Node(result)
            child.operation = operation
            node.children.append(child)
        return
    for i in range(len(node.nums)-1):
        for j in range(i+1, len(node.nums)):
            num1, num2 = node.nums[i], node.nums[j]
            for operation, result in applyOperations([num1, num2]).items():
                numsCopy = node.nums.copy()
                numsCopy.pop(j) # removing i first messes up indexing for j
                numsCopy.pop(i)
                childNums = numsCopy + [result]
                child = Node(childNums)
                child.operation = operation
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
    
    # avoid dividing by 0
    if nums[1] != 0:
        # check if num is divisible
        if nums[0] % nums[1] == 0:
            results['/'] = nums[0] // nums[1]
    else:
        results['/'] = 0
    
    return results

main()