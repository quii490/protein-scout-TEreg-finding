---
type: protein-evaluation
gene: "UFD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## UFD1 — REJECTED (研究热度过高 (PubMed strict=179，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UFD1 / UFD1L |
| 蛋白名称 | Ubiquitin recognition factor in ER-associated degradation protein 1 |
| 蛋白大小 | 307 aa / 34.5 kDa |
| UniProt ID | Q92890 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli; UniProt: Nucleus; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 307 aa / 34.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=179 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=74.6; PDB: 2YUJ, 5B6C, 5C1B, 7WWQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004854, IPR042299, IPR055417, IPR055418; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli | Approved |
| UniProt | Nucleus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- UFD1-NPL4 complex (GO:0036501)
- VCP-NPL4-UFD1 AAA ATPase complex (GO:0034098)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 179 |
| PubMed broad count | 292 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: UFD1L |

**关键文献**:
1. VCP/p97 UFMylation stabilizes BECN1 and facilitates the initiation of autophagy.. *Autophagy*. PMID: 38762759
2. p97/VCP is required for piecemeal autophagy of aggresomes.. *Nature communications*. PMID: 40335532
3. Targeting DTX2/UFD1-mediated FTO degradation to regulate antitumor immunity.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39661064
4. Mechanism of nascent chain removal by the ribosome-associated quality control complex.. *Nature communications*. PMID: 40595698
5. Molecular Basis of VCPIP1 and P97/VCP Interaction Reveals Its Functions in Post-Mitotic Golgi Reassembly.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39234822

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.6 |
| 高置信度残基 (pLDDT>90) 占比 | 37.5% |
| 置信残基 (pLDDT 70-90) 占比 | 20.8% |
| 中等置信 (pLDDT 50-70) 占比 | 26.1% |
| 低置信 (pLDDT<50) 占比 | 15.6% |
| 有序区域 (pLDDT>70) 占比 | 58.3% |
| 可用 PDB 条目 | 2YUJ, 5B6C, 5C1B, 7WWQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2YUJ, 5B6C, 5C1B, 7WWQ）+ AlphaFold高质量预测（pLDDT=74.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004854, IPR042299, IPR055417, IPR055418; Pfam: PF03152, PF24842 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBXN7 | 0.999 | 0.997 | — |
| VCP | 0.999 | 0.999 | — |
| NPLOC4 | 0.999 | 0.999 | — |
| FAF2 | 0.999 | 0.997 | — |
| FAF1 | 0.999 | 0.997 | — |
| NSFL1C | 0.998 | 0.994 | — |
| VCPIP1 | 0.998 | 0.994 | — |
| UBAC2 | 0.995 | 0.994 | — |
| UBXN10 | 0.995 | 0.994 | — |
| DERL1 | 0.995 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| mad2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| EBI-466296 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| NPL4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CDC48 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SELENOS | psi-mi:"MI:0096"(pull down) | pubmed:15215856 |
| Ge-1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| adf | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| HBS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| UBX2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11971|pubmed:16873066 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.6 + PDB: 2YUJ, 5B6C, 5C1B, 7WWQ | pLDDT=74.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol / Nucleoplasm, Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. UFD1 — Ubiquitin recognition factor in ER-associated degradation protein 1，研究基础较多，新颖性有限。
2. 蛋白大小307 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 179 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 179 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92890
- Protein Atlas: https://www.proteinatlas.org/ENSG00000070010-UFD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UFD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92890
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/UFD1/IF_images/UFD1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000070010-UFD1/subcellular

![](https://images.proteinatlas.org/30286/1500_E7_3_red_green.jpg)
![](https://images.proteinatlas.org/30286/1500_E7_4_red_green.jpg)
![](https://images.proteinatlas.org/30286/1503_C6_12_red_green.jpg)
![](https://images.proteinatlas.org/30286/1503_C6_9_red_green.jpg)
![](https://images.proteinatlas.org/30286/1505_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/30286/1505_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92890-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92890 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004854;IPR042299;IPR055417;IPR055418; |
| Pfam | PF03152;PF24842; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000070010-UFD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAF1 | Intact, Biogrid | true |
| NPLOC4 | Intact, Biogrid | true |
| VCP | Intact, Biogrid, Opencell | true |
| AMFR | Biogrid | false |
| CHMP2A | Biogrid | false |
| EZH2 | Biogrid | false |
| FAF2 | Biogrid | false |
| HTT | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
