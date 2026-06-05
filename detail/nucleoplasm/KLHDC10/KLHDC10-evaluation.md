---
type: protein-evaluation
gene: "KLHDC10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHDC10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHDC10 / KIAA0265 |
| 蛋白名称 | Kelch domain-containing protein 10 |
| 蛋白大小 | 442 aa / 49.1 kDa |
| UniProt ID | Q6PID8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 442 aa / 49.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=84.5; PDB: 9D8P |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015915, IPR006652, IPR052125; Pfam: PF01344, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul2-RING ubiquitin ligase complex (GO:0031462)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0265 |

**关键文献**:
1. Ribosome-associated quality-control mechanisms from bacteria to humans.. *Molecular cell*. PMID: 35452614
2. Mechanism and evolutionary origins of alanine-tail C-degron recognition by E3 ligases Pirh2 and CRL2-KLHDC10.. *Cell reports*. PMID: 37676773
3. Principles of paralog-specific targeted protein degradation engaging the C-degron E3 KLHDC2.. *Nature communications*. PMID: 39396041
4. The Kelch repeat protein KLHDC10 regulates oxidative stress-induced ASK1 activation by suppressing PP5.. *Molecular cell*. PMID: 23102700
5. Genome-wide DNA methylation investigation of glucocorticoid exposure within buccal samples.. *Psychiatry and clinical neurosciences*. PMID: 30821055

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.5 |
| 高置信度残基 (pLDDT>90) 占比 | 74.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.1% |
| 低置信 (pLDDT<50) 占比 | 16.7% |
| 有序区域 (pLDDT>70) 占比 | 82.1% |
| 可用 PDB 条目 | 9D8P |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=84.5，有序区 82.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015915, IPR006652, IPR052125; Pfam: PF01344, PF24681 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL2 | 0.944 | 0.329 | — |
| FEM1B | 0.937 | 0.071 | — |
| APPBP2 | 0.933 | 0.000 | — |
| FEM1C | 0.931 | 0.071 | — |
| ZER1 | 0.930 | 0.000 | — |
| KLHDC3 | 0.927 | 0.000 | — |
| ZYG11B | 0.927 | 0.000 | — |
| FEM1A | 0.926 | 0.071 | — |
| KLHDC2 | 0.924 | 0.000 | — |
| ELOB | 0.914 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000334140.4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CUL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| NUDCD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| USP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| NEDD8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| GLMN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KITLG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PYCR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.5 + PDB: 9D8P | pLDDT=84.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHDC10 — Kelch domain-containing protein 10，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小442 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PID8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128607-KLHDC10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHDC10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PID8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000128607-KLHDC10/subcellular

![](https://images.proteinatlas.org/20119/234_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/20119/234_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/20119/235_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/20119/235_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/20119/535_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/20119/535_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PID8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
