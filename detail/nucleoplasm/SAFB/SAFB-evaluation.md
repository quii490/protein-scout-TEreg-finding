---
type: protein-evaluation
gene: "SAFB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SAFB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SAFB / HAP, HET, SAFB1 |
| 蛋白名称 | Scaffold attachment factor B1 |
| 蛋白大小 | 915 aa / 102.6 kDa |
| UniProt ID | Q15424 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Midbody; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 915 aa / 102.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=72 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR035979, IPR000504, IPR051738, IPR034 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Midbody | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- midbody (GO:0030496)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 72 |
| PubMed broad count | 150 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HAP, HET, SAFB1 |

**关键文献**:
1. Autonomous transposons tune their sequences to ensure somatic suppression.. *Nature*. PMID: 38355802
2. SAFB restricts contact domain boundaries associated with L1 chimeric transcription.. *Molecular cell*. PMID: 38604171
3. Hypoxia-induced DTL promotes the proliferation, metastasis, and sorafenib resistance of hepatocellular carcinoma through ubiquitin-mediated degradation of SLTM and subsequent Notch pathway activation.. *Cell death & disease*. PMID: 39384740
4. SAFB associates with nascent RNAs and can promote gene expression in mouse embryonic stem cells.. *RNA (New York, N.Y.)*. PMID: 37468167
5. The increasing diversity of functions attributed to the SAFB family of RNA-/DNA-binding proteins.. *The Biochemical journal*. PMID: 27888239

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.0 |
| 高置信度残基 (pLDDT>90) 占比 | 13.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 66.8% |
| 有序区域 (pLDDT>70) 占比 | 24.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.0），有序残基占 24.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR035979, IPR000504, IPR051738, IPR034781; Pfam: PF00076, PF02037 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TJP2 | 0.957 | 0.000 | — |
| ESR1 | 0.927 | 0.625 | — |
| RBMX | 0.921 | 0.620 | — |
| HNRNPA1 | 0.869 | 0.615 | — |
| HNRNPU | 0.860 | 0.211 | — |
| SRSF1 | 0.857 | 0.058 | — |
| KHDRBS1 | 0.793 | 0.071 | — |
| MATR3-2 | 0.793 | 0.359 | — |
| SRPK1 | 0.790 | 0.474 | — |
| ERH | 0.787 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ABHD16A | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| SRPK1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11509566 |
| CHD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| SAFB2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12660241|imex:IM-19378 |
| USP45 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| EEF1D | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| RB1CC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.0 + PDB: 无 | pLDDT=54.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Midbody | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SAFB — Scaffold attachment factor B1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小915 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 72 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15424
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160633-SAFB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAFB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15424
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000160633-SAFB/subcellular

![](https://images.proteinatlas.org/16832/131_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/16832/131_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/16832/132_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/16832/132_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/16832/164_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/16832/164_H11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15424-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
