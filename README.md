# Walks that visit every vertex a bounded number of times are NP-complete

## Summary

A *walk* is a sequence of vertices in which consecutive vertices are adjacent. Vertices and edges may repeat, and the walk does not have to return to its start. Let K ≥ 1 be a fixed constant.

| Problem | Question | Complexity |
|---|---|---|
| EXACT-2 | Is there a walk that visits every vertex exactly twice? | NP-complete |
| ATMOST-2 | Is there a walk that visits every vertex at least once and at most twice? | NP-complete |
| EXACT-K | Is there a walk that visits every vertex exactly K times? | NP-complete for every fixed K ≥ 1 |
| ATMOST-K | Is there a walk that visits every vertex at least once and at most K times? | NP-complete for every fixed K ≥ 1 |

For K = 1, both EXACT-K and ATMOST-K are HAMILTONIAN PATH. For K ≥ 2, each reduces from HAMILTONIAN PATH by attaching a small gadget to every vertex:

- **ATMOST-K:** attach K−1 pendant leaves to every vertex.
- **EXACT-K:** attach K−1 pendant triangles to every vertex.

The proofs are below. `walks.py` checks both reductions exhaustively on every small graph, and no counterexample turned up.

## Why a gadget is needed

On the raw graph, neither problem is the same as HAMILTONIAN PATH:

- The path a–b–c has a Hamiltonian path but no exactly-twice walk. No two of the 4 visits to a and c can be consecutive, so they need at least 3 visits to b between them, but b allows only 2.
- The star with centre z and leaves p, q, r has no Hamiltonian path, but `p z q z r` visits every vertex at most twice.

Among connected graphs on 2 to 5 vertices, 7 give a different answer for EXACT-2 and 3 for ATMOST-2 (`python walks.py baseline`).

## Key lemma: walks as edge multisets

For a walk W, let m(e) be the number of times W traverses edge e, and let c(v) be the number of times W visits v.

Each visit to v in the middle of W uses 2 edge-ends at v, and a visit at either end of W uses 1. So, in the multigraph H with multiplicities m:

    deg_H(v) = 2·c(v) − ε(v)

Here ε(v) counts how many ends of W are v: ε = 1 at the start s and at the end t when s ≠ t, and ε(s) = 2 when s = t.

The converse holds by Euler's theorem. Take a multiplicity function whose support is connected and spans the graph, and whose degrees match 2·c(v) − ε(v) for one of these end patterns. Its Euler trail, or its Euler circuit started at s, is a walk with visit counts c.

For EXACT-K this means: G has a walk visiting every vertex exactly K times if and only if some multiplicity function on E(G) meets three conditions:

- its support is connected and spans every vertex;
- every degree is 2K;
- the only exceptions are two vertices of degree 2K−1, or one vertex of degree 2K−2.

`exact_euler` in `walks.py` decides EXACT-K this way. The checker also gives membership in NP when K is part of the input in binary: the multiplicities (each at most 2K) are a polynomial certificate. For fixed K the walk itself, with at most K·n entries, is the certificate.

## Reduction 1: ATMOST-K

**Construction.** Build G′ by attaching K−1 new pendant leaves ℓ₁, …, ℓ_{K−1} to every vertex v of G.

**Hamiltonian path ⇒ walk.** Follow a Hamiltonian path v₁ … vₙ of G, replacing each vᵢ with the block

    vᵢ ℓ₁ vᵢ ℓ₂ vᵢ … ℓ_{K−1} vᵢ

Each vᵢ is visited exactly K times and each leaf once.

**Walk ⇒ Hamiltonian path.** Let W be a walk in G′ that visits every vertex between 1 and K times. Fix a vertex v of G.

