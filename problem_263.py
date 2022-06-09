#236. Lowest Common Ancestor of a Binary Tree
#link https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution:
    
    dic = dict()
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def intersection(lst1, lst2):
            for value in lst1:
                if value in lst2:
                    return value
        
        queue=[(root,None)]
        
        while queue:
            node, parent = queue.pop()
            if node:
                if(parent and self.dic[parent.val]):
                     self.dic[node.val] =  [node.val] + self.dic[parent.val]
                else:
                     self.dic[node.val] =  [node.val]
                queue.append((node.left, node))
                queue.append((node.right, node))
                print(self.dic)
        return TreeNode(intersection(self.dic[p.val], self.dic[q.val]))
       
    

     
            