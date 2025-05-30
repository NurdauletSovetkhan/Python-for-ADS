import streamlit as st

def show_recursion(language):
    st.header("🌀 Topic 1: Recursion")
    st.markdown("""
    **Recursive Function:**  
    A function that calls itself with a smaller input to solve a bigger problem.  

    ✅ Must have:
    - Base Case
    - Recursive Case

    ### 🧮 Example: Factorial
    """)
    if language == "Python":
        st.code("""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
""", language="python")
    elif language == "C++":
        st.code("""
int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}
""", language="cpp")
    else:
        st.code("""
int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}
""", language="java")

    st.markdown("""
    ### ⏱️ Time & Space Efficiency
    - Time: O(n)
    - Space: O(n) (because of recursion stack)

    ❗ **Fibonacci Example (Inefficient)**

    O(2^n) due to overlapping subproblems.
    """)
    if language == "Python":
        st.code("""
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
""", language="python")
    st.markdown("""
    ➕ Use memoization or dynamic programming to improve this.

    ### 🧩 Recursive Data Types
    Examples:
    - Linked Lists
    - Trees (each node is a tree)
    - Graphs (recursive relationships)
    """)

def show_asymptotic(language):
    st.header("📈 Topic 2: Asymptotic Analysis and Big-O")
    st.markdown("""
    **Asymptotic Analysis** lets us analyze how an algorithm behaves as input grows (n → ∞).

    ### 📏 Main Notations:
    - **O(...)** – Worst-case (Big-O)
    - **Ω(...)** – Best-case (Omega)
    - **Θ(...)** – Average-case (Theta)

    ### ⚙️ Time Complexity Table
    """)
    st.table({
        "Complexity": ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n²)", "O(2^n)"],
        "Example": ["Access", "Binary Search", "Linear Search", "Merge Sort", "Bubble Sort", "Fibonacci"]
    })
    st.markdown("### 💻 Examples by Language:")
    if language == "Python":
        st.code("""
# O(1)
x = arr[0]

# O(n)
for i in arr:
    print(i)

# O(log n) - Binary Search
def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
""", language="python")
    elif language == "C++":
        st.code("""
int binarySearch(int arr[], int n, int x) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == x) return mid;
        else if (arr[mid] < x) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
""", language="cpp")
    else:
        st.code("""
int binarySearch(int[] arr, int x) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == x) return mid;
        else if (arr[mid] < x) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
""", language="java")
    st.markdown("""
    ### 🧠 Space Complexity
    Memory used by:
    - Variables
    - Function calls (stack)
    - Data structures (arrays, trees, etc.)
    """)

def show_arrays(language):
    st.header("📊 Topic 3: Arrays")
    st.markdown("""
    **Array** is a collection of elements stored in contiguous memory locations.  
    It allows O(1) access by index but insertion/deletion in the middle is O(n).

    ### Properties:
    - Fixed size (in most languages)
    - Random access

    ### Example:
    """)
    if language == "Python":
        st.code("""
arr = [1, 2, 3, 4, 5]
print(arr[2])  # Output: 3
""", language="python")
    elif language == "C++":
        st.code("""
int arr[] = {1, 2, 3, 4, 5};
cout << arr[2];  // Output: 3
""", language="cpp")
    else:
        st.code("""
int[] arr = {1, 2, 3, 4, 5};
System.out.println(arr[2]);  // Output: 3
""", language="java")
    st.markdown("""
    ### Operations Complexity:
    - Access: O(1)
    - Search: O(n)
    - Insert/Delete at end: O(1) amortized
    - Insert/Delete elsewhere: O(n)
    """)

