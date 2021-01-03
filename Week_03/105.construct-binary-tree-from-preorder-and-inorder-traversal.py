# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        读题：前序、中序数组还原树，节点元素唯一
        思路：
            根据中序遍历拆分左右子树递归边界，hashmap保存中序数组的值和下标
            根据前序遍历找到各个环节的root节点来建立树（目标是确定哪个节点为空，不空的话是左子树还是右子树）：
        """

        def _m_buildTree(_preorder, _inorder):

            if len(_preorder) == 0 : return None

            root = TreeNode(_preorder[0])
            #求左子树长度，用根节点在中序遍历的下标、减去中序数组的第一个节点的在全局中序map的下标
            size_left = inorder_map[_preorder[0]] - inorder_map[_inorder[0]]

            root.left = _m_buildTree(_preorder[1: 1+size_left], _inorder[: size_left])
            root.right = _m_buildTree(_preorder[1+size_left: ], _inorder[size_left+1: ])

            return root
        
        inorder_map = {value : key for key, value in enumerate(inorder)}
        return _m_buildTree(preorder, inorder)


if __name__ == '__main__':
    cls = Solution()
    cls.buildTree([3,9,20,15,7], [9,3,15,20,7])