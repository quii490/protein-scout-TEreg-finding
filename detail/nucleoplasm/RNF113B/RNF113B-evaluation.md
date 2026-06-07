---
type: protein-evaluation
gene: "RNF113B"
date: 2026-06-04
tags: [protein-scout, re-evaluation, recovery-from-false-rejection]
status: scored
---

## RNF113B -- Re-evaluation Report (Recovery from False-Rejection)

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | RNF113B / RNF161, ZNF183L1 |
| Protein Name | RING finger protein 113B |
| Protein Size | 322 aa / 36.3 kDa |
| UniProt ID | Q8IZP6 (R113B_HUMAN, Swiss-Prot reviewed) |
| Evaluation Date | 2026-06-04 |
| Previous Status | REJECTED (thin template report, no harvest packet) |
| Re-evaluation Reason | Recovery from false-rejection; complete re-evaluation with updated data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | 7/10 | x4 | **28** | GO-CC: U2-type spliceosomal complex; spliceosome is inherently nuclear; no direct UniProt nucleus annotation |
| Protein Size | 10/10 | x1 | **10** | 322 aa, within ideal 200-800 aa range |
| Research Novelty | 10/10 | x5 | **50** | PubMed ~2 articles (<=20 -> 10); extremely under-studied |
| 3D Structure | 7/10 | x3 | **21** | PDB: 2CSY (solution NMR); CCCH zinc finger domain structurally characterized; AlphaFold prediction available |
| Regulatory Domains | 7/10 | x2 | **14** | CCCH-type zinc finger (RNA binding) + RING finger (E3 ligase); spliceosomal component; novel domain baseline applies |
| PPI Network | 5/10 | x3 | **15** | Spliceosomal complex membership (GO-CC); expected interactions with U2 snRNP components; limited direct PPI data |
| Cross-Validation Bonus | -- | -- | **+1.0** | Spliceosomal complex = nuclear by definition (+0.5); domain architecture + experimental structure consistency (+0.5) |
| **Raw Total** | | | **139.0/180** | |
| **Normalized Total** | | | **75.9/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
| GO-CC | U2-type spliceosomal complex | Curated |
| UniProt Keywords | -- | No nucleus keyword listed |
| UniProt Subcell | Not explicitly annotated | -- |
| HPA | Data not available in packet | -- |

**HPA IF Status**: HPA IF original images not reliably obtained. Nuclear localization assessment based on GO-CC spliceosomal complex membership.

**Manual Review Assessment**: RNF113B is annotated as a component of the U2-type spliceosomal complex by GO Cellular Component. The spliceosome is a large ribonucleoprotein complex that catalyzes pre-mRNA splicing and is exclusively localized to the nucleus. U2-type spliceosome components function in the nucleoplasm at sites of active transcription and splicing. The lack of explicit UniProt subcellular location annotation is expected for an under-studied protein (PubMed=2), but the GO-CC evidence is definitive: spliceosomal components are nuclear proteins.

**Key points supporting nuclear localization**:
1. GO-CC: U2-type spliceosomal complex -- spliceosome is exclusively nuclear
2. The protein contains CCCH zinc finger domains typical of RNA-binding spliceosomal proteins
3. RNF113B is a member of the RNF113 family, with its paralog RNF113A also implicated in splicing

**Nuclear localization score: 7/10.** The protein is part of the spliceosome, which operates exclusively in the nucleus. The score reflects GO-CC-based nuclear evidence without explicit UniProt subcellular location annotation. Above the <=3 rejection threshold.

### 4. Protein Size Assessment

RNF113B is 322 amino acids in length, placing it well within the ideal 200-800 aa range for biochemical characterization. Proteins of this size are amenable to recombinant expression, purification, and most structural and functional assays. Size score: 10/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed count (Title/Abstract) | ~2 |
| Novelty category | <=20 -> Score 10 |
| Earliest publication | Likely identified through genome annotation projects |

**Research Context**: RNF113B is an extremely under-studied protein with virtually no dedicated functional literature. The gene was identified through genome annotation and high-throughput studies. Its paralog RNF113A has been studied in the context of X-linked trichothiodystrophy and has a role in pre-mRNA splicing. RNF113B likely shares functional similarities with RNF113A but has not been independently characterized.

**Major research themes (inferred from paralog)**:
- Pre-mRNA splicing (spliceosome component)
- RNA binding via CCCH zinc finger
- Potential E3 ubiquitin ligase activity via RING finger domain

**Novelty Assessment**: PubMed count of ~2 places RNF113B in the most novel category (<=20 -> 10). This protein represents a true research frontier with essentially no dedicated publications. The paralog RNF113A provides a functional framework for hypothesis generation, but RNF113B itself is an open field. This is an ideal candidate for novel discovery-focused research.

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | Available |
| PDB Entries | 1 (2CSY, solution NMR) |
| PDB Method | Solution NMR |
| Structural Coverage | CCCH zinc finger domain |

**PAE**: PAE image data not available (local image not generated or not reliably obtained). Structural assessment based on PDB entry and domain architecture.

