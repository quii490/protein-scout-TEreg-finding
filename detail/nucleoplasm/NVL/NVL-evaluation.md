# NVL – Critical False-Rejection Reevaluation Report

**Gene:** NVL
**UniProt Accession:** O15381
**Protein Name:** Nuclear valosin-containing protein-like
**Length:** 856 aa | **Mass:** 95.1 kDa
**Aliases:** NVL2
**Report Date:** 2026-06-04
**Review Stage:** W2 Batch 1 – CRITICAL REOPEN

---

## /180 Scoring Table

| Dimension | Max | Score | Rationale |
|-----------|-----|-------|-----------|
| 1. Nuclear Localization | 30 | 27 | HPA: Nucleoli (Enhanced). UniProt: Nucleus, nucleoplasm, Nucleus, nucleolus, Nucleus, nucleoplasm. GO-CC: 3 IDA nuclear anno. |
| 2. Protein Size | 10 | 3 | 856 aa / 95.1 kDa – very large protein. Significant resource commitment for full characterization. |
| 3. Research Novelty | 10 | 7 | PubMed strict: 34. Moderately low literature. Good novelty. |
| 4. 3D Structure | 30 | 15 | AlphaFold mean pLDDT: 72.5. PDB: 2 experimental structures. |
| 5. Regulatory Domains | 50 | 9 | InterPro: IPR003593, IPR050168, IPR041569. Function summary: Participates in the assembly of the telomerase holoenzyme and effecting of telomerase activity via its interaction with TERT (PubMed:22226966). Involved in both early and late stages of the pre-rRNA p... |
| 6. PPI Network | 50 | 28 | STRING: 15 partners. IntAct: 15 interactors. |
| **TOTAL** | **180** | **89** | |

---

## Nuclear Evidence Section

### HPA (Human Protein Atlas)
- **Status:** hpa_localization_available
- **Reliability (IF):** Enhanced
- **Main Location:** Nucleoli
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。
- **Nuclear-relevant locations:** Nucleoli

### UniProt Subcellular Location
- **Nucleus, nucleoplasm** – Evidence: ECO:0000269
- **Nucleus, nucleolus** – Evidence: ECO:0000269, ECO:0000269, ECO:0000269, ECO:0000269, ECO:0000269
- **Nucleus, nucleoplasm** – Evidence: ECO:0000269

### GO Cellular Component (GO-CC)
- **GO:0016020 (membrane)** – Evidence: HDA:UniProtKB
- **GO:0005730 (nucleolus)** – Evidence: IDA:HPA
- **GO:0005654 (nucleoplasm)** – Evidence: IDA:HPA
- **GO:0005634 (nucleus)** – Evidence: IDA:UniProtKB
- **GO:0005697 (telomerase holoenzyme complex)** – Evidence: IDA:UniProtKB

### Functional Context
- Participates in the assembly of the telomerase holoenzyme and effecting of telomerase activity via its interaction with TERT (PubMed:22226966). Involved in both early and late stages of the pre-rRNA processing pathways (PubMed:26166824). Spatiotemporally regulates 60S ribosomal subunit biogenesis in the nucleolus (PubMed:15469983, PubMed:16782053, PubMed:26456651, PubMed:29107693). Catalyzes the release of specific assembly factors, such as WDR74, from pre-60S ribosomal particles through the ...

**Summary:** NVL has strong nuclear evidence (HPA: Enhanced reliability; UniProt experimental nuclear evidence; GO: 3 IDA nuclear annotations). Nuclear score: 27/30.

**Interpretation note:** HPA IF original images not reliably fetched (HPA search page does not have usable subcellular IF originals). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC.

---

## PubMed Evidence

### Literature Metrics
| Query Type | Count | Query String |
|------------|-------|--------------|
| Strict (Title/Abstract) | 34 | `"NVL"[Title/Abstract] AND (gene[Title/Abstract] OR protein[Title/Abstract] OR hy...` |
| Symbol Only (Title/Abstract) | 162 | |
| Broad (All Fields) | 234 | |

**Alias Note:** Aliases observed but not used for scoring: NVL2

