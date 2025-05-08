# python -m streamlit run Python-for-ADS/ds_demo.py

import streamlit as st
import time
import random
from union_find import (
    QuickFind,
    QuickUnion,
    UnionByRank,
    PathCompressionOnly,
    UnionByRankWithPathCompression
)
import matplotlib.pyplot as plt




st.set_page_config(page_title="Disjoint Set Visualizer", layout="wide")

st.title("📚 Disjoint Set Data Structures")
tab1, tab2 = st.tabs(["📘 Theory", "⚙️ Benchmarks"])

with tab1:
    st.header("📘 Theory and Tasks")

    st.markdown("""
    ### 💡 Disjoint Set (Union-Find)

    A **Disjoint Set** is a data structure that keeps track of a partition of elements into **non-overlapping subsets**.  
    It is especially useful for determining whether two elements belong to the same subset.

    #### Core Operations:
    - **Find(x)** — returns the representative (root) of the subset containing `x`.
    - **Union(x, y)** — merges the subsets containing `x` and `y`.

    #### Optimizations:
    - **Path Compression** — flattens the tree structure during `find` calls to speed up future accesses.
    - **Union by Rank / Size** — always attaches the smaller tree under the root of the larger one.

    #### Applications:
    - Building **Minimum Spanning Trees (MST)** (e.g., Kruskal's algorithm)
    - **Connectivity** checking in graphs
    - **Clustering** and grouping problems
    - Grouping systems (e.g., social networks)

    👉 [Open presentation](https://docs.google.com/presentation/d/12VCENn-07ZMsSt0ZlJj_YpXNWtR3aEeNlLp6KD0PGf8/edit#slide=id.g20e53a1f10d_0_135)
    """)


        
    st.subheader("Task #1 — Quick Find")
    st.markdown("""
    **Quick Find** is the simplest implementation of Disjoint Set.  
    Each element stores an ID that represents its connected component.

    - **Find:** O(1) — Direct lookup of component ID.  
    - **Union:** O(N) — May need to update all elements with the same component ID.  
    - **Space:** O(N)
    """)
    st.code("""
    class QuickFind:
        def __init__(self, n):
            self.id = list(range(n))  # Each node starts in its own component

        def find(self, x):
            return self.id[x]  # Just return the component ID

        def union(self, x, y):
            pid = self.id[x]
            qid = self.id[y]
            for i in range(len(self.id)):
                if self.id[i] == pid:
                    self.id[i] = qid  # Update all elements with old ID to new one
    """)

    st.subheader("Task #2 — Quick Union")
    st.markdown("""
    **Quick Union** improves on Quick Find by representing each set as a tree.  
    Each node stores a reference to its parent.

    - **Find:** O(N) — Can be slow if the tree is tall.  
    - **Union:** O(N) — Depends on `find`.  
    - **Space:** O(N)  

    **Difference from Quick Find:**  
    `union` is faster in some cases, but `find` becomes slower due to tree traversal.
    """)
    st.code("""
    class QuickUnion:
        def __init__(self, n):
            self.parent = list(range(n))  # Each node is its own root initially

        def find(self, x):
            while x != self.parent[x]:  # Go up until we find the root
                x = self.parent[x]
            return x

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            self.parent[root_x] = root_y  # Attach one tree under another
    """)


    st.subheader("Task #3 — Union by Rank")
    st.markdown("""
    **Union by Rank** optimizes Quick Union by keeping trees balanced.  
    It tracks the depth (rank) of each tree and always attaches the shorter tree under the taller one.

    - **Find:** O(log N) — Height of the tree is limited.  
    - **Union:** O(log N)
    """)
    st.code("""
    class UnionByRank:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n  # Rank represents tree depth

        def find(self, x):
            while x != self.parent[x]:
                x = self.parent[x]
            return x

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x == root_y:
                return  # Already connected
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
    """)

    st.subheader("Task #4 — Path Compression")
    st.markdown("""
    **Path Compression** improves the `find` operation by flattening the tree.  
    Every time we call `find`, we make each node point directly to the root.

    - **Find:** O(log N) → O(α(N)) amortized — very close to constant.  
    - **Union:** O(N) — Without rank, union can still be costly.
    """)
    st.code("""
    class PathCompression:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])  # Flatten the path
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                self.parent[root_x] = root_y
    """)

    st.subheader("Task #5 — Union by Rank + Path Compression")
    st.markdown("""
    **Union by Rank + Path Compression** is the most efficient version of Disjoint Set.  
    It combines both optimizations to achieve nearly constant time for both operations.

    - **Find & Union:** O(α(N)) — In practice, almost O(1).  
    - **Space:** O(N)

    This is what most competitive programmers and real-world systems use.
    """)
    st.code("""
    class UnionByRankWithPathCompression:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x == root_y:
                return
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
    """)

    
