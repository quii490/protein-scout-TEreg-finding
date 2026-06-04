---
type: protein-evaluation
gene: "PRC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PRC1 — REJECTED (研究热度过高 (PubMed strict=1223，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRC1 |
| 蛋白名称 | Protein regulator of cytokinesis 1 |
| 蛋白大小 | 620 aa / 71.6 kDa |
| UniProt ID | O43663 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Microtubules, Cytokinetic bridge, Midbody; 额外: Nucleoplasm, ; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spindle pole; M |
| 蛋白大小 | 10/10 | ×1 | 10 | 620 aa / 71.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1223 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.9; PDB: 3NRX, 3NRY, 4L3I, 4L6Y, 5KMG, 7VBG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007145; Pfam: PF03999 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules, Cytokinetic bridge, Midbody; 额外: Nucleoplasm, Plasma membrane | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spindle pole; Midbody; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- contractile ring (GO:0070938)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- intercellular bridge (GO:0045171)
- microtubule cytoskeleton (GO:0015630)
- midbody (GO:0030496)
- mitotic spindle midzone (GO:1990023)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1223 |
| PubMed broad count | 1823 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The molecular principles of gene regulation by Polycomb repressive complexes.. *Nature reviews. Molecular cell biology*. PMID: 34400841
2. The Polycomb complex PRC2 and its mark in life.. *Nature*. PMID: 21248841
3. Epigenetic regulation of noncanonical menin targets modulates menin inhibitor response in acute myeloid leukemia.. *Blood*. PMID: 39158067
4. Goldilocks meets Polycomb.. *Genes & development*. PMID: 36460465
5. The Polycomb Repressor Complex 1 Drives Double-Negative Prostate Cancer Metastasis by Coordinating Stemness and Immune Suppression.. *Cancer cell*. PMID: 31327655

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 59.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 22.9% |
| 有序区域 (pLDDT>70) 占比 | 73.7% |
| 可用 PDB 条目 | 3NRX, 3NRY, 4L3I, 4L6Y, 5KMG, 7VBG |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3NRX, 3NRY, 4L3I, 4L6Y, 5KMG, 7VBG）+ AlphaFold极高置信度预测（pLDDT=78.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007145; Pfam: PF03999 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TPX2 | 0.999 | 0.292 | — |
| KIF4A | 0.995 | 0.642 | — |
| KIF23 | 0.992 | 0.536 | — |
| CENPE | 0.990 | 0.633 | — |
| KIF14 | 0.986 | 0.317 | — |
| RACGAP1 | 0.973 | 0.331 | — |
| KIF11 | 0.972 | 0.409 | — |
| PLK1 | 0.955 | 0.510 | — |
| CDC20 | 0.947 | 0.000 | — |
| KIF2C | 0.944 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000377793.3 | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-14964|pubmed:20691902 |
| Pla2g4a | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRT20 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TFS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| BLM10 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| ZDS2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| APS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PRE6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 3NRX, 3NRY, 4L3I, 4L6Y, 5KMG,  | pLDDT=78.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spind / Microtubules, Cytokinetic bridge, Midbody; 额外: Nuc | 一致 |
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
1. PRC1 — Protein regulator of cytokinesis 1，研究基础较多，新颖性有限。
2. 蛋白大小620 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1223 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1223 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43663
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198901-PRC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43663
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
