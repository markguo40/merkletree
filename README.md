# merkletree
A implementation of Merkle Tree

Author: Zhanchen Guo

No external package is required. This package only support Python 2

Merkle Tree is a binary tree that use hashes as value stored in each node. It also known as blockchain as it can check if all the information in the tree are the same by comparing only the hash value of the root node. More information in [Wikipedia](https://en.wikipedia.org/wiki/Merkle_tree)

##How to use it

I haven't figure out how to let user install, but here is how to use it, go into the same directory
write code like this
```
from merkletree import MerkleTree
```

or you can try the sample code
```
from merkletree import sample
sample()
```

merkletree.py file offers MerkleTree class and a function that contains the sample code

You can create MerkleTree instances.
For each MerkleTree object, you have following method to use:
getRootValue()
getValuesFromDepth(depth)
getAllValue()
getHeight()
add(vaue)
diff(other)

More detail on these method look up the comments in the code

This Merkle Tree package offer a method called diff to compare two Merkle Trees and find out the different base nodes (base nodes are the nodes in the bottom of the tree). This method contains a optimization through selected Breadth First Search which can potentially reduce the run time, but it will only perform it when the heights of two trees are the same. The optimization based on the idea that, if one related node has the same value between two trees, then all the children below this node should be the same, and therefore, there is not point to keep tracing down this node. If two tree have different height. Assuming N is the numbers of the base node in the smaller tree. The time complexity is O(N) as it directly loop through the base nodes rather tracing down the trees. If two trees have the same height, assuming there are M nodes that are different between two trees where M < N, the time complexity is O(M log M). You can see that if M is very close to N, this may cause longer time, but in practice. M suppose to be way smaller than N. 

Note that while it is possible to access the helper Node object, such behavior is not encouraged. All the method above will return the value in terms of hashes rather than Node objects. 

Note that the add method is not optimized. Every time you add a value, it will rebuild the entire tree. The time complexity is O(N log N)
