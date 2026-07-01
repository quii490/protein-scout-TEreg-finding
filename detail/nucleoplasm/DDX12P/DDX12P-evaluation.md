---
type: protein-evaluation
gene: "DDX12P"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## DDX12P 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DDX12P |
| 蛋白名称 | Putative ATP-dependent DNA helicase DDX12 |
| 蛋白大小 | 950 aa / 106.0 kDa |
| UniProt ID | Q92771 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 950 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=76.2; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | ATP-dep_Helicase_C; DinG/Rad3-like; Helic_SF1/SF2_ATP-bd_DinG/Rad3 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **122/180** | |
| **归一化总分** | | | **67.2/100** | 互证: +1 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=1, broad=1
- AF pLDDT: 76.2 / PDB: 0
- InterPro: ATP-dep_Helicase_C; DinG/Rad3-like; Helic_SF1/SF2_ATP-bd_DinG/Rad3
- Pfam: DEAD_2; Helicase_C_2
- PPI degree=5 ChIP: None
32855419: Warsaw Breakage Syndrome associated DDX11 helicase resolves G-quadruplex structu

### 4. 总体评价
★★★★  **67.2/100**  **nucleoplasm**
TE candidate: ATP-dep_Helicase_C; DinG/Rad3-like; Helic_SF1/SF2_ATP-bd_DinG/Rad3


### 补充分析 (UniProt API)

**蛋白全称**: Putative ATP-dependent DNA helicase DDX12

**功能**: DNA helicase involved in cellular proliferation. Probably required for maintaining the chromosome segregation (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR006555 |
| InterPro | IPR045028 |
| InterPro | IPR014013 |
| InterPro | IPR006554 |
| InterPro | IPR027417 |
| InterPro | IPR010614 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LRP1 | BioGRID | 1 |
| CUL3 | BioGRID | 1 |
| RBBP5 | BioGRID | 1 |
| SH2D3C | BioGRID | 0 |
| C9orf72 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q92771-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DDX12P

### 深度机制分析

**结构域架构**：DDX12P（Putative ATP-dependent DNA helicase DDX12, 950 aa / 106.0 kDa）的主要结构域注释为IPR006555（ATP-dependent helicase, C-terminal）、IPR045028（DinG/Rad3-like helicase）、IPR014013（Helicase superfamily 1/2, ATP-binding domain, DinG/Rad3-type）、IPR006554（Helicase-like, DEXD box c2 type）、IPR027417（P-loop containing nucleoside triphosphate hydrolase）。Pfam识别到PF06733（DEAD_2）和PF13307（Helicase_C_2）。该蛋白的pLDDT=76.2（高置信度），结构预测质量良好。无实验PDB结构，但同源蛋白DDX11（Warsaw breakage syndrome-associated）有丰富结构信息。PubMed=1（极低文献量），唯一相关文献为DDX11的G-quadruplex resolution研究——DDX12P作为DDX11 pseudogene/paralog，其功能注释几乎完全依赖sequence similarity inference。

**PPI互作网络解读**：PPI network（degree=5）——BioGRID记录的互作伙伴包括LRP1（LDL receptor related protein 1）、CUL3（Cullin-3, E3 ubiquitin ligase scaffold）、RBBP5（Retinoblastoma binding protein 5, MLL/COMPASS complex member, H3K4 methyltransferase cofactor）、SH2D3C（adaptor protein）和C9orf72（ALS/FTD-associated protein）。RBBP5是MLL/COMPASS H3K4 methyltransferase complex的核心亚基——该互作直接暗示DDX12P可能通过RBBP5参与H3K4me3-dependent transcriptional activation。CUL3互作则连接DDX12P到ubiquitin-proteasome system。这些互作提示DDX12P在chromatin-level transcriptional regulation中的potential moonlighting role。

**结构解读**：DDX12P属于SF2 helicase超家族（DinG/Rad3 subfamily）。该家族特征为3'-5' DNA helicase activity, ATP-dependent DNA unwinding requiring ssDNA loading。IPR006555（ATP-dependent helicase C-terminal domain）provide processivity；IPR014013（ATP-binding domain）包含Walker A/B motifs用于ATP hydrolysis。IPR010614（DEAD_2 domain, 新见于InterPro）提供可能的novel regulatory function。与DDX11的结构保守性提示DDX12P可能同样具有G-quadruplex resolution activity——G-quadruplex structures enriched at TE promoter regions。

**机制模型**：基于structural homology with DDX11 and PPI data：(1) DDX12P作为ATP-dependent DNA helicase识别并unwind specific DNA structures（可能包括G-quadruplex、R-loop）；(2) DNA unwinding activity可能facilitate transcription machinery access to chromatinized loci；(3) 与RBBP5的互作暗示DDX12P可能被recruit到MLL/COMPASS-targeted genomic regions，couple DNA unwinding with H3K4me3 deposition；(4) CUL3 interaction可能介导DDX12P自身的ubiquitination-dependent turnover或其他substrate的泛素化。但这些mechanisms均基于sequence homology和PPI network inference，需要experimental validation。

**TE调控展望**：DDX12P的TE regulation潜力具有interesting inferential basis。TE调控关联性取决于：(1) DDX12P的helicase activity能否resolve TE promoter处富集的G-quadruplex或其他non-B DNA structures——DDX11已知resolve G4 structures at cohesin binding sites；(2) RBBP5 interaction能否将DDX12P-targeted loci mark with H3K4me3，从而促进TE-embedded transcriptional units的激活；(3) DNA helicase activity could facilitate endogenous retroelement replication intermediates processing。建议通过in vitro helicase assay确认DDX12P的DNA substrate preference（尤其是G4 DNA vs dsDNA vs forked DNA），ChIP-seq鉴定其genomic binding sites和在TE loci上的富集，以及knockdown RNA-seq评估对TE subfamily expression的影响。

### PubMed

**Count: 1**

| PMID | Title |
|---|---|
| 32855419 | Warsaw Breakage Syndrome associated DDX11 helicase resolves G-quadruplex structures to support sister chromatid cohesion. |


