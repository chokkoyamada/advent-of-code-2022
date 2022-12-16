from anytree import Node, RenderTree


def main():
    lines = open("day7/inputs.txt").readlines()
    n = Node(name="Root", type="dir")
    root = n
    current_node: Node = n
    for line in lines:
        line = line.rstrip()
        if line.startswith("$"):
            if line.startswith("$ cd"):
                dir = line.split(" ")[2]
                if line == "$ cd /":
                    pass
                elif dir == "..":
                    current_node = current_node.parent
                else:
                    n = next(x for x in current_node.children if x.name == dir)
                    current_node = n
            elif line.startswith("$ ls"):
                pass
        else:
            if line.startswith("dir"):
                dir_name = line.split(" ")[1]
                n = Node(name=dir_name, parent=current_node, type="dir")
            else:
                size, file_name = line.split(" ")
                n = Node(name=file_name, parent=current_node, type="file", size=size)

    result = RenderTree(root)
    total_size = 0
    # calculate total size
    for pre, fill, node in result:
        if node.type == "file":
            total_size += int(node.size)
    print(total_size)
    size_to_reduce = 3636666
    size_list = []
    for node in root.descendants:
        if node.type == "dir":
            size = 0
            for n in node.descendants:
                if n.type == "file":
                    size += int(n.size)
            size_list.append(size)

    # size_to_reduceより大きいもので最小のものを探す
    result = min([x for x in size_list if x > size_to_reduce])
            
    print(result)


if __name__ == "__main__":
    main()
