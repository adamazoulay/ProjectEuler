# Template file for Project Euler questions
def build_tree(x_pos, y_pos):
    current_node = binary_tree_node(x_pos, y_pos)
    if x_pos < 0 or y_pos < 0:
        return None
    # elif (x_pos == 1 and y_pos == 0) or (x_pos == 0 and y_pos == 1):
    elif x_pos == 0 and y_pos == 0:
        return None
    else:
        current_node.down_child = build_tree(x_pos, y_pos - 1)
        current_node.right_child = build_tree(x_pos - 1, y_pos)
    # print(current_node.x_pos, " ", current_node.y_pos, " ", current_node.is_bottom)
    return current_node


def count_bottom_nodes(root_node):
    if root_node is None:
        return 0
    # print(root_node.x_pos, root_node.y_pos)
    if root_node.is_bottom:
        return 1 + count_bottom_nodes(root_node.down_child) + count_bottom_nodes(root_node.right_child)

    return count_bottom_nodes(root_node.down_child) + count_bottom_nodes(root_node.right_child)



class binary_tree_node:
    def __init__(self, x_pos, y_pos):
        self.down_child = None
        self.right_child = None
        self.x_pos = x_pos
        self.y_pos = y_pos
        if (self.x_pos == 1 and self.y_pos == 0) or (self.x_pos == 0 and self.y_pos == 1):
            self.is_bottom = True
        else:
            self.is_bottom = False


def lattice_paths(grid):
    current_node = build_tree(grid, grid - 1)
    print(2 * count_bottom_nodes(current_node))


if __name__ == "__main__":
    lattice_paths(12)
