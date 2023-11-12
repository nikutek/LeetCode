import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root:[TreeNode]) -> bool:
        level = 0
        
        while len(root)!=0:
            if math.pow(2,level) >=2: 
                nodes = root[:int(math.pow(2,level))]
                for i in range(len(nodes)//2):
                    print(nodes[i], nodes[-(i+1)])
                    if nodes[i] != nodes[-(i+1)]:
                        return False
                    
                root = root[int(math.pow(2,level)):]
                level+=1
            else:
                root.pop(0)
                level+=1
        return True
    
solution = Solution()
print(solution.isSymmetric([1,2,2,None,3,None,3]))