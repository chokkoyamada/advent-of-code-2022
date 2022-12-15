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
    for node in root.descendants:
        if node.type == "dir":
            size = 0
            for n in node.descendants:
                if n.type == "file":
                    size += int(n.size)
            if size <= 100000:
                total_size += size
    print(total_size)


if __name__ == "__main__":
    main()