1. Every visit to a leaf of v is either an end of W or a stretch `v ℓ v`.
2. Cut W at its r_v ≤ K visits to v. This gives at most K−1 inner gaps, and a gap that contains a leaf is exactly that leaf.
3. Let e(v) be the number of ends of W that are leaves of v. Leaves that are not ends of W need at least K−1−e(v) of the gaps. So at most e(v) gaps are *real* excursions into the rest of G.
4. Delete every leaf from W and merge repeated consecutive entries. The result W_G is a walk in G that visits every vertex.
5. In W_G, vertex v appears at most 1 + e(v) times. If W starts (or ends) at a leaf of v, then W_G starts (or ends) at v.

So W_G visits every vertex once, except that its first and last vertex may repeat once for each end of W at one of their leaves. Delete the first entry of W_G if its vertex appears again later, then delete the last entry if its vertex appears again earlier. What remains visits every vertex exactly once, so it is a Hamiltonian path of G. ∎

## Reduction 2: EXACT-K

**Leaves fail here.** A leaf that is not an end of W, visited exactly K times, needs K separate `v ℓ v` stretches. That forces at least K+1 visits to its hub. So only the ends of a walk can be leaves, and leaves cannot be attached to every vertex. Triangles avoid the problem.

**Construction.** Build G′ by attaching K−1 pendant triangles to every vertex v of G. Each triangle has two new vertices a and b, with edges va, vb and ab.

**Hamiltonian path ⇒ walk.** Follow a Hamiltonian path v₁ … vₙ of G. At each vᵢ, take one detour per triangle:

    vᵢ (a b a b … a b) vᵢ

The detour visits a K times and b K times, and uses edge ab 2K−1 times. With K−1 detours, vᵢ is visited exactly K times, and the walk then moves on to vᵢ₊₁.

**Walk ⇒ Hamiltonian path.** Take the multigraph H given by the key lemma, with end deficits ε summing to 2. Assume n ≥ 2; the case n = 1 is trivial.

*Accounting at one hub v.* Consider a triangle (a, b) at v, and let x = m(ab).

- Then m(va) = 2K − ε(a) − x and m(vb) = 2K − ε(b) − x.
- The triangle *absorbs* α = m(va) + m(vb) = 4K − ε(a) − ε(b) − 2x of v's degree.
- H is connected, so α ≥ 1. α has the parity of ε(a) + ε(b), so α ≥ 2 unless ε(a) + ε(b) is odd.

Let g(v) be the degree of v along edges of G, and let D_v be the total deficit at v and its triangles.

- **Upper bound:** g(v) = 2K − ε(v) − Σα ≤ 2 − ε(v) + (number of triangles at v with odd deficit).
- **Parity:** g(v) has the parity of D_v.
- **Lower bound:** g(v) ≥ 1, because v must connect to the other vertices of G.

The deficits sum to 2 over all hubs, which leaves these cases:

| Deficit at v's hub | g(v) |
|---|---|
| D_v = 0 | 2 |
| D_v = 1, at v itself | 1 |
| D_v = 1, at a triangle vertex | 1 or 3 |
| D_v = 2, split across two different triangles at v | 2 or 4 |
| D_v = 2, at v itself | impossible (g(v) ≤ 0) |
| D_v = 2, any other split | 2 |

Let H_G be the multigraph formed by the G-edges of H.

- H_G spans G, because g(v) ≥ 1 for every v.
- H_G is connected. Each triangle meets the rest of H only at its hub, so a path in H between two vertices of G that enters a triangle must leave it through the same hub, and that detour can be cut out.

By the table, every degree in H_G is 2, apart from one of these exceptions:

- **(a)** two vertices with degree 1 or 3;
- **(b)** one vertex with degree 4;
- **(c)** none.

*Extracting a Hamiltonian path.*

- **(c)** H_G is a Hamiltonian cycle, or a doubled edge when n = 2.
- **(a)** Take the Euler trail from x to y. Each other vertex appears once, and x and y appear at most twice, with one copy at the very start and end. Delete the first entry if x repeats and the last entry if y repeats.
- **(b)** The Euler circuit has the form `v X v Y`. Then `X v Y` is a Hamiltonian path.

In every case G has a Hamiltonian path. ∎

