# Prior work on spanning walks that visit every vertex at most k times (k-walks), and their complexity

Scope: does the literature already contain the result that ATMOST-K is NP-complete for every fixed K (open walk, or closed walk), proved by attaching K−1 pendant leaves to every vertex? Every claim below has a source. Labels used: **[EXPLICIT]** = stated in a paper; **[COROLLARY]** = follows easily but no paper found that says it; **[NOT FOUND]**.

Bottom line: the **closed-walk** version (a "k-walk") is **explicitly** NP-complete for every fixed k. Jackson & Wormald (1990), Theorem 6.1, prove this from HAMILTON CYCLE. Their construction with j = 1 is exactly the pendant-leaf construction: attach k−1 pendant vertices to every vertex. They say the result goes back to Broersma (Broersma & Göbel 1990). The **open-walk** version (the repo's ATMOST-K, which reduces from HAMILTONIAN PATH) was **not found stated anywhere**. It is the obvious open-walk analogue of the Jackson–Wormald proof, so it should be called an easy corollary or folklore, not a new result.

---

## Q1. What did Jackson & Wormald (1990) prove, and is the complexity of deciding "does G have a k-walk" (fixed k ≥ 2) published?

### Takeaway
Yes. Jackson & Wormald, "k-walks of graphs", Australas. J. Combin. 2 (1990) 135–146, Section 6 "NP-completeness of k-walk problems", Theorem 6.1: for fixed k and j, K-WALK IN J-CONNECTED GRAPH and EXACT K-WALK IN J-CONNECTED GRAPH are NP-complete. The proof is a reduction from HAMILTON CYCLE. For j = 1 the gadget is "attach k−1 pendant vertices to every vertex". They also say the plain (j = 1) NP-completeness already follows from Broersma's earlier proof.

### Cited Findings
- **Bibliographic record:** Bill Jackson and Nicholas C. Wormald, "k-walks of graphs", *Australasian Journal of Combinatorics* 2 (1990), pp. 135–146. — [AJC landing page](https://ajc-new.maths.uq.edu.au/v2.p135); [PDF](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Abstract (verbatim):** "We obtain various sufficient conditions for a graph to have a spanning closed walk meeting each vertex exactly k times or meeting each vertex at most k times. In particular, we generalise the result of Oberly and Sumner that every connected, locally connected K_{1,3}-free graph with at least three vertices is hamiltonian." — [PDF](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Definition (closed walks only):** "An exact k-walk (or k-walk) of G is a connected spanning subgraph W of (2k)×G, such that the degree of each vertex v in W is 2k (or is an even number which is at most 2k, respectively)." By Euler's theorem, "a graph with a k-walk (or exact k-walk) possesses a closed walk passing through each vertex at most k times (or exactly k times, respectively)." For graphs with at least 3 vertices, every 1-walk is a Hamilton cycle. — [PDF](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Composition equivalence:** for k ≥ 2, G has a k-walk (or exact k-walk) iff the composition G[K̄_k] (or G[K_k]) has a Hamilton cycle. The paper says it uses "a similar connection in examining the complexity of finding k-walks (see Section 6)". — [PDF](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Section 6, opening paragraph (verbatim, checked against the page image):** "It was shown in [B2] that the problem of whether a given graph has an exact k-walk is NP-complete. The proof was by transformation of an arbitrary graph G to a graph G′ such that G has a Hamilton cycle iff G′ has an exact k-walk. ... In fact, with the proof given, G has a Hamilton cycle iff G′ has any k-walk, and thus the question of whether a given graph has a k-walk is NP-complete. However, the graphs G′ have many cut-vertices, and so it is natural to ask whether the restriction of the question to more highly connected graphs is still NP-complete." — [PDF, p. 145](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Problems stated in Garey–Johnson style:** "K-WALK IN J-CONNECTED GRAPH. Instance: j-connected graph G. Question: Does G have a k-walk?" and "EXACT K-WALK IN J-CONNECTED GRAPH. Instance: j-connected graph G. Question: Does G have an exact k-walk?" — [PDF, p. 145](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Theorem 6.1 (verbatim):** "For k and j fixed, K-WALK IN J-CONNECTED GRAPH and EXACT K-WALK IN J-CONNECTED GRAPH are NP-complete." — [PDF, p. 145](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Proof of Theorem 6.1 (verbatim, checked against the page image because the OCR text drops words):** "We give a polynomial reduction from HAMILTON CYCLE to each problem. Let G be an arbitrary graph with |V(G)| ≥ 2, and form the composition H = G[K_j]. To each inflated vertex of H (in the terminology of the proof of Theorem 5.1), join jk − 1 separate copies of K_j, to obtain G′. Then a k-walk in G′ uses at most two edges of H incident with any inflated vertex, and so yields a 1-walk of G. The converse also holds. In addition, G′ is j-connected. Thus, we have reduced HAMILTON CYCLE to K-WALK IN J-CONNECTED GRAPH. The proof for exact k-walks is exactly the same since if G has a 1-walk it follows that G′ has an exact k-walk." — [PDF, p. 145](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Prior and parallel credit:** the acknowledgement says some results, including "a generalisation of Theorem 6.1", "were obtained, amongst other things, independently very recently by Pruesse [P]". [P] = G. Pruesse, "A Generalization of Hamiltonicity", M.Sc. Thesis, University of Toronto (1990). [B2] = "H. Broersma, k-traceable graphs (submitted to Discrete Math.)". — [PDF, pp. 145–146](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Published form of [B2]:** a 2024 paper cites it as "[BG90] H.J. Broersma and F. Göbel, 'k-Traversable graphs', Ars Combinatoria 29A (1990), pp. 141–153". It summarises: "In 1990, Broersma and Göbel proposed two variants of the Hamiltonian cycle problem: for fixed k, is there a closed walk that visits each vertex exactly k times, or at least once and at most k times, respectively? They showed that for constant k, both of these problems are NP-hard [BG90]. Jackson and Wormald subsequently proved that both problems remain NP-hard in j-connected graphs for any constant j [JW90]." — [Liu, Sheffield, Westover, arXiv:2405.16270](https://arxiv.org/html/2405.16270)
- **Other main results of Jackson–Wormald, for context:**
  - Lemma 2.1(i): a graph with a k-walk is 1/k-tough.
  - Lemma 2.2: (i) a k-tree (spanning tree of max degree ≤ k) gives a k-walk, by doubling its edges; (ii) a k-walk gives a (k+1)-tree.
  - Corollary 2.4, via Sein Win's theorem: if c(G−S) ≤ (k−2)|S| + 2 for all S, then G has a k-walk.
  - Conjecture 2.1: every 1/(k−1)-tough graph has a k-walk (k ≥ 2).
  - Theorem 3.1: every connected K_{1,k+1}-free graph has a k-walk.
  - Theorem 5.1: δ(G) > (|V|−1)/(k+1) implies a k-walk.
  - Theorem 5.7: every 3-connected planar graph has a 3-walk. Conjecture 5.1: it has a 2-walk.

  — [PDF](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **Pendant-vertex gadgets also appear elsewhere in the same paper:** Remark 2.1 builds a graph with no k-walk starting from "the graph obtained from K_3 by attaching k pendant vertices at each of the three vertices". — [PDF, p. 137](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- **The standard modern definition follows Jackson–Wormald:** "A k-walk in a graph is a spanning closed walk using each vertex at most k times. When k = 1, a 1-walk is a Hamilton cycle." — [WEGA graph-theory wiki, "K-Walk"](https://pco.iis.nsk.su/wega/index.php/K-Walk). Kaiser et al. use the same: "Following Jackson and Wormald [6], we define a k-walk in a graph G to be a closed spanning walk visiting each vertex at most k times." — [Kaiser, Kužel, Li, Wang, "A note on k-walks in bridgeless graphs"](http://home.zcu.cz/~kaisert/papers/deg-walk.pdf)

### Inferences
- With j = 1, the Theorem 6.1 construction is H = G[K_1] = G, plus jk − 1 = k − 1 separate copies of K_1 (single pendant vertices) joined to each vertex. That is exactly "attach k−1 pendant leaves to every vertex", reduced from HAMILTON CYCLE. So the repo's closed-walk remark, and its pendant-leaf technique, are already explicitly in print (1990) for the closed version.
- k is fixed in Theorem 6.1. NP-completeness when k is part of the input follows at once, since the problem is in NP: a k-walk has at most kn vertex occurrences.
- Jackson–Wormald give Broersma's paper as the source of the original closed-walk NP-completeness, and say the at-most-k version follows "with the proof given". The precise first-published statement should therefore be credited to Broersma & Göbel (1990) and/or Jackson & Wormald (1990), with Pruesse (1990, M.Sc. thesis) as independent work.

### Gaps
- I could not get the full text of Broersma & Göbel, "k-Traversable graphs", Ars Combin. 29A (1990) 141–153. Unconfirmed: its exact theorem statement; the form of its gadget (Jackson–Wormald say only that G′ "has many cut-vertices"); whether it states the at-most-k version itself or only the exact-k version. Liu et al. (2024) say "both" were shown; Jackson–Wormald (1990) say only the exact version was shown and that the at-most version follows from the same proof. The two accounts differ slightly.
- Broersma's preprint was titled "k-traceable graphs". "Traceable" usually means having a Hamiltonian path, so the paper might also treat open walks. This could not be checked.
- Pruesse's M.Sc. thesis (Toronto 1990) is not indexed online. A search found only Pruesse's 1992 Ph.D. ("Generating Linear Extensions by Transpositions"), so the content of the "generalisation of Theorem 6.1" is unknown. — [Math Genealogy: Gara Pruesse](https://mathgenealogy.org/id.php?id=103665)
- Minor: Liu et al. cite the Jackson–Wormald title as "k-walks in graphs". The paper itself is titled "k-walks of Graphs".

---

## Q2. Is there a known result for OPEN spanning walks visiting each vertex at most k times?

### Takeaway
**[NOT FOUND]** as an explicit statement. I found no paper defining an "open k-walk" or stating NP-completeness of the open (path-like) version for fixed k ≥ 2. The k-walk literature uses closed walks throughout. The open version is an easy corollary **[COROLLARY]**: the same pendant-leaf construction, reduced from HAMILTONIAN PATH instead of HAMILTON CYCLE. The nearest explicit open-type result is Singh & Zenklusen's NP-completeness of "containing a k-trail" (homomorphic images of max-degree-k trees; for k = 2 this is a spanning trail), which also uses k−2 pendant leaves per vertex.

### Cited Findings
- Every definition found is closed:
  - Jackson–Wormald: "spanning closed walk" — [PDF](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
  - WEGA: "spanning closed walk" — [WEGA](https://pco.iis.nsk.su/wega/index.php/K-Walk)
  - Kaiser et al.: "closed spanning walk" — [Kaiser et al.](http://home.zcu.cz/~kaisert/papers/deg-walk.pdf)
  - Gao & Pasechnik: "A k-walk is a spanning subgraph W of 2k×G such that each vertex of W has even degree at most 2k", i.e. the closed Eulerian definition — [Gao & Pasechnik, arXiv:1412.0514](https://arxiv.org/html/1412.0514v4)
- Liu–Sheffield–Westover (2024) study only closed walks ("[a,b]-HAM: ... does there exist a closed walk in G that visits every vertex at least a times and at most b times?"). The open/traceable version is not discussed. — [arXiv:2405.16270](https://arxiv.org/abs/2405.16270)
- **k-trails (Singh & Zenklusen).** M. Singh and R. Zenklusen, "k-Trails: Recognition, Complexity, and Approximations", arXiv:1512.01781 (Dec 2015). Results stated by the source:
  - Definition 2: G is a k-trail if it is "the homomorphic image of a connected graph H with maximum degree at most k".
  - Theorem 1.3: "For any k ≥ 2, the problem of deciding whether a graph contains a k-trail is NP-complete."
  - Theorem 1.4: if G contains a k-trail then it is a (k+1)-trail.
  - Proof of Theorem 1.3: reduction from Hamiltonian path in cubic graphs. "For each vertex v ∈ Ṽ, we introduce a new set of vertices v_i, 1 ≤ i ≤ k − 2 and connect them to v via the edge (v, v_i)." This is again a pendant-leaf construction.

  The paper does not cite Jackson–Wormald or Broersma. — [arXiv:1512.01781](https://arxiv.org/abs/1512.01781)
- The search also turned up the repo under review ("myticalcat/k-walks-completeness"), which states the open ATMOST-K result. It is not independent prior work. — [GitHub](https://github.com/myticalcat/k-walks-completeness)

### Inferences
- Checking the open-walk reduction for completeness (my own argument, not from a source). Let G′ be G with K−1 pendant leaves attached to each vertex.
  - (⇒) Given a Hamiltonian path v_1…v_n, insert v ℓ v detours at each vertex, and start and end the walk at leaves of v_1 and v_n. Interior vertices are visited K times; endpoint vertices K−1 times.
  - (⇐) Drop the leaves from the walk and merge repeated vertices. Each vertex then appears in one contiguous block, except that a vertex whose leaf is an endpoint of the walk can appear in up to 1 + (number of its leaves used as endpoints) blocks. Only the first and last blocks of the projected walk can be redundant. Deleting them leaves a Hamiltonian path.

  So ATMOST-K (open) is NP-complete for fixed K. The proof is the open-walk transcription of Jackson–Wormald's Theorem 6.1 with j = 1. Fair wording: "folklore / easy corollary of Jackson–Wormald 1990 (and Broersma–Göbel 1990)", not new.
- Lemma 2.2 of Jackson–Wormald carries over to open walks by the same arguments: doubling-tree / DFS-tour, and "first-entry edges". So the open version is sandwiched between max-degree-k and max-degree-(k+1) spanning trees, as in the closed case.
- Since the 2-trail case means "has a spanning trail" (an open walk with no repeated edges), Singh–Zenklusen is related but measures something different: preimage-tree degree and edge-disjointness, not visit counts.

### Gaps
- I did not search MathSciNet/zbMATH (not available). An open-walk statement might exist in a less-indexed paper, a thesis (e.g. Pruesse 1990, or Broersma's "k-traceable graphs"), or an exercise collection.
- I did not find the related "open Hamiltonian walk" literature (minimum-length open spanning walks, e.g. Vacek 1991) online. It concerns walk length, not per-vertex visit bounds.

---

## Q3. Relation to degree-bounded spanning trees; has anyone noted the pendant-leaf reduction for k-walks? Do the later k-walk / k-tree / k-trail papers comment on complexity?

### Takeaway
The k-tree ⇄ k-walk link is explicit in Jackson–Wormald (Lemma 2.2). The pendant-leaf reduction appears explicitly in three places:
- for k-walks: Jackson–Wormald Theorem 6.1 with j = 1;
- for k-trails: Singh–Zenklusen Theorem 1.3, with k−2 leaves;
- for degree-bounded spanning trees: standard (Garey–Johnson ND1, from HAMILTONIAN PATH; e.g. the UIUC CS 374 exercise attaches a "fan" of pendant edges).

The structural k-walk papers I checked (Kaiser et al. 2006/07; Gao & Pasechnik 2015) do not discuss NP-hardness.

### Cited Findings
- Jackson–Wormald Lemma 2.2: "(i) If G contains a k-tree then G has a k-walk. (ii) If G has a k-walk then G contains a (k+1)-tree." Proof of (i): "Doubling the edges in a k-tree in G yields a k-walk of G." Proof of (ii): delete from an Euler tour every edge entering a previously visited vertex. "A k-tree of a graph is a spanning tree with maximum degree k." — [PDF, p. 137](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- Win's theorem as used by Jackson–Wormald: "Theorem 2.3 [SW] If G is connected, k ≥ 2, and, for any subset S of V(G), c(G − S) ≤ (k − 2)|S| + 2, then G has a k-tree." Citation: Sein Win, "On a connection between the existence of k-trees and the toughness of a graph", *Graphs and Combinatorics* 5 (1989) 201–205. — [PDF](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- Degree-constrained spanning tree: "This problem is NP-complete (Garey & Johnson 1979). This can be shown by a reduction from the Hamiltonian path problem. It remains NP-complete even if k is fixed to a value ≥ 2." Fürer & Raghavachari (1994) find in polynomial time a spanning tree of max degree ≤ Δ* + 1, where Δ* is the optimum. — [Wikipedia, Degree-constrained spanning tree](https://en.wikipedia.org/wiki/Degree-constrained_spanning_tree)
- Folklore pendant-leaf (fan) reduction for bounded-degree spanning trees, as a homework exercise: "does G have a spanning tree in which every node has degree at most 374? ... a reduction from the undirected Hamiltonian path problem. Given an arbitrary graph G, let H be the graph obtained by attaching a fan of 372 edges to every vertex of G." — [UIUC CS/ECE 374, Lab 14 Solutions, Spring 2017](https://courses.grainger.illinois.edu/cs374/sp2017/labs/solutions/lab14-sol.pdf)
- Singh–Zenklusen's k-trail hardness proof uses k−2 pendant vertices per vertex of a cubic graph, reduced from Hamiltonian path in cubic graphs. — [arXiv:1512.01781](https://arxiv.org/abs/1512.01781)
- Kaiser, Kužel, Li, Wang, "A note on k-walks in bridgeless graphs" (LRI research report RR1444, 2006). Abstract: "We show that every bridgeless graph of maximum degree Δ has a spanning ⌈(Δ+1)/2⌉-walk. The bound is optimal." It notes: "For general graphs, this problem is trivial since a tree of maximum degree Δ has a Δ-walk [6], and it clearly does not admit any k-walk with k < Δ." No NP-hardness discussion found in the text. — [author PDF](http://home.zcu.cz/~kaisert/papers/deg-walk.pdf); [LRI report](https://www.lri.fr/~bibli/Rapports-internes/2006/RR1444.pdf)
- Gao Mou & Dmitrii V. Pasechnik, "Edge-dominating cycles, k-walks and Hamilton prisms in 2K₂-free graphs" (arXiv:1412.0514v4, Dec 2015): "For any integer k≥2, every 1/(k−1)-tough 2K₂-free graph G admits a k-walk. Moreover, the latter can be found in time polynomial in |V(G)|." No NP-hardness discussion. — [arXiv:1412.0514](https://arxiv.org/html/1412.0514v4)
- Search snippets (I did not read the full texts) say Ellingham and co-authors proved the Jackson–Wormald toughness conjecture for restricted classes: K₄-minor-free graphs, and P₄-free graphs, where "a P4-free graph has a spanning k-walk if and only if it is 1/k-tough". — [Ellingham et al., Toughness and spanning trees in K4-minor-free graphs, arXiv:1704.00246](https://arxiv.org/pdf/1704.00246); [Ellingham et al., Toughness and prism-hamiltonicity of P4-free graphs, arXiv:1901.01959](https://arxiv.org/pdf/1901.01959)

### Inferences
- The "pendant-leaf" idea is a long-standing, standard technique in this area, used in at least three closely related settings: k-walks, degree-bounded spanning trees, and k-trails. The repo's reduction is a direct instance of it.
- Combining Jackson–Wormald Lemma 2.2 with Fürer–Raghavachari gives a polynomial-time additive approximation of the least k for which a (closed) k-walk exists. If Δ* is the minimum max-degree of a spanning tree, the optimum k lies in {Δ* − 1, Δ*}, and Fürer–Raghavachari give a (Δ*+1)-tree, hence a (Δ*+1)-walk (additive error ≤ 2). I did not see this observation stated in a source.

### Gaps
- I did not open these to check for complexity remarks: Ellingham & Zha, "Toughness, trees, and walks" (J. Graph Theory 33 (2000)); Gao & Richter's 2-walk papers on circuit/3-connected planar graphs; Kawarabayashi & Ozeki, "Spanning closed walks and TSP in 3-connected planar graphs" (JCTB 2014, [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0095895614000574)). They are known to be existence/structural results. Whether they mention NP-hardness (e.g. of k-walks in planar graphs) is unverified.
- I did not check Ozeki & Yamashita's survey "Spanning trees: a survey" (Graphs Combin., 2011) for remarks on k-walk complexity.
- The exact wording of Garey & Johnson's ND1 entry was not checked against the book; only Wikipedia's paraphrase is cited.
- Publication venue of Kaiser et al. (journal version) is not verified here; only the 2006 LRI report/preprint is cited.

---

## Q4. Results on the threshold where the problem becomes easy (large k relative to n, or relative to degree)

### Takeaway
For at-most-k visits the easy threshold is trivial and well known: every connected graph has a Δ(G)-walk (Jackson–Wormald, via spanning trees). So K ≥ Δ(G), and in particular the repo's K ≥ n−1, is always a YES instance. Liu–Sheffield–Westover (2024) give a tight dichotomy for closed walks in bounded-degree graphs: [1,b]-HAM is NP-hard iff b < d. For exact-k visits, hardness persists to much larger k (Ganian et al.).

### Cited Findings
- "every connected graph G has an α(G)-walk" (stated as following trivially from Theorem 3.1). Theorem 5.3: "Let G be a j-connected graph. Put k = ⌈α(G)/j⌉. Then G has a k-walk." Theorem 3.1(i): every connected K_{1,k+1}-free graph has a k-walk. — [Jackson–Wormald PDF, pp. 138, 143](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)
- "a tree of maximum degree Δ has a Δ-walk [6], and it clearly does not admit any k-walk with k < Δ." In bridgeless graphs the threshold drops to ⌈(Δ+1)/2⌉, which is tight. — [Kaiser et al.](http://home.zcu.cz/~kaisert/papers/deg-walk.pdf)
- Liu, Sheffield, Westover, "Complexity of Multiple-Hamiltonicity in Graphs of Bounded Degree", arXiv:2405.16270 (2024). Theorem 2 (undirected graphs of max degree d): [a,b]-HAM "is NP-hard when either a=1 and b<d or a>1 and b/a<d−1. Otherwise it is in P." Theorem 1 covers d-regular graphs. They note "the graphs produced by known reductions have maximum degree growing linearly in b". — [arXiv:2405.16270](https://arxiv.org/html/2405.16270)
- Exact visits with non-constant multiplicity (closed): "Ganian et al consider the case where a is nonconstant in n, showing that [a,a]-HAM is NP-hard for a ≤ O(n^(1−ε)), but in RP for a ≥ Ω(n/log n)". Citation: R. Ganian, N. S. Narayanaswamy, S. Ordyniak, C. S. Rahul, M. S. Ramanujan, "On the Complexity Landscape of Connected f-Factor Problems", *Algorithmica* 81 (2019) 2606–2632 (MFCS 2016). — [Liu et al.](https://arxiv.org/html/2405.16270); [MFCS 2016 version](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.41)
- Jackson–Wormald Theorem 5.1, a density threshold: "If G is connected, k ≥ 2 and δ(G) > (|V(G)| − 1)/(k + 1) then G has a k-walk." — [PDF, p. 142](https://ajc-new.maths.uq.edu.au/pdf/2/ocr-ajc-v2-p135.pdf)

### Inferences
- The repo's polynomial threshold K ≥ n−1 is correct but weak. The known trivial threshold is K ≥ Δ(G): every spanning tree has max degree ≤ Δ(G), and a DFS tour of a tree visits v at most deg_T(v) times, for open or closed walks. Liu et al.'s Theorem 2 shows this is tight in the bounded-degree setting for closed walks: NP-hard for every constant b < d.
- Liu et al.'s Theorem 2 implies that in max-degree-d graphs the closed version stays NP-hard for every b < d. This sharpens the "graphs of growing degree" reductions of Broersma–Göbel and Jackson–Wormald, whose pendant gadgets raise the degree linearly in k.

### Gaps
- No source found on the open-walk version in bounded-degree graphs, or on a sharp n-relative threshold (e.g. K = f(n)) for the at-most-K version. Since K ≥ Δ is always YES, such a threshold is likely uninteresting except in degree-restricted classes.
