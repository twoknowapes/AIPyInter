from collections import deque, defaultdict
from typing import List, Dict, Set

class Graph:
    """Implementation of an undirected graph using adjacency list
    
    Supports:
    - Adding nodes and edges
    - Depth-first search (DFS)
    - Breadth-first search (BFS)
    """
    def __init__(self):
        self.graph: Dict[int, List[int]] = defaultdict(list)

    def add_node(self, node: int) -> None:
        """Add a node to the graph"""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u: int, v: int) -> None:
        """Add an undirected edge (u, v) to the graph"""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start: int) -> List[int]:
        """Depth-first search traversal
        
        Recursively visits all unvisited neighbors of each node
        Returns list of nodes in traversal order
        """
        # 用集合记录已访问的节点
        visited: Set[int] = set()
        # 存储遍历顺序的结果列表
        result: List[int] = []

        def _dfs(v: int) -> None:
            # 将当前节点标记为已访问
            visited.add(v)
            # 将当前节点加入结果列表
            result.append(v)
            # 递归访问所有未访问的相邻节点
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    _dfs(neighbor)

        # 从起始节点开始深度优先遍历
        _dfs(start)
        return result

    def bfs(self, start: int) -> List[int]:
        """Breadth-first search traversal
        
        Uses a queue to visit nodes level by level
        Returns list of nodes in traversal order
        """
        # 用集合记录已访问的节点
        visited: Set[int] = set()
        # 使用双端队列存储待访问的节点
        queue: deque[int] = deque([start]) 
        # 存储按访问顺序的节点列表
        result: List[int] = []

        # 持续处理队列中的节点直到队列为空
        while queue:
            # 从队列左侧取出一个节点
            v = queue.popleft()
            if v not in visited:
                # 将节点标记为已访问
                visited.add(v)
                # 将节点加入结果列表
                result.append(v)
                # 将所有未访问的邻接节点加入队列
                for neighbor in self.graph[v]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result