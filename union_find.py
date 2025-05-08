class QuickFind:
    def __init__(self, n):
        # Initialize the array where each element is its own component ID
        self.id = list(range(n))  # id[i] = component id of i

    def find(self, x):
        # Return the component ID of element x
        return self.id[x]

    def union(self, x, y):
        # Merge the components of x and y
        id_x = self.id[x]
        id_y = self.id[y]
        if id_x != id_y:
            # Update all elements with the same component ID as y to have the component ID of x
            for i in range(len(self.id)):
                if self.id[i] == id_y:
                    self.id[i] = id_x

# QuickFind:
# id = [0, 1, 2, 3, 4]
# union(0, 1)
# -> id = [1, 1, 2, 3, 4]
# union(1, 2)
# -> id = [2, 2, 2, 3, 4]

# - `find` is O(1) because it directly accesses the array.
# - `union` is O(N) because it iterates through the entire array to update component IDs.
# - Space complexity is O(N) because it stores an array of size N.


class QuickUnion:
    def __init__(self, n):
        # Initialize the parent array where each element is its own root
        self.parent = list(range(n))  # каждый элемент - корень сам себе

    def find(self, x):
        # Traverse up the tree to find the root of x
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        # Merge the trees of x and y by connecting their roots
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

# QuickUnion:
# parent = [0, 1, 2, 3, 4]
# union(0, 1)
# -> parent = [1, 1, 2, 3, 4]
# union(1, 2)
# -> parent = [1, 2, 2, 3, 4]
# - `find` is O(N) in the worst case because the tree can become very deep.
# - `union` is O(N) because it depends on `find`.
# - Space complexity is O(N) because it stores the parent array.


class UnionByRank:
    def __init__(self, n):
        # Initialize the parent array and rank array
        self.parent = list(range(n))
        self.rank = [0] * n  # rank represents the height of the tree

    def find(self, x):
        # Traverse up the tree to find the root of x
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        # Merge the trees of x and y based on their rank
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        # Attach the smaller tree under the larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # If ranks are equal, choose one as root and increase its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

# UnionByRank:
# 0 - 1     2 - 3
# rank[0] = 1, rank[2] = 1
# union(0, 2) → оба ранка равны → любой под другой, ранк увеличится
# - `find` is O(log N) because the tree is balanced.
# - `union` is O(log N) because it depends on `find`.
# - Space complexity is O(N) because it stores the parent and rank arrays.


class PathCompressionOnly:
    def __init__(self, n):
        # Initialize the parent array
        self.parent = list(range(n))

    def find(self, x):
        # Find the root of x and compress the path by pointing directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # сжатие пути
        return self.parent[x]

    def union(self, x, y):
        # Merge the trees of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

# PathCompressionOnly:
# До: 0 → 1 → 2 → 3
# После find(0) → 0 → 3, 1 → 3, 2 → 3
# - `find` is O(α(N)) in amortized time, where α is the inverse Ackermann function.
# - `union` is O(α(N)) because it depends on `find`.
# - Space complexity is O(N) because it stores the parent array.


class UnionByRankWithPathCompression:
    def __init__(self, n):
        # Initialize the parent array and rank array
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Find the root of x and compress the path by pointing directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # сжатие пути
        return self.parent[x]

    def union(self, x, y):
        # Merge the trees of x and y based on their rank
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        # Attach the smaller tree under the larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # If ranks are equal, choose one as root and increase its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

# UnionByRankWithPathCompression:
# - Combines both rank and path compression for optimal performance.
# - `find` and `union` are O(α(N)) in amortized time.
# - Space complexity is O(N) because it stores the parent and rank arrays.

# 1. Quick Find → прост, но тормозной
# 2. Quick Union → лучше, но может застревать на find
# 3. Union by Rank → сбалансированные деревья
# 4. Path Compression → супер быстрый find
# 5. Rank + Compression → must have