### Key Papers (with PMIDs)
1. **PMID:36634459** – Vulsteke JB, Smith V, Bonroy C (2023 Feb). "Identification of new telomere- and telomerase-associated autoantigens in systemic sclerosis." *Journal of autoimmunity.*
2. **PMID:36609656** – Louche A, Blanco A, Lacerda TLS (2023 Jan 6). "Brucella effectors NyxA and NyxB target SENP3 to modulate the subcellular localisation of nucleolar proteins." *Nature communications.*
3. **PMID:40780730** – Yamashita Y, Yamano Y, Muro Y (2025 Aug 7). "Development of an enzyme-linked immunosorbent assay for the efficient detection of autoantibodies against nuclear valosin-containing protein-like protein (NVL) 2 using its manipulated cDNA." *RMD open.*
4. **PMID:25891250** – Wang M, Chen J, He K (2015 Oct 1). "The NVL gene confers risk for both major depressive disorder and schizophrenia in the Han Chinese population." *Progress in neuro-psychopharmacology & biological psychiatry.*
5. **PMID:34909468** – Yilmaz YZ, Yilmaz BB, Ozdemir YE (2021 Dec). "Effects of hypertonic alkaline nasal irrigation on COVID-19." *Laryngoscope investigative otolaryngology.*

### Literature Assessment
- **Total publications:** Low (34 strict, 234 broad).
- **Novelty score:** 7/10.
- **No publications directly linking this gene to TE regulation.** This represents an unexplored area.

---

## AlphaFold / PDB / PAE

### AlphaFold Predicted Structure
- **Entry:** AF-O15381-F1, version 6
- **Mean pLDDT:** 72.5
- **pLDDT Distribution:**
  - >90 (very high confidence): 19.0%
  - 70-90 (confident): 49.9%
  - 50-70 (low confidence): 9.0%
  - <50 (very low confidence): 22.1%
- **Assessment:** Moderate-confidence structure with some predicted disorder. The protein has both well-folded and flexible regions.

### Experimental PDB Structures
- **2X8A** – X-ray, 2.60 A, chains: A=574-845
- **6RO1** – X-ray, 3.07 A, chains: B=167-216

### Structural Assessment
- PAE image data not locally generated; structure judgment based on AlphaFold pLDDT statistics.
- **Score:** 15/30

---

## PPI Network

### STRING (Functional Partners)
| Partner | Combined Score | Experimental | Textmining | Relevance |
|---------|---------------|-------------|------------|-----------|
| MTREX | 0.983 | 0.900 | 0.623 | |
| TERT | 0.944 | 0.000 | 0.465 | |
| GNL3L | 0.938 | 0.085 | 0.489 | |
| DKC1 | 0.934 | 0.000 | 0.187 | |
| NHP2 | 0.920 | 0.100 | 0.091 | |
| GAR1 | 0.917 | 0.000 | 0.000 | |
| NOP10 | 0.914 | 0.000 | 0.094 | |
| TEP1 | 0.910 | 0.088 | 0.081 | |
| NOM1 | 0.906 | 0.000 | 0.000 | |
| WRAP53 | 0.906 | 0.000 | 0.094 | |
| ... | ... | ... | ... | (15 total partners) |

### IntAct
Total: 15 validated interactors

| Partner | Method | PMID | Interaction Type |
|---------|--------|------|-----------------|
| CRMP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | psi-mi:"MI:0915"(physical association) |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2010.11.017 | psi-mi:"MI:0914"(association) |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 | psi-mi:"MI:0915"(physical association) |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identification) | pubmed:29568061|imex:IM-26301 | psi-mi:"MI:2364"(proximity) |
| RRP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| FGF8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| PLEKHO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | psi-mi:"MI:0914"(association) |
| RNF4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| ... | ... | ... | (15 total) |

### PPI Network Assessment
- **Moderate interaction network.**
- **Score:** 28/50

---

## FALSE REJECTION RECHECK

### Original Rejection Reason (inferred)
NVL was likely auto-rejected due to:
- Large protein size (856 aa)

