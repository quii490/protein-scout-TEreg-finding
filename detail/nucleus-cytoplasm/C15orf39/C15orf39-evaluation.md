---
type: protein-evaluation
gene: "C15orf39"
date: 2026-06-01
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## C15orf39 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | C15orf39 |
| 蛋白全名 | Uncharacterized protein C15orf39 |
| 蛋白大小 | 1047 aa / ~115 kDa |
| UniProt ID | Q6ZRI6 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | UniProt Cytoplasm + Nucleus (ECO:0000269); GO nucleus IDA:UniProtKB + cytoplasm IDA |
| 蛋白大小 | 4/10 | ×1 | 4.0 | 1047 aa, large protein |
| 研究新颖性 | 10/10 | ×5 | 50.0 | Strict=5 |
| 三维结构 | 3/10 | ×3 | 9.0 | AlphaFold pLDDT 48.4 — very low, highly disordered |

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/C15orf39/C15orf39-PAE.png]]
![[C15orf39-PAE.png]]
| 调控结构域 | 3/10 | ×2 | 6.0 | Uncharacterized; no defined functional domains |
| PPI 网络 | 4/10 | ×3 | 12.0 | STRING 502 error; IntAct 15 records; UniProt 0 curated |
| **加权总分** | | | **109/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **59.6/100**** | |

PubMed strict: 5

### 3. 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm (ECO:0000269); Nucleus (ECO:0000269) | Experimental |
| GO-CC | cytoplasm IDA:UniProtKB; cytosol IDA:HPA; nucleus IDA:UniProtKB | Direct assay |
| HPA (IF) | HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/C15orf39/IF_images/C15orf39_IF_461_C8_1_blue_red_green.jpg]]。核定位基于HPA localization/reliability + UniProt + GO-CC。


**HPA IF 状态**: HPA IF 图像已本地嵌入。



![[C15orf39-PAE.png]]

### 4. PPI 网络

| Partner | Source | Evidence | Relevance |
|---|---|---|---|
| RPLP1 | IntAct | two hybrid (PMID:16169070) | Ribosomal protein |
| CTBP2 | IntAct | two hybrid (PMID:21988832) | Transcriptional corepressor (nuclear) |
| SRPK1 | IntAct | kinase assay (PMID:23602568) | Splicing kinase (nuclear) |
| CCNJL | IntAct | coIP (PMID:28514442) | Cyclin J-like |
| MARF1 | IntAct | socio-affinity (PMID:unassigned1312) | Meiosis regulator |

**STRING**: HTTP 502 — 数据不可用。**IntAct**: 15 条记录，含 CTBP2（核转录辅抑制因子）和 SRPK1（核 splicing 激酶）等核蛋白互作。**UniProt curated interactions**: 0。无 BioGrid 补充数据。

### 5. 研究现状
关键文献: C15orf39 通过 PI3K/AKT 信号促进胃癌发生 (PMID:40032127)、通过 PRMT2 抑制炎症反应 (PMID:38892217)。功能方向偏向癌症和炎症信号。PRMT2 为核蛋白精氨酸甲基转移酶，提示可能的核功能关联。

### 6. 总体评价
C15orf39 是大型未表征蛋白，具有实验级核-胞质双定位证据 (ECO:0000269/IDA)。主要弱项为极低结构置信度 (pLDDT 48.4) 和蛋白质巨大 (1047 aa)。PPI 含 CTBP2 和 SRPK1 等核蛋白互作。研究极度新颖 (strict=5)。低置信度 nucleus-cytoplasm 候选，建议优先获取结构/定位实验数据。

### 7. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZRI6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZRI6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C15orf39

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/C15orf39/C15orf39-PAE.png]]



![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/C15orf39/C15orf39-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZRI6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037656; |
| Pfam | PF17663; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167173-C15orf39/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAPZB | Opencell | false |
| CTBP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
