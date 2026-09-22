# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map={val:i for i,val in enumerate(inorder)}
        self.idx=0
        def helper(left,right):
            if left>right:
                return None
            root_val=preorder[self.idx]
            self.idx+=1
            root=TreeNode(root_val)
            mid=idx_map[root_val]
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(inorder)-1)
            # if not preorder or not inorder:
            #     return None
            # root=TreeNode(preorder[0])
            # idx=inorder.index(preorder[0])
            # root.left=self.buildTree(preorder[1:idx+1],inorder[:idx])
            # root.right=self.buildTree(preorder[idx+1:],inorder[idx+1:])
                    
            # return root