with tab2:
    if "n" not in st.session_state:
        st.session_state.n = 10_000
    if "runs" not in st.session_state:
        st.session_state.runs = 50_000

    n = st.session_state.n
    runs = st.session_state.runs

    operations = [(random.randint(0, n - 1), random.randint(0, n - 1)) for _ in range(runs)]

    if st.button("🎲 Randomize Values"):
        st.session_state.n = random.randint(10, 100_000)
        st.session_state.runs = random.randint(10, 100_000)
        st.rerun()

    n = st.slider("Количество элементов", 10, 100_000, st.session_state.n, step=1000)
    runs = st.slider("Количество операций union/find", 10, 100_000, st.session_state.runs, step=1000)

    st.session_state.n = n
    st.session_state.runs = runs

    st.subheader("📊 Theoretical difficulty (Big-O)")

    st.markdown("""
    - **Quick Find**:  
      - `find`: O(1) — direct access to the component ID.  
      - `union`: O(N) — need to update IDs for all connected elements.
      
    - **Quick Union**:  
      - `find`: O(N) — may traverse a tall tree.  
      - `union`: O(N) — depends on `find` time.

    - **Union by Rank**:  
      - `find`: O(log N) — due to tree balancing.  
      - `union`: O(log N) — trees stay balanced.

    - **Path Compression Only**:  
      - `find`: O(log N) → O(α(N)) amortized — flattens the tree.  
      - `union`: O(N) — no balancing.

    - **Union by Rank + Path Compression**:  
      - `find` and `union`: O(α(N)) — nearly constant time in practice.
    """)


    if st.button("🔄 Run Benchmark"):
        times = {}

        qf = QuickFind(n)
        start = time.time()
        for x, y in operations:
            qf.union(x, y)
        times["Quick Find"] = time.time() - start

        qu = QuickUnion(n)
        start = time.time()
        for x, y in operations:
            qu.union(x, y)
        times["Quick Union"] = time.time() - start

        ubr = UnionByRank(n)
        start = time.time()
        for x, y in operations:
            ubr.union(x, y)
        times["Union by Rank"] = time.time() - start

        pco = PathCompressionOnly(n)
        start = time.time()
        for x, y in operations:
            pco.union(x, y)
        times["Path Compression"] = time.time() - start

        ubrpc = UnionByRankWithPathCompression(n)
        start = time.time()
        for x, y in operations:
            ubrpc.union(x, y)
        times["Rank + Path Compression"] = time.time() - start

        st.subheader("⏱ Time Benchmark")
        st.write(f"**Parametress:** {n} elements, {runs} operations")

        for name, t in times.items():
            st.write(f"**{name}**: {t:.5f} seconds")

        fig, ax = plt.subplots()
        ax.bar(times.keys(), times.values(), color=["blue", "red", "orange", "purple", "green"])
        ax.set_ylabel("Time (seconds)")
        ax.set_title("Comparasion of Union-Find")
        plt.xticks(rotation=15)
        st.pyplot(fig)

   