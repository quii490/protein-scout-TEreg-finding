---
type: protein-evaluation
gene: "RPGRIP1"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: rejected
---

## RPGRIP1 -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RPGRIP1 / X-linked retinitis pigmentosa GTPase regulator-interacting protein 1 |
| Protein Name | X-linked retinitis pigmentosa GTPase regulator-interacting protein 1 |
| Protein Size | 1286 aa / 146.7 kDa |
| UniProt ID | Q96KN7 (RPGR1_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation to confirm rejection status |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 1/10 | x4 | **4** | UniProt: Cell projection, cilium only; GO-CC: cilium/axoneme/ciliary tip; no nuclear annotation; exclusively ciliary |
| Protein Size | 5/10 | x1 | **5** | 1286 aa, in the 1200-2000 aa range |
| Research Novelty | REJECTED | x5 | **REJECTED** | PubMed ~176 articles (>100 -> automatic REJECTED) |
| 3D Structure | 7/10 | x3 | **21** | PDB: 4QAM; experimental crystallography; informational only (protein already rejected) |
| Regulatory Domains | 2/10 | x2 | **4** | C2 domain (membrane/lipid binding); coiled-coil; no DNA/chromatin domains; ciliary function |
| PPI Network | 4/10 | x3 | **12** | RPGR, NPHP4; ciliary transport and photoreceptor maintenance; no nuclear PPI |
| Cross-Validation Bonus | -- | -- | **+0** | Informational only (protein rejected on two independent grounds) |
| **Raw Total** | | | **N/A** | Protein rejected -- scores are informational only |
| **Normalized Total** | | | **N/A** | Protein rejected -- scores are informational only |

### 3. Nuclear Localization Evidence -- FAILS THRESHOLD

| Source | Localization | Reliability |
|--------|-------------|-------------|
| UniProt (Swiss-Prot) | Cell projection, cilium | Reviewed -- exclusive annotation |
| GO-CC | Axoneme | Curated |
| GO-CC | Ciliary tip | Curated |
| GO-CC | Cilium | Curated |
| GO-CC | Cytosol | Curated |
| GO-CC | Microtubule cytoskeleton | Curated |
| GO-CC | Photoreceptor connecting cilium | Curated |
| GO-CC | Photoreceptor distal connecting cilium | Curated |

**HPA IF Status**: HPA IF original images not reliably obtained. Localization assessment based on UniProt and GO-CC -- no nuclear evidence.

**Manual Review Assessment**: RPGRIP1 is an exclusively ciliary protein. Every annotated subcellular location points to the cilium or ciliary substructures (axoneme, ciliary tip, photoreceptor connecting cilium, photoreceptor distal connecting cilium). The cytosol annotation represents the soluble pool before ciliary targeting. There is NO nuclear annotation in any database. The protein functions in ciliary transport and photoreceptor maintenance -- processes that occur at the primary cilium of photoreceptor cells, not in the nucleus.

**Reasons for rejection on nuclear grounds**:
1. UniProt subcellular location: exclusively "Cell projection, cilium" -- no nucleus
2. GO-CC annotations: all ciliary (axoneme, ciliary tip, cilium, photoreceptor connecting cilium, photoreceptor distal connecting cilium)
3. No nuclear, nucleoplasm, chromatin, or PML body annotation in any database
4. UniProt keywords: "Ciliopathy, Cilium, Cone-rod dystrophy, Glaucoma, Leber congenital amaurosis" -- all disease associations are with retinal/ciliary disorders
5. Protein function: ciliary transport adaptor, photoreceptor maintenance -- no nuclear function
6. Interacting partners (RPGR, NPHP4) are ciliary proteins -- no nuclear PPI

**Nuclear localization score: 1/10. RULE: Nuclear <=3 -> REJECTED.** RPGRIP1 is definitively non-nuclear. It is a ciliary protein with no nuclear annotation or function. This is not a borderline case.

### 4. PubMed Count -- FAILS THRESHOLD (independent rejection ground)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~176 |
| Rejection threshold | >100 |
| Earliest publication | ~1999 |

**PubMed Assessment**: With approximately 176 PubMed articles, RPGRIP1 far exceeds the >100 threshold for automatic rejection. The extensive literature reflects its established role in retinal degenerative diseases, particularly Leber congenital amaurosis and retinitis pigmentosa. The protein has been heavily studied in the context of ciliopathies and photoreceptor biology.

**RULE: PubMed >100 -> REJECTED.** This is an independent rejection ground. Even if RPGRIP1 were nuclear (which it is not), the PubMed count alone would disqualify it.

### 5. Research Context (Informational)

RPGRIP1 is a well-established ciliary protein that functions as an adaptor linking the ciliary transition zone protein RPGR (retinitis pigmentosa GTPase regulator) to other ciliary and centrosomal proteins. Mutations in RPGRIP1 cause Leber congenital amaurosis type 6, a severe early-onset retinal dystrophy, as well as cone-rod dystrophy and primary open-angle glaucoma.

**Major research themes (all ciliary/retinal)**:
- Ciliary protein trafficking and transport
- Photoreceptor connecting cilium structure and function
- Retinal degenerative disease mechanisms
- Ciliopathy genetics and pathophysiology
- Ciliary transition zone organization

**Note**: RPGRIP1 is an important protein in ciliary biology and retinal disease, but it has no relevance to nuclear protein research. The rejection is based on the scope of the nuclear protein screen, not on the protein's biological importance.

### 6. 3D Structure Analysis (Informational)

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 (4QAM) |
| Structural Coverage | Partial (C2 domain) |

**Structure Assessment**: RPGRIP1 has one experimental PDB structure (4QAM), covering the C2 domain. The C2 domain is a membrane/lipid-binding domain consistent with ciliary membrane association. Score 7/10 is informational only.

### 7. Domain Architecture (Informational)

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR021656 (RPGRIP1 domain) | Family-specific domain |
| InterPro | IPR000008 (C2 domain) | Membrane/lipid binding -- ciliary function |
| InterPro | IPR041091 (RPGRIP1_C) | C-terminal conserved region |
| Pfam | PF00168 (C2) | C2 domain |
| Pfam | PF11618 (RPGRIP1) | RPGRIP1-specific domain |

**Domain Analysis**: The C2 domain and coiled-coil regions are consistent with ciliary scaffold/adaptor function. No DNA-binding, chromatin-interacting, or nuclear regulatory domains are present. Score 2/10 (informational only).

### 8. PPI Network Analysis (Informational)

| Partner | Context | Functional Relevance |
|---------|---------|---------------------|
| RPGR | Retinitis pigmentosa GTPase regulator | Ciliary transition zone partner |
| NPHP4 | Nephrocystin-4 | Ciliary transport |

**PPI Assessment**: All characterized interactions are with ciliary proteins, reinforcing the exclusively non-nuclear nature of RPGRIP1. Score 4/10 (informational only).

### 9. Cross-Validation Analysis (Informational)

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Ciliary Localization | UniProt + GO-CC + Keywords | Exclusively ciliary | Highly consistent |
| Disease Association | Keywords + Literature | Retinal ciliopathies | Consistent with ciliary function |
| Domain | C2 domain + coiled-coil | Ciliary scaffold/adaptor | Consistent with ciliary function |

### 10. Overall Assessment

**Recommendation Level**: NOT RECOMMENDED -- REJECTED on two independent grounds

**Core Reasons for Rejection**:
1. PubMed count (176) exceeds the >100 hard threshold -- automatic REJECTION
2. Nuclear localization score (1/10) is well below the <=3 threshold -- automatic REJECTION
3. The protein is exclusively ciliary with no nuclear annotation or function
4. All disease associations are with retinal ciliopathies
5. All interacting partners are ciliary proteins
6. Domain architecture (C2 domain) is incompatible with nuclear/chromatin function

**Note on biological importance**: RPGRIP1 is a critically important protein in retinal biology and ciliopathy genetics. This rejection reflects the scope of the nuclear protein screen, not a negative assessment of the protein's scientific value. RPGRIP1 is an excellent target for ciliary biology and retinal disease research.

### 11. Decision

**FINAL DECISION**: REJECTED (previous rejection UPHELD with stronger evidence). RPGRIP1 is a definitive ciliary protein with extensive literature (PubMed=176). The protein fails both independent rejection criteria: PubMed >100 AND nuclear localization <=3. This is not a borderline case -- RPGRIP1 has no nuclear annotation whatsoever and is extensively characterized as a ciliary protein involved in retinal degenerative diseases. The protein has clear biological importance in ciliopathy research but is inappropriate for a nuclear protein screen.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q96KN7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RPGRIP1%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references
- PDB: https://www.rcsb.org/ (4QAM)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KN7
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q96KN7/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries
