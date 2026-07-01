---
type: protein-evaluation
gene: "CCDC106"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC106 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC106 |
| 蛋白名称 | Coiled-coil domain-containing protein 106 |
| 蛋白大小 | 280 aa / 32.0 kDa |
| UniProt ID | Q9BWC9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 280 aa / 32.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031591; Pfam: PF15794 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification and characterization of the novel protein CCDC106 that interacts with p53 and promotes its degradation.. *FEBS letters*. PMID: 20159018
2. HPV-CCDC106 integration alters local chromosome architecture and hijacks an enhancer by three-dimensional genome structure remodeling in cervical cancer.. *Journal of genetics and genomics = Yi chuan xue bao*. PMID: 33023834
3. Molecular mechanism of CCDC106 regulating the p53-Mdm2/MdmX signaling axis.. *Scientific reports*. PMID: 38081879
4. CCDC106 promotes non-small cell lung cancer cell proliferation.. *Oncotarget*. PMID: 28460455
5. Bioinformatics and machine learning approaches reveal key genes and underlying molecular mechanisms of atherosclerosis: A review.. *Medicine*. PMID: 39093811

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.8 |
| 高置信度残基 (pLDDT>90) 占比 | 39.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 21.8% |
| 低置信 (pLDDT<50) 占比 | 22.1% |
| 有序区域 (pLDDT>70) 占比 | 56.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.8，有序区 56.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031591; Pfam: PF15794 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TP53 | 0.751 | 0.517 | — |
| CCDC154 | 0.622 | 0.000 | — |
| CCDC34 | 0.605 | 0.000 | — |
| ATF4 | 0.605 | 0.605 | — |
| RSPRY1 | 0.594 | 0.000 | — |
| FIZ1 | 0.554 | 0.000 | — |
| NUDT13 | 0.539 | 0.000 | — |
| ZC3H15 | 0.539 | 0.000 | — |
| AKAP13 | 0.536 | 0.000 | — |
| SNX15 | 0.535 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.8 + PDB: 无 | pLDDT=72.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CCDC106 — Coiled-coil domain-containing protein 106，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小280 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TP53 | STRING | 751 |
| ATF4 | BioGRID | 1 |
| COPS6 | BioGRID | 1 |
| KAT5 | BioGRID | 1 |
| LRIF1 | BioGRID | 1 |
| UTP14A | BioGRID | 1 |
| SETDB1 | BioGRID | 1 |
| RBM48 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

CCDC106（Coiled-coil domain-containing protein 106, 280 aa, UniProt Q9BWC9）。定位于nucleoplasm，包含一个Pfam PF15794/InterPro IPR031591 coiled-coil结构域。AlphaFold v6预测结构pLDDT=72.8（有序区56.1%），无实验PDB结构。coiled-coil结构域通常介导蛋白-蛋白互作及同源/异源寡聚化，提示CCDC106可能通过卷曲螺旋界面参与多蛋白复合体组装。

从PPI网络角度，STRING预测15个互作伙伴，其中最关键的是TP53（combined score=0.751, experimental=0.517），已有文献报道CCDC106与p53直接互作并促进p53降解（PMID:20159018, PMID:38081879）。BioGRID额外鉴定ATF4、COPS6、KAT5、SETDB1等伙伴。CCDC106-p53-Mdm2/MdmX轴是核心机制：CCDC106作为p53负调控因子，通过促进p53泛素化降解维持p53稳态（PMID:38081879）。在宫颈癌中，HPV整合至CCDC106位点改变局部染色质三维结构并劫持增强子活性（PMID:33023834），提示其在基因组结构调控中的非经典角色。

从TE调控角度，CCDC106与SETDB1（H3K9me3甲基转移酶，经典TE沉默因子）的BioGRID互作极具启示性。SETDB1催化转座子区域的H3K9me3修饰以维持TE转录沉默。若CCDC106通过coiled-coil结构域与SETDB1形成复合体，可能间接参与TE表观遗传沉默的调控——这一假说尚无文献报道，值得实验验证。

从研究新颖性角度，PubMed仅8篇严格文献，p53-CCDC106相互作用机制刚被阐明（PMID:38081879, 2023），其基因组调控功能完全未被探索。结构质量中等（pLDDT=72.8），综合评分73.9/100，推荐开展CCDC106-SETDB1互作的Co-IP验证及ChIP-seq分析，探索其在TE区域的作用。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BWC9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173581-CCDC106/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC106
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWC9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000173581-CCDC106/subcellular

![](https://images.proteinatlas.org/43219/1035_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/43219/1035_G12_3_red_green.jpg)
![](https://images.proteinatlas.org/43219/847_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/43219/847_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/43219/857_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/43219/857_F11_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BWC9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BWC9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031591; |
| Pfam | PF15794; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173581-CCDC106/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF4 | Intact, Biogrid | true |
| TP53 | Intact, Biogrid | true |
| CACNA1S | Intact | false |
| CEP19 | Intact | false |
| CSNK2B | Biogrid | false |
| EIF1AD | Intact | false |
| FAM9B | Intact | false |
| GID4 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
