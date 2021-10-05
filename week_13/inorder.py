# region representation of binary trees.
## This file contains functions for the representation of binary trees.
## used in class Binary_search_tree's __repr__
## Written by a former student in the course (at TAU) - thanks to Amitai Cohen
import copy


def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


# endregion

class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key) + ": " + str(self.val)

    def is_leaf(self):
        return (self.left == None) and (self.right == None)


class Binary_search_tree():
    def __init__(self):
        self.root = None

    def __repr__(self):
        # no need to understand the implementation of this one
        out = ""
        # need printree.py file or make sure to run it in the NB
        for row in printree(self.root):
            out = out + row + "\n"
        return out


    def search(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:  # left
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root == None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

    def inorder(self):
        ''' return inorder traversal of values as str, uses recursion '''

        def inorder_rec(curr_node, res):
            if curr_node is not None:
                inorder_rec(curr_node.left, res)
                res.append((curr_node.key, curr_node.val))
                inorder_rec(curr_node.right, res)
            return res

        if self.root == None:  # empty tree
            return "Empty Tree"
        else:
            return inorder_rec(self.root, [])

    def preorder(self):
        ''' return inorder traversal of values as str, uses recursion '''

        def preorder_rec(curr_node, res):
            if curr_node != None:
                res.append((curr_node.key, curr_node.val))
                preorder_rec(curr_node.left, res)
                preorder_rec(curr_node.right, res)
            return res

        if self.root == None:  # empty tree
            return "Empty Tree"
        else:
            return preorder_rec(self.root, [])


BST = Binary_search_tree()
BST.insert(15, 94)
BST.insert(8, 87)
BST.insert(17, 75)
BST.insert(3, 68)
BST.insert(12, 89)
BST.insert(17, 66)
BST.insert(23, 71)

print(BST)
print(BST.inorder())
# print(BST.preorder())


# BST.insert(5009, 64)
# BST.insert(5007, 98)

# BST.insert(5004, 94)
# BST.insert(5000, 87)
# BST.insert(5001, 75)
# BST.insert(5003, 68)
# BST.insert(5002, 89)
# BST.insert(5005, 66)
# BST.insert(5006, 71)
# BST.insert(5009, 64)
# BST.insert(5007, 98)
# BST.search(5003)
