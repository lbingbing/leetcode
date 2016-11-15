The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

Solution:
f0[node]: max when node not robbed
f1[node]: max when node robbed

f0[node]=max(f0[node.left],f1[node.left])+max(f0[node.right],f1[node.right])
f1[node]=node.val+f0[node.left]+f0[node.right]

two result of different states are returned, so only results of children are needed by the parent; otherwise results of grandchildren are also needed because how results of children was achieved (i.e. that child robbed or not) is not clear.
then postorder traversal can return the result without need of linear-sized cache.