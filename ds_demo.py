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
    Disjoint Set (или Union-Find) — структура данных для работы с непересекающимися множествами.
    Позволяет эффективно объединять множества и находить их корни.
    Используется в задачах на графы, например, для нахождения минимального остовного дерева (MST).
                Ссылка на презентацию: https://docs.google.com/presentation/d/12VCENn-07ZMsSt0ZlJj_YpXNWtR3aEeNlLp6KD0PGf8/edit#slide=id.g20e53a1f10d_0_135
    """)
        
    st.subheader("🧠 Task #1 — Quick Find")
    st.markdown("""
    Quick Find — простая реализация Disjoint Set, где каждый элемент хранит свой ID-компоненты.  
    - **Union:** O(N)  
    - **Find:** O(1)  
    - **Space:** O(N)
    """)
    st.code("""
    class QuickFind:
        def __init__(self, n):
            self.id = list(range(n))

        def find(self, x):
            return self.id[x]

        def union(self, x, y):
            pid = self.id[x]
            qid = self.id[y]
            for i in range(len(self.id)):
                if self.id[i] == pid:
                    self.id[i] = qid
    """)

    st.subheader("🧠 Task #2 — Quick Union")
    st.markdown("""
    Quick Union — улучшение, где хранятся ссылки на родителя.  
    - **Union:** O(N)  
    - **Find:** O(N)  
    - **Space:** O(N)  
    **Разница с Quick Find:** union быстрее, но find медленнее.
    """)
    st.code("""
    class QuickUnion:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, x):
            while x != self.parent[x]:
                x = self.parent[x]
            return x

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            self.parent[root_x] = root_y
    """)

    st.subheader("🧠 Task #3 — Union by Rank")
    st.markdown("""
    Union by Rank — к Quick Union добавляем высоту (ранг) дерева, чтобы соединять меньшие по высоте под большими.  
    - **Union:** O(log N)  
    - **Find:** O(log N)
        """)
        
    st.code("""
    class UnionByRank:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, x):
            while x != self.parent[x]:
                x = self.parent[x]
            return x

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

    st.subheader("🧠 Task #4 — Path Compression")
    st.markdown("""
    Path Compression ускоряет find, делая все узлы по пути напрямую связанными с корнем.  
    - **Union:** O(log N)  
    - **Find:** O(log N) → O(α(N)) в амортизированном.
        """)
    st.code("""
    class PathCompression:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                self.parent[root_x] = root_y
            """)

    st.subheader("🧠 Task #5 — Union by Rank + Path Compression")
    st.markdown("""
    Лучшая реализация Disjoint Set: два подхода вместе.  
    - **Union & Find:** O(α(N)) — почти константа  
    - **Space:** O(N)
        """)
    st.code("""
    class UnionByRankWithPathCompression:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
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

    if st.button("🎲 Случайные параметры"):
        st.session_state.n = random.randint(10, 100_000)
        st.session_state.runs = random.randint(10, 100_000)
        st.rerun()

    n = st.slider("Количество элементов", 10, 100_000, st.session_state.n, step=1000)
    runs = st.slider("Количество операций union/find", 10, 100_000, st.session_state.runs, step=1000)

    st.session_state.n = n
    st.session_state.runs = runs

    st.subheader("📊 Теоретическая сложность (Big-O)")

    st.markdown("""
    - **Quick Union**: O(N) — find и union в худшем случае.
    - **Union by Rank**: O(log N) — дерево сбалансировано.
    - **Union by Rank + Path Compression**: O(α(N)) — почти O(1) в реальности.
    """)

    if st.button("🚀 Старт замера"):
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

        st.subheader("⏱ Время выполнения")
        st.write(f"**Параметры:** {n} элементов, {runs} операций")

        for name, t in times.items():
            st.write(f"**{name}**: {t:.5f} сек")

        fig, ax = plt.subplots()
        ax.bar(times.keys(), times.values(), color=["blue", "red", "orange", "purple", "green"])
        ax.set_ylabel("Время (сек)")
        ax.set_title("Сравнение производительности Union-Find")
        plt.xticks(rotation=15)
        st.pyplot(fig)

   