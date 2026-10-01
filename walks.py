"""Exhaustive small-graph checks for the NP-hardness of four walk problems.

A walk is a vertex sequence in which consecutive vertices are adjacent; vertices and
edges may repeat. For a graph G and a fixed K >= 1:

  EXACT-K    does G have a walk that visits every vertex exactly K times?
  ATMOST-K   does G have a walk that visits every vertex at least once and at most K times?

Both reduce from HAMILTONIAN PATH (K = 1 is HAMILTONIAN PATH itself):

  ATMOST-K   attach K-1 pendant leaves to every vertex
  EXACT-K    attach K-1 pendant triangles to every vertex

For every graph on up to n vertices (one per isomorphism class) a check asserts
"G has a Hamiltonian path"  ==  "the gadget graph has the required walk".

Two independent deciders are used:
  walk_dfs      searches walks directly from the definition (any lo..hi visit bounds)
  exact_euler   EXACT-K only: searches edge multiplicities and applies Euler's theorem;
                much faster on the larger gadget graphs. The 'crosscheck' check
                confirms it agrees with walk_dfs.

Usage:  python walks.py             run the default checks
        python walks.py --list      list every check
        python walks.py NAME ...    run the named checks
"""
import functools
import itertools
import sys
import time

sys.setrecursionlimit(10000)


# ---------------------------------------------------------------- graphs

def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    return adj


def reachable(n, edges, start=0):
    adj = adjacency(n, edges)
    seen, stack = {start}, [start]
    while stack:
        for y in adj[stack.pop()]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return seen


def is_connected(n, edges):
    return len(reachable(n, edges)) == n


@functools.lru_cache(maxsize=None)
def graphs_up_to_iso(n):
    """One edge list per isomorphism class of graphs on n vertices."""
    pairs = list(itertools.combinations(range(n), 2))
    perms = list(itertools.permutations(range(n)))
    seen, out = set(), []
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        canon = min(tuple(sorted(tuple(sorted((p[a], p[b]))) for a, b in edges)) for p in perms)
        if canon not in seen:
            seen.add(canon)
            out.append(edges)
    return out


def all_graphs(nmax):
    for n in range(1, nmax + 1):
        for edges in graphs_up_to_iso(n):
            yield n, edges


# ---------------------------------------------------------------- gadgets

def add_leaves(n, edges, k):
    """Attach k pendant leaves to every vertex."""
    out, m = list(edges), n
    for v in range(n):
        for _ in range(k):
            out.append((v, m))
            m += 1
    return m, out


def add_triangles(n, edges, k):
    """Attach k pendant triangles v-a-b to every vertex v."""
    out, m = list(edges), n
    for v in range(n):
        for _ in range(k):
            a, b = m, m + 1
            m += 2
            out += [(v, a), (v, b), (a, b)]
    return m, out


# ---------------------------------------------------------------- deciders

def walk_dfs(n, edges, lo, hi):
    """Is there a walk visiting every vertex at least lo and at most hi times?"""
    adj = adjacency(n, edges)
    base = [(hi + 1) ** i for i in range(n)]
    cnt = [0] * n
    dead = set()  # (vertex, count vector) states known to fail

    def dfs(cur, code, done):  # done = #vertices already visited >= lo times
        if done == n:
            return True
        key = code * n + cur
        if key in dead:
            return False
        # prune: every vertex still short of lo must be reachable from cur via vertices below hi
        seen, stack = {cur}, [cur]
        while stack:
            for y in adj[stack.pop()]:
                if y not in seen and cnt[y] < hi:
                    seen.add(y)
                    stack.append(y)
        if any(cnt[v] < lo and v not in seen for v in range(n)):
            dead.add(key)
            return False
        for u in adj[cur]:
            if cnt[u] < hi:
                cnt[u] += 1
                found = dfs(u, code + base[u], done + (cnt[u] == lo))
                cnt[u] -= 1
                if found:
                    return True
        dead.add(key)
        return False

    for s in range(n):
        cnt[s] = 1
        found = dfs(s, base[s], int(lo <= 1))
        cnt[s] = 0
        if found:
            return True
    return False


def ham_path(n, edges):
    return walk_dfs(n, edges, 1, 1)


def exact_euler(n, edges, k):
    """EXACT-K via Euler's theorem.

    A walk visiting every vertex exactly k times exists iff there are edge
    multiplicities m >= 0 whose support is connected and spans every vertex, with
    degree 2k - d(v) at each vertex v. The deficit d marks the walk's ends: d = 1 at
    two distinct vertices s, t (walk from s to t), or d = 2 at a single vertex s
    (walk from s back to s).
    """
    if n == 1:
        return k == 1
    inc = [[] for _ in range(n)]
    for i, (a, b) in enumerate(edges):
        inc[a].append(i)
        inc[b].append(i)
    patterns = [{s: 2} for s in range(n)]
    patterns += [{s: 1, t: 1} for s, t in itertools.combinations(range(n), 2)]
    return any(_realise(n, edges, inc, [2 * k - p.get(v, 0) for v in range(n)]) for p in patterns)