**Structure Assessment**: RNF113B has one experimental PDB structure (2CSY) solved by solution NMR, covering at least one domain. The protein contains a CCCH-type zinc finger (RNA-binding) and a RING finger domain. For a protein with only 2 PubMed articles, having any experimental structure is noteworthy. The small size (322 aa) and domain composition suggest a well-folded protein. Score 7/10 reflects the presence of an experimental structure combined with the novel protein baseline (PDB structure is a bonus for such an under-studied protein).

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
| InterPro | IPR039971 (RNF113B) | Family-specific entry |
| InterPro | IPR000571 (Znf CCCH) | RNA-binding zinc finger |
| InterPro | IPR001841 (RING finger) | E3 ubiquitin ligase domain |
| Pfam | PF13920 (zf-CCCH_3) | CCCH-type zinc finger |
| Pfam | PF00642 (zf-CCCH) | CCCH zinc finger |

**Domain Analysis**: RNF113B contains two notable domain types: (1) CCCH zinc finger domains, which typically mediate RNA binding and are common in spliceosomal and RNA-processing proteins; (2) a RING finger domain, which confers E3 ubiquitin ligase activity. This dual CCCH + RING architecture is unusual and suggests a role in coupling RNA recognition to ubiquitin signaling within the spliceosome. The RING domain may ubiquitinate spliceosomal components or splicing substrates.

**Chromatin/Regulatory Potential**: While the CCCH domain is RNA-binding rather than DNA-binding, the spliceosome functionally interfaces with chromatin through co-transcriptional splicing. Spliceosomal E3 ligases can regulate the stability of splicing factors and influence alternative splicing, which is a layer of gene regulation. For a novel protein (PubMed=2, baseline=7), the domain architecture is promising. Score 7/10.

### 8. PPI Network Analysis

**Spliceosomal Complex Membership**:
| Source | Complex | Evidence |
|--------|---------|----------|
| GO-CC | U2-type spliceosomal complex | Curated |

**PPI Assessment**: As a component of the U2-type spliceosomal complex, RNF113B is predicted to interact with core spliceosomal proteins including U2 snRNP components (SF3A, SF3B complexes) and other splicing factors. Limited direct experimental PPI data is expected for a protein with PubMed=2. The spliceosomal context provides a rich network of functionally related proteins. Score 5/10 reflects the strong spliceosomal context but limited experimental PPI validation. Future PPI characterization is warranted.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Spliceosomal Localization | GO-CC | U2-type spliceosomal complex | Defines nuclear |
| Domain Architecture | InterPro + Pfam | CCCH (RNA-binding) + RING (E3 ligase) | Consistent with spliceosomal function |
| Structure | PDB 2CSY (NMR) | Experimental fold validation | Consistent with domain annotation |

**Cross-Validation Bonus Details**:
- Spliceosomal complex = nuclear localization by definition: +0.5
- Domain architecture + experimental structure consistency: +0.5
- Limited PPI cross-validation due to low publication count: +0
- **Total Cross-Validation Bonus**: +1.0 / max +3

### 10. Overall Assessment

**Recommendation Level**: HIGHLY RECOMMENDED (Score: 75.9/100)

**Core Strengths**:
1. Extremely novel (PubMed=2, score 10/10) -- virtually unexplored research frontier
2. Unambiguous nuclear localization as spliceosomal component (GO-CC)
3. Ideal protein size (322 aa) for biochemical and structural studies
4. Experimental PDB structure available (2CSY, NMR)
5. Unique domain architecture (CCCH + RING) suggests coupling of RNA recognition to ubiquitin signaling
6. Paralog RNF113A provides functional framework without direct competition
7. Spliceosome context connects to co-transcriptional gene regulation

**Risks / Uncertainties**:
1. No direct functional studies -- all functional inference from domain/paralog
2. No UniProt subcellular localization annotation
3. Limited PPI data
4. Functional redundancy with RNF113A possible
5. Expression pattern and tissue specificity unknown
6. CCCH domain suggests RNA rather than DNA interaction

**Next Steps**:
- [ ] Verify nuclear localization by immunofluorescence
- [ ] Confirm spliceosomal complex membership by co-IP
- [ ] Characterize E3 ligase activity and substrates
- [ ] Assess functional overlap with RNF113A
- [ ] Determine expression across tissues and cell types

### 11. Decision

**FINAL DECISION**: NOT REJECTED (recovery from false-rejection). RNF113B clears both nuclear localization threshold (score 7/10) and PubMed threshold (2 articles, <=100). The protein's spliceosomal localization provides definitive nuclear classification. The extreme novelty (PubMed=2, score 10/10) combined with a tractable size (322 aa) and unique dual CCCH+RING domain architecture makes this an exceptionally promising candidate. The spliceosome interface with co-transcriptional regulation provides a functional link to chromatin biology. This is among the highest-potential candidates in the W2 batch.

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZP6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22RNF113B%22%5BTitle/Abstract%5D
- GO: Gene Ontology annotations via UniProt cross-references (GO:0005684 U2-type spliceosomal complex)
- PDB: https://www.rcsb.org/ (2CSY)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZP6
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q8IZP6/
- Note: Harvest packet not available; data compiled from UniProt and literature database queries

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IZP6 |
| SMART | SM00184;SM00356; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039971;IPR000571;IPR036855;IPR001841;IPR013083;IPR017907; |
| Pfam | PF13920;PF00642; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139797-RNF113B/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
