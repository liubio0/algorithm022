# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        1、读题：节点值唯一，p、q不同节点均存在二叉树，求二者的最近公共祖先，可能为自己。
        2、思路：
            递归、分治：
            1）从根节点出发，记录每个节点找到p或者q的状态然后往父节点传。
            2）找p或者q都可以返回的逻辑是：
                2.1 找到一个节点p（或者q），就确定了该节点一定与最终结果有关：
                2.1.1 p是最终结果，比如找到p，包含了后裔节点q，此时返回了p。
                2.1.2 p不是最终结果，返回该节点的结果后，通过q节点的返回结果合并即可找到最终结果。
        """
        if not root or root == p or root == q : return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left: return right
        if not right: return left
        if left and right: return root
        
        return None
    
    
    def lowestCommonAncestor_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        1、读题：节点值唯一，p、q不同节点均存在二叉树，求二者的最近公共祖先，可能为自己。
        2、思路：
            递归、分治：
            1）从根节点出发，记录每个节点找到p或者q的状态然后往父节点传。
            2）找p或者q都可以返回的逻辑是：
                2.1 找到一个节点p（或者q），就确定了该节点一定与最终结果有关：
                2.1.1 p是最终结果，比如找到p，包含了后裔节点q，此时返回了p。
                2.1.2 p不是最终结果，返回该节点的结果后，通过q节点的返回结果合并即可找到最终结果。
        """
        if not root or root == p or root == q : return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        return root if left and right else (left if not right else right)