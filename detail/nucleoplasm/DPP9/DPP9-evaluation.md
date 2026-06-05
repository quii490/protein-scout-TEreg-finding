---
type: protein-evaluation
gene: "DPP9"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DPP9 — REJECTED (研究热度过高 (PubMed strict=136，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPP9 / DPRP2 |
| 蛋白名称 | Dipeptidyl peptidase 9 |
| 蛋白大小 | 863 aa / 98.3 kDa |
| UniProt ID | Q86TI2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DPP9/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DPP9/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, cytosol; Nucleus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 863 aa / 98.3 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=136 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.5; PDB: 6EOQ, 6EOR, 6QZV, 6X6A, 6X6C, 7A3F, 7JKQ |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029058, IPR045785, IPR001375, IPR002469, IPR050 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cell leading edge (GO:0031252)
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 136 |
| PubMed broad count | 298 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DPRP2 |

**关键文献**:
1. DPP9 Stabilizes NRF2 to Suppress Ferroptosis and Induce Sorafenib Resistance in Clear Cell Renal Cell Carcinoma.. *Cancer research*. PMID: 37713596
2. The NLRP1 and CARD8 inflammasomes.. *Immunological reviews*. PMID: 32558991
3. DPP9 regulates NQO1 and ROS to promote resistance to chemotherapy in liver cancer cells.. *Redox biology*. PMID: 39094401
4. The amino-dipeptidyl peptidases DPP8 and DPP9: Purification and enzymatic assays.. *Methods in enzymology*. PMID: 37230592
5. Genetic mechanisms of critical illness in COVID-19.. *Nature*. PMID: 33307546

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.5 |
| 高置信度残基 (pLDDT>90) 占比 | 81.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 96.0% |
| 可用 PDB 条目 | 6EOQ, 6EOR, 6QZV, 6X6A, 6X6C, 7A3F, 7JKQ, 7JN7, 7SVL, 7SVN |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6EOQ, 6EOR, 6QZV, 6X6A, 6X6C, 7A3F, 7JKQ, 7JN7, 7SVL, 7SVN）+ AlphaFold极高置信度预测（pLDDT=92.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR045785, IPR001375, IPR002469, IPR050278; Pfam: PF19520, PF00930, PF00326 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CARD8 | 0.972 | 0.900 | — |
| NLRP1 | 0.951 | 0.909 | — |
| PREP | 0.946 | 0.000 | — |
| DPP7 | 0.881 | 0.000 | — |
| TFDP3 | 0.786 | 0.000 | — |
| HRK | 0.660 | 0.000 | — |
| CC2D1B | 0.630 | 0.000 | — |
| LZTFL1 | 0.606 | 0.000 | — |
| IFNAR2 | 0.585 | 0.000 | — |
| ATP11A | 0.574 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=92.5 + PDB: 6EOQ, 6EOR, 6QZV, 6X6A, 6X6C,  | pLDDT=92.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DPP9 — Dipeptidyl peptidase 9，有一定研究基础，但仍存在niche空间。
2. 蛋白大小863 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 136 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 136 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86TI2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142002-DPP9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPP9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86TI2
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:19:23

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86TI2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
