class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        while root or stack:
          while root:
            stack.append(root)
            root = root.left
          root = stack.pop()
          result.append(root.val)
          root = root.right
        return result  