def show_linked_lists(language):
    st.header("🔗 Topic 4: Linked Lists")
    st.markdown("""
    **Linked List** is a linear data structure where each element (node) contains a value and a pointer to the next node.

    ### Types:
    - Singly Linked List
    - Doubly Linked List
    - Circular Linked List

    ### Advantages over Arrays:
    - Dynamic size
    - Efficient insert/delete at head or tail (O(1))

    ### Example (Singly Linked List Node in Python):
    """)
    if language == "Python":
        st.code("""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
""", language="python")
    elif language == "C++":
        st.code("""
struct Node {
    int val;
    Node* next;
    Node(int x) : val(x), next(nullptr) {}
};
""", language="cpp")
    else:
        st.code("""
class Node {
    int val;
    Node next;
    Node(int x) {
        val = x;
        next = null;
    }
}
""", language="java")
    st.markdown("""
    ### Operations Complexity:
    - Search: O(n)
    - Insert/Delete at head: O(1)
    - Insert/Delete at tail: O(1) if tail pointer exists, else O(n)
    """)

def show_stack_queue(language):
    st.header("📚 Topic 5: Stack and Queue")
    st.markdown("""
    **Stack** — LIFO (Last In, First Out) data structure.  
    **Queue** — FIFO (First In, First Out) data structure.

    ### Stack operations:
    - Push: add to top (O(1))
    - Pop: remove from top (O(1))
    - Peek/Top: see top element (O(1))

    ### Queue operations:
    - Enqueue: add to back (O(1))
    - Dequeue: remove from front (O(1))

    ### Example: Stack in Python
    """)
    if language == "Python":
        st.code("""
stack = []
stack.append(10)  # push
top = stack.pop() # pop
""", language="python")
    elif language == "C++":
        st.code("""
#include <stack>
std::stack<int> s;
s.push(10);
int top = s.top();
s.pop();
""", language="cpp")
    else:
        st.code("""
import java.util.Stack;
Stack<Integer> s = new Stack<>();
s.push(10);
int top = s.pop();
""", language="java")
    st.markdown("""
    ### Queues can be implemented using arrays or linked lists.  
    For efficient O(1) enqueue and dequeue, use **circular queue** or **linked list** based queue.
    """)

def show_heap(language):
    st.header("📦 Topic 6: Heap")
    st.markdown("""
    **Heap** is a specialized tree-based data structure that satisfies the heap property:  
    - Max-Heap: Parent node ≥ children  
    - Min-Heap: Parent node ≤ children

    ### Common uses:
    - Priority Queues
    - Heapsort

    ### Operations:
    - Insert: O(log n)
    - Extract Max/Min: O(log n)
    - Peek Max/Min: O(1)

    ### Example: Python Min-Heap using `heapq` module
    """)
    if language == "Python":
        st.code("""
import heapq
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
min_val = heapq.heappop(heap)
""", language="python")
    elif language == "C++":
        st.code("""
// Use priority_queue from STL (default max-heap)
#include <queue>
std::priority_queue<int> pq;
pq.push(10);
pq.push(5);
int max_val = pq.top();
pq.pop();
""", language="cpp")
    else:
        st.code("""
import java.util.PriorityQueue;
PriorityQueue<Integer> pq = new PriorityQueue<>(); // min-heap by default
pq.add(10);
pq.add(5);
int min_val = pq.poll();
""", language="java")

