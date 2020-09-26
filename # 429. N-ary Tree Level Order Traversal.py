# my solution 与最快版本思路一致 时间也相近
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        curr_list = [root]
        while len(curr_list) > 0:
            curr_node = []
            level_res = []
            for item in curr_list:
                level_res.append(item.val)
                for child in item.children:
                    curr_node.append(child)
            curr_list = curr_node
            res.append(level_res)
        return res


# recursive solution by others
class Solution:
	def levelOrder(self, root) -> List[List[int]]:
		output = []
		if root is not None:
			output.append([root.val])
			self.trav(root.children, 0, output)
			output.pop()
		return output

	def trav(self, node, deep, output):
		deep += 1
		if (len(output) - 1 < deep): output.append([])
		for x in node:
			output[deep].append(x.val)
			if x.children is not None:
				self.trav(x.children, deep, output)