### Recheck Analysis
1. **HPA Evidence:** Nucleoli – STRONG, reliability: Enhanced.
2. **UniProt Evidence:** Nucleus, nucleoplasm – ECO:0000269 (experimental, ['ECO:0000269']).
2. **UniProt Evidence:** Nucleus, nucleolus – ECO:0000269 (experimental, ['ECO:0000269', 'ECO:0000269', 'ECO:0000269', 'ECO:0000269', 'ECO:0000269']).
2. **UniProt Evidence:** Nucleus, nucleoplasm – ECO:0000269 (experimental, ['ECO:0000269']).
3. **GO-CC Evidence:** 3 IDA-level nuclear annotations present: nucleolus, nucleoplasm, nucleus.
4. **PubMed Count:** 34 strict – within acceptable range.

### Verdict on False Rejection
**The original rejection was FALSE – NVL should NOT have been rejected.** The nuclear evidence is ROBUST (HPA + UniProt experimental + GO IDA). The automated system may have undervalued the nuclear localization, been confused by dual localization patterns, or applied overly conservative scoring.

**This gene SHOULD BE REOPENED for TE-regulatory evaluation.**

---

## TE-Regulator Relevance Reasoning

1. **Translation/Ribosome:** NVL is involved in translation. TE transcripts can be translated, and translational regulation is a layer of TE control. Ribosome-associated proteins may affect TE-derived protein production.
2. **Nucleolar Function:** NVL localizes to the nucleolus. Repetitive rDNA and some TEs are organized in nucleolar-associated domains, making nucleolar proteins relevant to TE spatial organization.

**Caveats:**
- No direct evidence of TE regulation has been established for this gene.
- The connection to TE biology is inferred from nuclear localization and functional domain analysis.

**Assessment:** MODERATE-HIGH interest candidate. Nuclear evidence is robust and literature is limited, offering good novelty. The protein's functional roles in the nucleus provide mechanistic hypotheses for TE regulation.

---

## Final Decision

**DECISION: SCORED – REOPENED for evaluation**

**Score: 89/180**

**Reasoning:** NVL was falsely rejected despite nuclear evidence. The protein has sufficient nuclear localization annotations to merit evaluation. The literature count (34 strict) is within acceptable range. Reopening is justified by the combination of nuclear evidence and functional potential.

**Recommended next steps:**
1. Confirm NVL nuclear localization by immunofluorescence or subcellular fractionation.
2. Screen for NVL binding/regulation at TE loci (ChIP-seq or CUT&RUN targeting TEs).
3. Investigate NVL expression in contexts where TEs are active (development, cancer, stress).
4. Determine whether NVL loss/gain affects TE expression (RNA-seq with TE quantification).

---

## Manual Review Note

*Reviewer: Automated re-evaluation system (2026-06-04)*
*Status: FALSE REJECTION CONFIRMED – gene reopened*

NVL encodes Nuclear valosin-containing protein-like, a 856-amino acid 95.1 kDa protein. 
HPA localizes NVL to Nucleoli (Enhanced reliability). 
UniProt annotates nuclear localization. 
The protein functions primarily in: Participates in the assembly of the telomerase holoenzyme and effecting of telomerase activity via its interaction with TERT (PubMed:22226966). Involved in both early and late stages of the pre-rRNA p. 
The false rejection appears to have resulted from automated scoring that failed to adequately weight the nuclear evidence. 
With only 34 publications, NVL represents a highly novel target. 
The nuclear localization and functional profile make it a strong candidate for TE-regulatory investigation.

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000143748-NVL/subcellular

![](https://images.proteinatlas.org/28219/1176_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/28219/1176_B1_3_red_green.jpg)
![](https://images.proteinatlas.org/28219/1281_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/28219/1281_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/28219/1313_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/28219/1313_D12_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15381 |
| SMART | SM00382; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003593;IPR050168;IPR041569;IPR003959;IPR003960;IPR038100;IPR031996;IPR027417; |
| Pfam | PF00004;PF17862;PF16725; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143748-NVL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADARB1 | Biogrid | false |
| ATP5PD | Opencell | false |
| BRD4 | Biogrid | false |
| IFI16 | Biogrid | false |
| MYC | Biogrid | false |
| NDUFV2 | Opencell | false |
| NPM1 | Biogrid | false |
| PARP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