The graph G′ has n + 2(K−1)n vertices, so the reduction is polynomial for every fixed K (and for K given in unary).

## Remarks

- **Lexicographic products.** EXACT-K on G is the same problem as HAMILTONIAN PATH on G[K̄_K], the graph in which every vertex becomes K non-adjacent copies. Label the i-th visit to v with the i-th copy. So HAMILTONIAN PATH stays NP-complete on graphs of the form G[K̄_K].
- **Closed walks.** Count the visits of a closed walk cyclically, so its shared start and end is one visit, not two. Then every deficit is 0, and the same triangle gadget reduces HAMILTONIAN CYCLE on graphs with n ≥ 3 to the closed version of EXACT-K. This is case (c): H_G is connected with every degree 2. For n ≥ 3 that makes H_G a Hamiltonian cycle, because a doubled edge would use up the degree of both its ends and form a 2-vertex component. Graphs with n ≤ 2 have no Hamiltonian cycle, and the reduction maps them to a fixed no-instance. (Without that special case, K₂ breaks the reduction: case (c) gives a doubled edge.) `walks.py` does not check this.
- **Large K.** ATMOST-K is easy once K ≥ n − 1. For n ≥ 2, take a spanning tree T, walk around it from any vertex, and stop just before the final return to the start. This walk visits each vertex v exactly deg_T(v) ≤ n − 1 times, so the question becomes "is G connected?". Hardness needs K to be a fixed constant, or at least K < n − 1.
- **Walks only.** These results are for walks. If edges may not repeat (trails), both gadgets break: a leaf forces its edge to be used twice, and a triangle reuses ab. The trail versions are not covered here.

## Verification (`walks.py`)

**Method.**

- **Graphs tested:** every graph up to the stated size, one per isomorphism class.
- **Check:** "G has a Hamiltonian path" must equal "G′ has the required walk".
- **Deciders:** two independent ones.
  - `walk_dfs` searches walks straight from the definition. It memoises (vertex, visit-count) states, and prunes a state when some vertex still short of its count can no longer be reached.
  - `exact_euler` is the multiplicity search from the key lemma.
- **Agreement:** the two deciders agree on all 683 instances of the `crosscheck` check:
  - raw graphs with n ≤ 6 and K = 1, 2, 3;
  - EXACT-2 gadget graphs with n ≤ 5;
  - EXACT-3 gadget graphs with n ≤ 3.

| Check | Gadget | Graphs (n ≤) | With a Hamiltonian path | Mismatches |
|---|---|---|---|---|
| `atmost2` | 1 leaf per vertex | 208 (6) | 118 | 0 |
| `atmost3` | 2 leaves per vertex | 52 (5) | 27 | 0 |
| `atmost4` | 3 leaves per vertex | 18 (4) | 9 | 0 |
| `exact2-dfs` | 1 triangle per vertex | 208 (6) | 118 | 0 |
| `exact2-euler` | 1 triangle per vertex | 208 (6) | 118 | 0 |
| `exact3-euler` | 2 triangles per vertex | 52 (5) | 27 | 0 |
| `exact4-euler` | 3 triangles per vertex | 52 (5) | 27 | 0 |
| `exact5-euler` | 4 triangles per vertex | 18 (4) | 9 | 0 |
| `exact3-dfs`\* | 2 triangles per vertex | 18 (4) | 9 | 0 |

\* `exact3-dfs` is not in the default run; it takes about 4 minutes.

These exhaustive checks are evidence that the gadgets behave as the proofs say, not a proof on their own. They would have caught a wrong gadget: without one, the answers differ from HAMILTONIAN PATH (see *Why a gadget is needed*).

### Running it

Python 3, standard library only.

```
python walks.py              # all default checks, about 4 minutes
python walks.py --list       # list the checks
python walks.py exact4-euler # run selected checks
```

Listing the graphs on 6 vertices takes about 50 seconds the first time; later checks in the same run reuse the list. The script exits non-zero if any check fails.
