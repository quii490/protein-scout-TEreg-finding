---
type: protein-evaluation
gene: "FBXO42"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO42 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO42 / FBX42, JFK, KIAA1332 |
| 蛋白名称 | F-box only protein 42 |
| 蛋白大小 | 717 aa / 77.8 kDa |
| UniProt ID | Q6P3S6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 717 aa / 77.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR052821, IPR015915; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX42, JFK, KIAA1332 |

**关键文献**:
1. Cullin-associated and neddylation-dissociated protein 1 (CAND1) alleviates NAFLD by reducing ubiquitinated degradation of ACAA2.. *Nature communications*. PMID: 37528093
2. Ubiquitination and degradation of SUMO1 by small-molecule degraders extends survival of mice with patient-derived tumors.. *Science translational medicine*. PMID: 34644148
3. Genome-wide CRISPR screens identify novel regulators of wild-type and mutant p53 stability.. *Molecular systems biology*. PMID: 38580884
4. Fbxo42 promotes the degradation of Ataxin-2 granules to trigger terminal Xbp1 signaling.. *Nature communications*. PMID: 40804044
5. FBXO42 promotes hepatocellular carcinoma progression via mediating p57Kip2 ubiquitination and degradation.. *European journal of medical research*. PMID: 40842039

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 32.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 46.4% |
| 有序区域 (pLDDT>70) 占比 | 46.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 46.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR052821, IPR015915; Pfam: PF13415, PF12937 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL1 | 0.949 | 0.838 | — |
| SKP1 | 0.898 | 0.699 | — |
| RBX1 | 0.804 | 0.627 | — |
| TP53 | 0.740 | 0.510 | — |
| CUL3 | 0.645 | 0.065 | — |
| RBPJ | 0.622 | 0.614 | — |
| PPP4R1 | 0.570 | 0.501 | — |
| FBXO38 | 0.555 | 0.000 | — |
| RNF25 | 0.534 | 0.000 | — |
| MAU2 | 0.533 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SkpB | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| SkpA | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Dmel\CG6569 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pus7 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RHOB | psi-mi:"MI:0018"(two hybrid) | pubmed:19637314|imex:IM-20406 |
| GABPI | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ccdc85 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CG6911 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 无 | pLDDT=63.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXO42 — F-box only protein 42，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小717 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P3S6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000037637-FBXO42/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO42
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P3S6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO42/IF_images/A-431_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO42/IF_images/U-251MG_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000037637-FBXO42/subcellular

![](https://images.proteinatlas.org/25071/224_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/25071/224_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/25071/226_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/25071/226_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/25071/261_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/25071/261_E8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P3S6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
