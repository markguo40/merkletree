###################
# Zhanchen Guo
# Merkel Tree implementation
###################
from __future__ import division
import hashlib
from collections import deque

hash_func = hashlib.sha256

class MerkleTree(object):

    class Node(object):

        def __init__(self, value):
            self.value = hash_func(value).hexdigest()
            self.left = None
            self.right = None

        def __add__(self, node):
            if type(node) == type(self):
                return self.value + node.value
            raise Exception("Internal Comparison Error. You have to compare Node to Node")

        def hasNoChild(self):
            return self.left == self.right == None

    def __init__(self, items):
        """ Items should be a list of strings
            The order of the items matters
        """
        self.hashed_items = self._hash(items)
        self.root, self.height = self._grow(self.hashed_items)

    def _hash(self, items):
        return [self.Node(item) for item in items]

    def _grow(self, items, height=0):
        """ Bottom up, all the way to the root
        """
        nodes = []
        last = None
        if len(items) > 1:
            if len(items) % 2 == 1:
                last = items.pop()
            for i in xrange(0, len(items), 2):
                parent = self.Node(items[i] + items[i + 1])
                parent.left = items[i]
                parent.right = items[i + 1]
                nodes.append(parent)
            if last:
                parent = self.Node(last.value)
                parent.left = last
                nodes.append(parent)
                items.append(last) # put the last item back in
            return self._grow(nodes, height + 1)
        else:
            return items[0], height

    def getRootValue(self):
        """ Return the root value of the merkle tree
        """
        return self.root.value

    def getValuesFromDepth(self, depth):
        """ Argument is the target depth
            Return a list of the values at the target depth of the tree
        """
        if depth == self.height:
            return self.getAllValue()
        elif depth < self.height:
            items = self._depth([self.root], depth, 0)
            return [item.value for item in items]
        raise Exception("Your target depth can not be over the tree height")

    def getAllValue(self):
        """ Return a list of all the node value at the bottom of the tree
        """
        return [item.value for item in self.hashed_items]

    def _depth(self, values, depth, current):
        """ Top down fashion. Used by getValuesFromDepth function as well as
            diff function
        """

        depth_values = []
        for Node in values:
            depth_values.append(Node.left)
            if Node.right:
                depth_values.append(Node.right)

        current += 1
        if current == depth:
            return depth_values
        return self._depth(depth_values, depth, current)

    def getHeight(self):
        """ The height of the merkle tree does not include the root node
        """
        return self.height

    def add(self, values):
        """ Argument values can be string or a list, if it is a string, it
            will treat the string as one item
            This method will add that value to the merkle tree
        """
        if type(values) != list:
            values = [values]
        self.hashed_items.extend(self._hash(values))
        self.root, self.height = self._grow(self.hashed_items)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.getRootValue == self.getRootValue()
        raise Exception("You have to compare Merkle Tree with Merkle Tree")

    def __ne__(self, other):
        return not self.__eq__(other)

    def diff(self, other):
        """ Automatically find the differences between two trees
            Arugment other has to be a merkle tree
            Optimized if two trees have the same height
            Return and print in the console both the different hash value in
            the current tree and the different hash value in the other tree
        """
        if self == other: #if not compariable, the exception will raise in __eq__
            raise Exception("There is no differences between two trees")

        #Using Breadth First Seach optimize only if the trees have the same height
        diff_curr = []
        diff_other = []

        if self.height == other.getHeight():
            selfqueue = deque([self.root])
            otherqueue = deque([other.root])
            extra = deque()
            longer = 0 # 0 represent equal, 1 means other tree longer, 2 means current tree longer

            while selfqueue:
                curr_node = selfqueue.popleft()
                other_node = otherqueue.popleft()
                if curr_node.hasNoChild():
                    diff_curr.append(curr_node.value)
                if other_node.hasNoChild():
                    diff_other.append(other_node.value)

                # This just in case one tree has more hashed items than another
                if not curr_node.right and other_node.right:
                    extra.append(other_node)
                    longer = 1

                if curr_node.right and not other_node.right:
                    extra.append(curr_node)
                    longer = 2

                if curr_node.left and other_node.left and curr_node.left.value != other_node.left.value:
                    selfqueue.append(curr_node.left)
                    otherqueue.append(other_node.left)
                if curr_node.right and other_node.right and curr_node.right.value != other_node.right.value:
                    selfqueue.append(curr_node.right)
                    otherqueue.append(other_node.right)


            extra_result = []
            while extra:
                current = extra.popleft()
                if current.hasNoChild():
                    extra_result.append(current)
                    continue
                extra.append(current.left)
                if current.right:
                    extra.append(current.right)
            if longer == 2:
                diff_curr += extra_result
            elif longer == 1:
                diff_other += extra_result
        else:
            curr_items = self.hashed_items
            other_items = other.hashed_items
            flag = 0
            if len(curr_items) > len(other_items):
                flag = 1
                extra = curr_items[len(other_items):]
                curr_items = curr_items[:len(other_items)]
            elif len(curr_items) < len(other_items):
                flag = 2
                extra = other_items[len(curr_items):]
                other_items = other_items[:len(curr_items)]

            for curr_item, other_item in zip(curr_items, other_items):
                if curr_item.value != other_item.value:
                    diff_curr.append(curr_item.value)
                    diff_other.append(other_item.value)

            # In case one tree has more hashed items than another
            extra = [item.value for item in extra]
            if flag == 1:
                diff_curr += extra
            elif flag == 2:
                diff_other += extra

        print "Different nodes: this tree:"
        for node in diff_curr:
            print node,
        print
        print "Another tree:"
        for node in diff_other:
            print node,
        print

        return diff_curr, diff_other

def sample():
    """ This is a example of how to use the Merkle Tree Class
    """
    sample1 = ["Name: Zhanchen Guo",
                "Emails: markguo@minerva.kgi.edu",
                "Accont Balance: 100",
                "Birthday: 05/21/96",
                ]

    sample2 = ["Name: Zhanchen Guo",
                "Emails: markguo40@gmail.com",
                "Accont Balance: 100",
                "Birthday: none",
                ]

    hashed = MerkleTree(sample1)
    print "Before adding"
    print "Height:", hashed.getHeight()
    print "Root Value:", hashed.getRootValue()
    hashed.add(["Marrital Status: Single"])
    print "After adding"
    print "Height:", hashed.getHeight()
    print "Root Value:", hashed.getRootValue()
    print "The value for depth 2:"
    print hashed.getValuesFromDepth(2)

    hashed2 = MerkleTree(sample2)
    hashed2.diff(hashed)

    print
    print "###########################"
    print "New case when they have the same height"
    hashed2.add(["Marrital Status: Single"])
    hashed2.diff(hashed)
