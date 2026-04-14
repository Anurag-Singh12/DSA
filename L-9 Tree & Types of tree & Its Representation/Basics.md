# Tree in DSA (Basics)

- A **tree** is a **non-linear data structure** made of nodes  
- It represents a **hierarchical relationship**  
- The top node is called the **root**  
- Each node can have **child nodes**  
- Nodes are connected by **edges**  

## Key Terms

- **Root** → topmost node  
- **Parent / Child** → relationship between nodes  
- **Leaf Node** → node with no children  
- **Subtree** → smaller tree inside a tree  
- **Height** → longest path from root to leaf  
- **Depth** → distance from root to a node  


## Types of Trees

### 1. Binary Tree
- Each node has at most **2 children**  
- (left, right)

### 2. Binary Search Tree (BST)
- Left < Root < Right  
- Used for searching  

### 3. Full/Strict Binary Tree
- Each node has **0 or 2 children**  

### 4. Complete Binary Tree
- All levels filled except last (left to right)  


## Tree Representation

### 1. Array Representation

- Mostly used for **Binary Trees**  

- Index rules:
  - Left child → `2*i + 1`  
  - Right child → `2*i + 2`

#### Drawbacks of Tree using Array
- More memory usage (adding dummy nodes)
- Complex implementation

#### Example:
Index: 0 1 2 3 4
Value: A B C D E


### 2. Linked List Representation

- Each node contains:

data | left pointer | right pointer