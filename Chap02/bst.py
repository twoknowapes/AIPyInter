from typing import Optional, List

class TreeNode:
    def __init__(self, value: int):
        """初始化二叉树节点"""
        self.value: int = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class BST:
    def __init__(self):
        """初始化空的二叉搜索树"""
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        """插入新节点"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        """递归插入新节点"""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value: int) -> Optional[TreeNode]:
        """查找节点"""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        """递归查找节点"""
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value: int) -> None:
        """删除节点"""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        """递归删除节点"""
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def _find_min(self, node: TreeNode) -> TreeNode:
        """查找最小值节点"""
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self) -> List[int]:
        """中序遍历"""
        result: List[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[TreeNode], result: List[int]) -> None:
        """递归进行中序遍历"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    bst = BST()

    # 插入节点
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # 中序遍历
    print("In-order Traversal: ", bst.inorder_traversal())  # 输出: [20, 30, 40, 50, 60, 70, 80]

    # 查找节点
    print("Search 40: ", bst.search(40) is not None)  # 输出: True
    print("Search 90: ", bst.search(90) is not None)  # 输出: False

    # 删除节点
    bst.delete(20)
    print("After deleting 20:", bst.inorder_traversal())  # 输出: [30, 40, 50, 60, 70, 80]

    bst.delete(30)
    print("After deleting 30:", bst.inorder_traversal())  # 输出: [40, 50, 60, 70, 80]

    bst.delete(50)
    print("After deleting 50:", bst.inorder_traversal())  # 输出: [40, 60, 70, 80]