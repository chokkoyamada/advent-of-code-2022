from anytree import Node, RenderTree

direction = """$ cd /
$ ls
dir blrnnv
dir ctfjwl
dir dqf
135993 dqqbcfr
$ cd dqf
"""

direction2 = """$ cd /
$ ls
dir blrnnv
dir ctfjwl
dir dqf
135993 dqqbcfr
dir ftj
125510 fzjdz
dir jvtlfbzr
31762 lsvw.lwr
dir qfstpm
dir sbprmc
dir svbnljr
dir tchbjclg
dir wtm
dir ztrz
$ cd blrnnv
$ ls
169869 mjjj.wnq
$ cd ..
$ cd ctfjwl
$ ls
"""


lines = direction2.splitlines()
n = Node(name="Root", type="dir")
root = n
current_node: Node = n
for line in lines:
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
print(result)
