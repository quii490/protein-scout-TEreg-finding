---
type: protein-evaluation
gene: "DUT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DUT — REJECTED (研究热度过高 (PubMed strict=130，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUT |
| 蛋白名称 | Deoxyuridine 5'-triphosphate nucleotidohydrolase, mitochondrial |
| 蛋白大小 | 252 aa / 26.6 kDa |
| UniProt ID | P33316 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Mitochondrion |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 252 aa / 26.6 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=130 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.3; PDB: 1Q5H, 1Q5U, 2HQU, 3ARA, 3ARN, 3EHW, 4MZ5 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008181, IPR029054, IPR036157, IPR033704; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 130 |
| PubMed broad count | 1377 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Malic enzyme 2 connects the Krebs cycle intermediate fumarate to mitochondrial biogenesis.. *Cell metabolism*. PMID: 33770508
2. Life without dUTPase.. *Frontiers in microbiology*. PMID: 27933035
3. Polyglutamine Repeats in Viruses.. *Molecular neurobiology*. PMID: 30182336
4. DUT (p.Y116C)-Mutation-Induced Thrombocytopenia in Rabbits.. *International journal of molecular sciences*. PMID: 40362420
5. Evolution of the DUT gene: horizontal transfer between host and pathogen in all three domains of life.. *Current protein & peptide science*. PMID: 12369928

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.3 |
| 高置信度残基 (pLDDT>90) 占比 | 50.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.6% |
| 中等置信 (pLDDT 50-70) 占比 | 17.9% |
| 低置信 (pLDDT<50) 占比 | 26.2% |
| 有序区域 (pLDDT>70) 占比 | 56.0% |
| 可用 PDB 条目 | 1Q5H, 1Q5U, 2HQU, 3ARA, 3ARN, 3EHW, 4MZ5, 4MZ6, 5H4J, 7PWJ |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1Q5H, 1Q5U, 2HQU, 3ARA, 3ARN, 3EHW, 4MZ5, 4MZ6, 5H4J, 7PWJ）+ AlphaFold预测（pLDDT=74.3），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008181, IPR029054, IPR036157, IPR033704; Pfam: PF00692 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TYMS | 0.994 | 0.225 | — |
| DTYMK | 0.981 | 0.000 | — |
| DCTD | 0.977 | 0.073 | — |
| ITPA | 0.959 | 0.132 | — |
| TK2 | 0.955 | 0.000 | — |
| NME6 | 0.948 | 0.000 | — |
| NME1 | 0.945 | 0.000 | — |
| NT5C | 0.942 | 0.000 | — |
| AK9 | 0.938 | 0.089 | — |
| NME2 | 0.937 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.3 + PDB: 1Q5H, 1Q5U, 2HQU, 3ARA, 3ARN,  | pLDDT=74.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Mitochondrion / Nucleoplasm | 一致 |
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
1. DUT — Deoxyuridine 5'-triphosphate nucleotidohydrolase, mitochondrial，有一定研究基础，但仍存在niche空间。
2. 蛋白大小252 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 130 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 130 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P33316
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128951-DUT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P33316
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:21:39

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000128951-DUT/subcellular

![](https://images.proteinatlas.org/54422/849_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/54422/849_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/54422/869_E11_4_red_green.jpg)
![](https://images.proteinatlas.org/54422/869_E11_5_red_green.jpg)
![](https://images.proteinatlas.org/54422/885_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/54422/885_E11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