def show_hash_tables_trees(language):
    st.header("🔍 Topic 7: Hash Tables & Trees")
    st.markdown("""
    ### Hash Table:
    - Data structure that stores key-value pairs
    - Average O(1) insert, delete, search
    - Uses hashing function

    ### Example: Python dict
    """)
    if language == "Python":
        st.code("""
my_dict = {'apple': 5, 'banana': 3}
print(my_dict['apple'])  # Output: 5
""", language="python")
    elif language == "C++":
        st.code("""
#include <unordered_map>
std::unordered_map<std::string, int> my_map;
my_map["apple"] = 5;
""", language="cpp")
    else:
        st.code("""
import java.util.HashMap;
HashMap<String, Integer> map = new HashMap<>();
map.put("apple", 5);
""", language="java")
    st.markdown("""
    ### Trees:
    - Hierarchical data structure
    - Each node has children nodes
    - Special types: Binary Trees, Binary Search Trees (BST), AVL Trees, Heaps, Tries

    ### BST Example (insert/search):
    """)
    if language == "Python":
        st.code("""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
""", language="python")
    elif language == "C++":
        st.code("""
struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int x): val(x), left(nullptr), right(nullptr) {}
};

Node* insert(Node* root, int val) {
    if (!root) return new Node(val);
    if (val < root->val) root->left = insert(root->left, val);
    else root->right = insert(root->right, val);
    return root;
}
""", language="cpp")
    else:
        st.code("""
class Node {
    int val;
    Node left, right;
    Node(int x) {
        val = x;
        left = right = null;
    }
}

Node insert(Node root, int val) {
    if (root == null) return new Node(val);
    if (val < root.val) root.left = insert(root.left, val);
    else root.right = insert(root.right, val);
    return root;
}
""", language="java")

def show_sorting(language):
    st.header("🔃 Topic 8: Sorting Algorithms")
    st.markdown("""
    ### Bubble Sort:
    - Simple, repeatedly swaps adjacent elements if out of order
    - O(n²) time complexity

    ### Merge Sort:
    - Divide and Conquer
    - Splits array, sorts subarrays, merges them
    - O(n log n) time complexity

    ### Quick Sort:
    - Divide and Conquer
    - Picks pivot, partitions array around pivot
    - Average O(n log n), worst O(n²)

    ### Example: Merge Sort (Python)
    """)
    if language == "Python":
        st.code("""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
""", language="python")
    elif language == "C++":
        st.code("""
// Merge Sort in C++ (simplified)
void merge(int arr[], int l, int m, int r) {
    // merging code here ...
}
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = (l+r)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}
""", language="cpp")
    else:
        st.code("""
// Quick Sort Java Example
void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
""", language="java")

def show_searching(language):
    st.header("🔍 Topic 9: Searching Algorithms")
    st.markdown("""
    ### Linear Search:
    - Check elements one by one
    - O(n) time

    ### Binary Search:
    - Works on sorted arrays
    - Repeatedly divide search interval in half
    - O(log n) time

    ### Example: Binary Search Python
    """)
    if language == "Python":
        st.code("""
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
""", language="python")
    elif language == "C++":
        st.code("""
int binarySearch(int arr[], int n, int x) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == x) return mid;
        else if (arr[mid] < x) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
""", language="cpp")
    else:
        st.code("""
int binarySearch(int[] arr, int x) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == x) return mid;
        else if (arr[mid] < x) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
""", language="java")

def show_graphs(language):
    st.header("🌐 Topic 10: Graphs")
    st.markdown("""
    A **Graph** consists of vertices (nodes) and edges (connections).  

    ### Types:
    - Directed / Undirected
    - Weighted / Unweighted

    ### Representation:
    - Adjacency Matrix (O(V²) space)
    - Adjacency List (O(V+E) space)

    ### Traversals:
    - DFS (Depth-First Search)
    - BFS (Breadth-First Search)

    ### Example: Graph with adjacency list (Python)
    """)
    if language == "Python":
        st.code("""
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
""", language="python")
    elif language == "C++":
        st.code("""
// Adjacency list representation
#include <vector>
#include <list>
std::vector<std::list<int>> graph(4);
graph[0].push_back(1); // edge 0->1
graph[1].push_back(3);
""", language="cpp")
    else:
        st.code("""
// Java adjacency list
import java.util.ArrayList;
ArrayList<Integer>[] graph = new ArrayList[4];
for (int i = 0; i < 4; i++) graph[i] = new ArrayList<>();
graph[0].add(1);
graph[1].add(3);
""", language="java")
    st.markdown("""
    ### DFS Example (Python):
    """)
    if language == "Python":
        st.code("""
def dfs(graph, start, visited=set()):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
""", language="python")