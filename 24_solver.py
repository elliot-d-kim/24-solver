def main():
    given_nums = []

    print("Let's solve 24! Enter the 4 given numbers one by one below.\n")
    for i in range(4):
        given_nums.append(int(input("Enter number: ")))

    nums = given_nums
    root = Node(nums)
    buildTree(root)
    findSolutions(root)
    renderTree(root)

class Node:
    def __init__(self, nums):
        self.children = []      # nodes made directly via combinations using self.nums
        self.nums = nums        # the nums available for combination
        self.operands = []      # the numbers combined in parent to create this node
        self.operation = ""     # operation used to combine

def buildTree(node):
    '''
    goal: build tree of all possible arithmetic outcomes
    input: node with list of numbers in nums field
    output: nothing returned (node is grown into tree of possible outcomes)
    '''
    if len(node.nums) == 2:
        for operation, result in applyOperations(node.nums).items():
            child = Node([result])
            child.operands = sorted(node.nums, reverse = True)
            child.operation = operation
            node.children.append(child)
        return
    # iterate through possible pairs for combination
    for i in range(len(node.nums)-1):
        for j in range(i+1, len(node.nums)):
            num1, num2 = node.nums[i], node.nums[j]

            # consider +, -, *, / the two numbers
            for operation, result in applyOperations([num1, num2]).items():
                numsCopy = node.nums.copy()
                numsCopy.pop(j) # removing i first messes up indexing for j
                numsCopy.pop(i)

                # create child node based on combining num1 and num2 with operation
                child = Node(numsCopy + [result])
                child.operands = sorted([num1, num2], reverse = True)
                child.operation = operation
                node.children.append(child)

    for child in node.children:
        buildTree(child)
    
def findSolutions(root):
    '''
    goal: cut all nodes that don't lead to 24
    input: (root) node from which to remove any non-solutions
    output: nothing returned (tree trimmed to contain only paths to 24)
    '''
    if len(root.nums) == 2:
        idx = 0
        while idx < len(root.children):     # foreach: indexing issues with remove()
            child = root.children[idx]
            if child.nums != [24]:          # if non-solution node, trim
                root.children.remove(child)
            else:
                idx += 1
        return
    idx = 0
    while idx < len(root.children):         # foreach: indexing issues with remove()
        child = root.children[idx]
        findSolutions(child)
        if child.children == []:            # if solution(s) among descendants, trim node
            root.children.remove(child)
        else:
            idx += 1

def renderTree(node):
    '''
    goal: show tree in readable format
    input: root node
    output: nothing returned (print tree)
    '''
    prepend = "---" * (4 - len(node.nums))
    appendEqn = ""
    if len(node.nums) < 4:
        appendEqn = ", " + strFormatEqn(node.operands, node.operation)
    print(prepend + str(node.nums) + appendEqn)
    if node.children == []:
        return
    for child in node.children:
        renderTree(child)

def strFormatEqn(operands, operation):
    '''
    goal: format operands and operation as "(a + b)"
    input: operands = (a, b); operation = "+"
    output: return "(a + b)"
    '''
    if operands == []:
        return ""
    return "(" + str(operands[0]) + " " + operation + " " + str(operands[1]) + ")"

def applyOperations(nums):
    '''
    goal: return all valid results from arithmetic operations in a dict
    input: list of 2 nums
    output: {('+', 7), ('-', 1), ('x', 12)}
    '''
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