def _realise(n, edges, inc, need):
    """Backtrack for multiplicities with degree exactly need[v] and connected spanning support."""
    m = [None] * len(edges)          # None = not yet assigned
    free = [len(inc[v]) for v in range(n)]

    def still_connectable():
        live = [e for i, e in enumerate(edges) if m[i] is None or m[i] > 0]
        return is_connected(n, live)

    def step():
        if any(free[v] == 0 and need[v] != 0 for v in range(n)):
            return False
        if not still_connectable():
            return False
        open_vertices = [v for v in range(n) if free[v]]
        if not open_vertices:
            return True
        v = min(open_vertices, key=lambda x: free[x])
        return spread(v, [e for e in inc[v] if m[e] is None], 0)

    def spread(v, es, i):  # split need[v] over v's unassigned edges es[i:]
        e = es[i]
        a, b = edges[e]
        u = b if a == v else a
        if i == len(es) - 1:
            choices = [need[v]] if need[v] <= need[u] else []
        else:
            choices = range(min(need[v], need[u]) + 1)
        for x in choices:
            m[e] = x
            need[v] -= x; need[u] -= x; free[v] -= 1; free[u] -= 1
            ok = spread(v, es, i + 1) if i + 1 < len(es) else step()
            m[e] = None
            need[v] += x; need[u] += x; free[v] += 1; free[u] += 1
            if ok:
                return True
        return False

    return step()


# ---------------------------------------------------------------- checks

PROBLEMS = {
    # name: (gadget, decider(n, edges, k))
    "atmost": (add_leaves, lambda n, e, k: walk_dfs(n, e, 1, k)),
    "exact-dfs": (add_triangles, lambda n, e, k: walk_dfs(n, e, k, k)),
    "exact-euler": (add_triangles, exact_euler),
}


def check_reduction(problem, k, nmax):
    gadget, decide = PROBLEMS[problem]
    total = yes = 0
    bad = []
    for n, edges in all_graphs(nmax):
        hp = ham_path(n, edges)
        m, edges2 = gadget(n, edges, k - 1)
        total += 1
        yes += hp
        if hp != decide(m, edges2, k):
            bad.append(edges)
    ok = not bad
    return ok, f"{total} graphs, n <= {nmax} ({yes} with a Hamiltonian path); mismatches: {len(bad)} {bad[:3]}"


def check_baseline(nmax):
    """The gadgets are needed: on raw connected graphs the answers differ from HAMILTONIAN PATH."""
    lines = []
    for label, lo, hi in [("EXACT-2", 2, 2), ("ATMOST-2", 1, 2)]:
        diff = [e for n, e in all_graphs(nmax)
                if n > 1 and is_connected(n, e) and ham_path(n, e) != walk_dfs(n, e, lo, hi)]
        lines.append(f"{label}: {len(diff)} connected graphs differ, e.g. {diff[:2]}")
    return True, "; ".join(lines)


def check_crosscheck(nmax):
    """exact_euler must agree with walk_dfs, on raw graphs and on gadget graphs."""
    total, bad = 0, []
    for n, edges in all_graphs(nmax):
        cases = [(n, edges, k) for k in (1, 2, 3)]
        if n <= 5:
            cases.append((*add_triangles(n, edges, 1), 2))
        if n <= 3:
            cases.append((*add_triangles(n, edges, 2), 3))
        for m, e, k in cases:
            total += 1
            if walk_dfs(m, e, k, k) != exact_euler(m, e, k):
                bad.append((e, k))
    return not bad, (f"{total} instances (raw graphs n <= {nmax} with K = 1, 2, 3; EXACT-2 gadget graphs n <= 5; "
                     f"EXACT-3 gadget graphs n <= 3); disagreements: {len(bad)} {bad[:3]}")


CHECKS = {
    # name: (description, run, in default run)
    "baseline":     ("raw graphs differ from HamPath (gadgets are needed)", lambda: check_baseline(5), True),
    "crosscheck":   ("Euler decider == walk DFS decider",                   lambda: check_crosscheck(6), True),
    "atmost2":      ("ATMOST-2, 1 leaf per vertex",                         lambda: check_reduction("atmost", 2, 6), True),
    "atmost3":      ("ATMOST-3, 2 leaves per vertex",                       lambda: check_reduction("atmost", 3, 5), True),
    "atmost4":      ("ATMOST-4, 3 leaves per vertex",                       lambda: check_reduction("atmost", 4, 4), True),
    "exact2-dfs":   ("EXACT-2, 1 triangle per vertex (walk DFS)",           lambda: check_reduction("exact-dfs", 2, 6), True),
    "exact2-euler": ("EXACT-2, 1 triangle per vertex (Euler)",              lambda: check_reduction("exact-euler", 2, 6), True),
    "exact3-euler": ("EXACT-3, 2 triangles per vertex (Euler)",             lambda: check_reduction("exact-euler", 3, 5), True),
    "exact4-euler": ("EXACT-4, 3 triangles per vertex (Euler)",             lambda: check_reduction("exact-euler", 4, 5), True),
    "exact5-euler": ("EXACT-5, 4 triangles per vertex (Euler)",             lambda: check_reduction("exact-euler", 5, 4), True),
    # slow (minutes): direct walk search on the larger gadget graphs
    "exact3-dfs":   ("EXACT-3, 2 triangles per vertex (walk DFS, slow)",    lambda: check_reduction("exact-dfs", 3, 4), False),
}
DEFAULT = [name for name, (_, _, default) in CHECKS.items() if default]


def main(argv):
    if "--list" in argv:
        for name, (desc, _, default) in CHECKS.items():
            print(f"{name:13} {desc}{'' if default else '  [not run by default]'}")
        return 0
    names = argv or DEFAULT
    unknown = [x for x in names if x not in CHECKS]
    if unknown:
        print(f"unknown check(s): {unknown}; see --list")
        return 2
    failed = 0
    for name in names:
        desc, run, _ = CHECKS[name]
        t = time.time()
        ok, detail = run()
        failed += not ok
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {desc} -- {detail} ({time.time() - t:.1f}s)", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
