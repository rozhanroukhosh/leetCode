#297. Serialize and Deserialize Binary Tree
#link https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import pickle
import codecs
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if(root):
            obj = root.__dict__
            serialized= codecs.encode(pickle.dumps(obj), "base64").decode()
            return serialized
        else:
            serialized= codecs.encode(pickle.dumps(None), "base64").decode()
            return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        decoded = pickle.loads(codecs.decode(data.encode(), "base64"))
        if decoded:
            return TreeNode(**decoded)
        else:
            return []
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))