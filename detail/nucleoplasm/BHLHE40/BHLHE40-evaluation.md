---
type: protein-evaluation
gene: "BHLHE40"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BHLHE40 — REJECTED (研究热度过高 (PubMed strict=207，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BHLHE40 / BHLHB2, DEC1, SHARP2, STRA13 |
| 蛋白名称 | Class E basic helix-loop-helix protein 40 |
| 蛋白大小 | 412 aa / 45.5 kDa |
| UniProt ID | O14503 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 412 aa / 45.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=207 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050370, IPR036638, IPR003650; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 207 |
| PubMed broad count | 486 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB2, DEC1, SHARP2, STRA13 |

**关键文献**:
1. Autophagy in age-related macular degeneration.. *Autophagy*. PMID: 35468037
2. Temporal analyses of postnatal liver development and maturation by single-cell transcriptomics.. *Developmental cell*. PMID: 35134346
3. Differential chromatin accessibility and transcriptional dynamics define breast cancer subtypes and their lineages.. *Nature cancer*. PMID: 39478117
4. A systematic review of p53 regulation of oxidative stress in skeletal muscle.. *Redox report : communications in free radical research*. PMID: 29298131
5. BHLHE40 Cooperates with GATA2/3 to Control Human Syncytiotrophoblast Lineage Differentiation.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40911186

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.9 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 27.2% |
| 低置信 (pLDDT<50) 占比 | 45.4% |
| 有序区域 (pLDDT>70) 占比 | 27.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.9），有序残基占 27.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050370, IPR036638, IPR003650; Pfam: PF07527, PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARNTL | 0.985 | 0.232 | — |
| NPAS2 | 0.972 | 0.363 | — |
| BHLHE41 | 0.971 | 0.449 | — |
| CRY1 | 0.969 | 0.289 | — |
| PER2 | 0.955 | 0.276 | — |
| CLOCK | 0.939 | 0.279 | — |
| NFIL3 | 0.936 | 0.340 | — |
| PER3 | 0.930 | 0.141 | — |
| NR1D1 | 0.929 | 0.046 | — |
| NR1D2 | 0.913 | 0.186 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000256495.3 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| CHD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ZHX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BRD7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UBE2I | psi-mi:"MI:0018"(two hybrid) | pubmed:11278694|imex:IM-19104 |
| NUMBL | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| APH1A | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| HIVEP1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.9 + PDB: 无 | pLDDT=59.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BHLHE40 — Class E basic helix-loop-helix protein 40，研究基础较多，新颖性有限。
2. 蛋白大小412 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 207 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 207 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14503
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134107-BHLHE40/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BHLHE40
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14503
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000134107-BHLHE40/subcellular

![](https://images.proteinatlas.org/28922/583_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/28922/583_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/28922/598_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/28922/598_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/28922/602_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/28922/602_A10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14503-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
